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


# temporario
if __name__ == "__main__":
    from load_data import load_financial_data

    df = load_financial_data()

    df = calculate_margins(df)
    df = calculate_revenue_growth(df)

    print(df)
