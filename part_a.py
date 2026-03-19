"""
part_a.py
Part A – Concept Application
Covers: loc, iloc, Filtering, describe(), Histogram, Bar Plot, Line Chart, KDE Plot
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os

matplotlib.use("Agg")          # headless rendering
os.makedirs("outputs", exist_ok=True)

# ── Load dataset ──────────────────────────────────────────────────────────────
df = pd.read_csv("data/sales_data.csv", parse_dates=["Date"])
print("Dataset loaded:", df.shape)
print(df.head(3))

# =============================================================================
# A1 – Data Selection using loc
# =============================================================================
print("\n── A1: loc examples ──")

# Example 1 – Select first 5 rows, specific columns
loc_ex1 = df.loc[0:4, ["Date", "Region", "Sales"]]
print("\nloc Ex1 – rows 0-4, columns Date/Region/Sales:")
print(loc_ex1)

# Example 2 – Rows where Region is 'North', show Sales and Profit
loc_ex2 = df.loc[df["Region"] == "North", ["Region", "Sales", "Profit"]].head(5)
print("\nloc Ex2 – North region rows:")
print(loc_ex2)

# Example 3 – Rows with Sales > 500, show Date, Category, Sales
loc_ex3 = df.loc[df["Sales"] > 500, ["Date", "Category", "Sales"]].head(5)
print("\nloc Ex3 – rows where Sales > 500:")
print(loc_ex3)

# =============================================================================
# A2 – Data Selection using iloc
# =============================================================================
print("\n── A2: iloc examples ──")

# Example 1 – First 5 rows, first 3 columns
iloc_ex1 = df.iloc[0:5, 0:3]
print("\niloc Ex1 – rows 0-4, cols 0-2:")
print(iloc_ex1)

# Example 2 – Last 5 rows, last 3 columns
iloc_ex2 = df.iloc[-5:, -3:]
print("\niloc Ex2 – last 5 rows, last 3 cols:")
print(iloc_ex2)

# Example 3 – Every 100th row, columns at index 1, 3, 5
iloc_ex3 = df.iloc[::100, [1, 3, 5]]
print("\niloc Ex3 – every 100th row, cols at index 1,3,5:")
print(iloc_ex3)

# =============================================================================
# A3 – Filtering Data
# =============================================================================
print("\n── A3: Filtering ──")

# Filter 1 – High-value Electronics sales
electronics_high = df[(df["Category"] == "Electronics") & (df["Sales"] > 400)]
print(f"\nFilter 1 – Electronics with Sales > 400: {len(electronics_high)} rows")
print(electronics_high[["Date", "Category", "Sales", "Profit"]].head(5))

# Filter 2 – Profitable North/East sales with low discount
north_east_profit = df[
    (df["Region"].isin(["North", "East"])) &
    (df["Profit"] > 100) &
    (df["Discount"] < 0.1)
]
print(f"\nFilter 2 – North/East, Profit>100, Discount<0.1: {len(north_east_profit)} rows")
print(north_east_profit[["Region", "Sales", "Profit", "Discount"]].head(5))

# Filter 3 – Young customers with high quantity orders
young_bulk = df[(df["Customer_Age"] < 30) & (df["Quantity"] > 30)]
print(f"\nFilter 3 – Age<30 and Qty>30: {len(young_bulk)} rows")
print(young_bulk[["Customer_Age", "Quantity", "Sales"]].head(5))

# =============================================================================
# A4 – Descriptive Statistics
# =============================================================================
print("\n── A4: describe() ──")
stats = df[["Sales", "Quantity", "Profit", "Discount", "Customer_Age"]].describe()
print(stats)

print("\n── Interpretation ──")
print(f"Sales  → mean={stats['Sales']['mean']:.1f}, std={stats['Sales']['std']:.1f}")
print(f"        min={stats['Sales']['min']:.1f}, max={stats['Sales']['max']:.1f}")
print("        High std means Sales values are spread out; a few very large transactions pull the mean up.")
print(f"Profit → mean={stats['Profit']['mean']:.1f}, can go negative (losses possible).")
print(f"Discount → mean={stats['Discount']['mean']:.2f} (~{stats['Discount']['mean']*100:.0f}% avg discount).")

# =============================================================================
# A5 – Histogram (Sales distribution)
# =============================================================================
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(df["Sales"], bins=30, color="steelblue", edgecolor="white")
ax.set_title("Sales Distribution (Histogram)")
ax.set_xlabel("Sales (₹)")
ax.set_ylabel("Frequency")
ax.grid(axis="y", alpha=0.4)
plt.tight_layout()
plt.savefig("outputs/a5_histogram_sales.png", dpi=120)
plt.close()
print("\nA5 – Histogram saved → outputs/a5_histogram_sales.png")
print("Interpretation: Distribution is right-skewed. Most transactions are below ₹400,")
print("but a few high-value orders stretch the tail to the right.")

# =============================================================================
# A6 – Bar Plot (Average Sales by Category)
# =============================================================================
avg_sales = df.groupby("Category")["Sales"].mean().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(avg_sales.index, avg_sales.values, color=["#4C72B0","#DD8452","#55A868","#C44E52","#8172B2"])
ax.set_title("Average Sales by Category")
ax.set_xlabel("Category")
ax.set_ylabel("Average Sales (₹)")
ax.bar_label(bars, fmt="%.0f", padding=3)
ax.grid(axis="y", alpha=0.4)
plt.tight_layout()
plt.savefig("outputs/a6_bar_category_sales.png", dpi=120)
plt.close()
print("\nA6 – Bar plot saved → outputs/a6_bar_category_sales.png")

# =============================================================================
# A7 – Line Chart (Monthly total Sales over time)
# =============================================================================
monthly = df.resample("ME", on="Date")["Sales"].sum()

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(monthly.index, monthly.values, marker="o", color="teal", linewidth=2)
ax.set_title("Monthly Total Sales – Trend Over Time")
ax.set_xlabel("Month")
ax.set_ylabel("Total Sales (₹)")
ax.grid(alpha=0.4)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/a7_line_monthly_sales.png", dpi=120)
plt.close()
print("A7 – Line chart saved → outputs/a7_line_monthly_sales.png")

# =============================================================================
# A8 – KDE Plot (Sales density vs histogram overlay)
# =============================================================================
import numpy as np
from scipy.stats import gaussian_kde

x = np.linspace(df["Sales"].min(), df["Sales"].max(), 300)
kde = gaussian_kde(df["Sales"])

fig, ax = plt.subplots(figsize=(8, 5))
# Normalised histogram
ax.hist(df["Sales"], bins=30, density=True, color="steelblue", alpha=0.5,
        edgecolor="white", label="Histogram (normalised)")
# KDE curve
ax.plot(x, kde(x), color="red", linewidth=2, label="KDE")
ax.set_title("Sales – KDE vs Histogram")
ax.set_xlabel("Sales (₹)")
ax.set_ylabel("Density")
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("outputs/a8_kde_sales.png", dpi=120)
plt.close()
print("A8 – KDE plot saved → outputs/a8_kde_sales.png")
print("KDE smooths out the histogram bins giving a cleaner view of the distribution shape.")
print("\nAll Part A outputs saved in ./outputs/")
