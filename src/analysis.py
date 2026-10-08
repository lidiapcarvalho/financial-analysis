import pandas as pd


def calculate_margins(df):
    df["Operating Margin"] = (
        df["Operating Income"] / df["Revenue"] * 100
    )

    df["Net Profit Margin"] = (
        df["Net Income"] / df["Revenue"] * 100
    )

    return df


def calculate_revenue_growth(df):
    df = df.sort_values(["Company", "Fiscal Year"]).copy()

    df["Revenue Growth"] = (
        df.groupby("Company")["Revenue"]
        .pct_change()
        * 100
    )

    return df


def calculate_returns(df):
    df = df.sort_values(["Company", "Fiscal Year"]).copy()

    df["Average Total Assets"] = (
        df.groupby("Company")["Total Assets"]
        .transform(lambda x: x.rolling(2).mean())
    )

    df["Average Equity"] = (
        df.groupby("Company")["Equity"]
        .transform(lambda x: x.rolling(2).mean())
    )

    df["Return on Assets (ROA)"] = (
        df["Net Income"] / df["Average Total Assets"] * 100
    )

    df["Return on Equity (ROE)"] = (
        df["Net Income"] / df["Average Equity"] * 100
    )

    return df


def display_analysis(df):
    columns = [
        "Company",
        "Fiscal Year",
        "Revenue",
        "Revenue Growth",
        "Operating Margin",
        "Net Profit Margin",
        "Return on Assets (ROA)",
        "Return on Equity (ROE)",
    ]

    display_df = df[columns].round(2)

    display_df = display_df.rename(columns={
        "Return on Assets (ROA)": "ROA",
        "Return on Equity (ROE)": "ROE"
    })

    print("\nFinancial Analysis:")
    print(display_df.to_string(index=False))


def compare_period(df):
    comparison = df[df["Fiscal Year"].between(2020, 2025)].copy()

    start = comparison[comparison["Fiscal Year"] == 2020].set_index("Company")
    end = comparison[comparison["Fiscal Year"] == 2025].set_index("Company")

    comparison_df = pd.DataFrame({
        "Revenue (2020)": start["Revenue"],
        "Revenue (2025)": end["Revenue"],
        "Operating Margin (2020)": start["Operating Margin"],
        "Operating Margin (2025)": end["Operating Margin"],
        "Net Profit Margin (2020)": start["Net Profit Margin"],
        "Net Profit Margin (2025)": end["Net Profit Margin"],
        "ROA (2020)": start["Return on Assets (ROA)"],
        "ROA (2025)": end["Return on Assets (ROA)"],
        "ROE (2020)": start["Return on Equity (ROE)"],
        "ROE (2025)": end["Return on Equity (ROE)"],
    })

    return comparison_df

def calculate_period_changes(comparison_df):
    comparison_df["Revenue Change (%)"] = (
        (comparison_df["Revenue (2025)"] / comparison_df["Revenue (2020)"] - 1)
        * 100
    )

    comparison_df["Operating Margin Change (p.p.)"] = (
        comparison_df["Operating Margin (2025)"]
        - comparison_df["Operating Margin (2020)"]
    )

    comparison_df["Net Profit Margin Change (p.p.)"] = (
        comparison_df["Net Profit Margin (2025)"]
        - comparison_df["Net Profit Margin (2020)"]
    )

    return comparison_df

    # temporario - teste
if __name__ == "__main__":
    from load_data import load_financial_data

    df = load_financial_data()

    df = calculate_margins(df)
    df = calculate_revenue_growth(df)
    df = calculate_returns(df)

    display_analysis(df)

    comparison = compare_period(df)

    print("\n2020–2025 Comparison:")
    print(comparison.round(2).to_string())

    comparison = calculate_period_changes(comparison)

    print("\n2020–2025 Performance Changes:")
    print(
        comparison[
            [
                "Revenue Change (%)",
                "Operating Margin Change (p.p.)",
                "Net Profit Margin Change (p.p.)",
            ]
        ].round(2).to_string()
    )