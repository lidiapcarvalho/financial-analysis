import pandas as pd


def load_financial_data():
    df = pd.read_excel("data/financial-data.xlsx", header=2)
    return df


# temporario
if __name__ == "__main__":
    df = load_financial_data()

    print("Columns:")
    print(df.columns.tolist())

    print("\nShape:")
    print(df.shape)

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isna().sum())

    print("\nCompanies:")
    print(df["Company"].unique())

    print("\nFiscal years:")
    print(df["Fiscal Year"].unique())

    print("\nFinancial data summary:")
    print(df.describe())

    print("\nRows by company:")
    print(df.groupby("Company")["Fiscal Year"].agg(["min", "max", "count"]))
