import pandas as pd

# Load CSV
df = pd.read_csv("sales_data.csv")

print("===== Dataset =====")
print(df)

print("\n===== First 5 Rows =====")
print(df.head())

print("\n===== Dataset Information =====")
df.info()

print("\n===== Summary Statistics =====")
print(df.describe())

print("\n===== Electronics Products =====")
print(df[df["Category"] == "Electronics"])

print("\n===== Total Quantity by Category =====")
print(df.groupby("Category")["Quantity"].sum())
