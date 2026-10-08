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

    print("\nFinancial Analysis:")
    print(df[columns].round(2).to_string(index=False))


# temporario - teste
if __name__ == "__main__":
    from load_data import load_financial_data

    df = load_financial_data()

    df = calculate_margins(df)
    df = calculate_revenue_growth(df)
    df = calculate_returns(df)

    display_analysis(df)
