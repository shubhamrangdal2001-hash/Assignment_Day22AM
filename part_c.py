"""
part_c.py
Part C – Interview Ready
Q1: loc vs iloc  |  Q2: Filter rows above average  |  Q3: describe()
"""

import pandas as pd

df = pd.read_csv("data/sales_data.csv", parse_dates=["Date"])

# =============================================================================
# Q1 – What is the difference between loc and iloc in Pandas?
# =============================================================================
"""
Answer:
    loc  → label-based selection. You refer to row/column by their actual
            index label or column name.
    iloc → integer position-based selection. You refer to rows/columns by
            their integer position (0, 1, 2 ...) regardless of labels.

    Key difference:
    - loc includes the end of a slice (df.loc[0:4] gives 5 rows).
    - iloc excludes the end  (df.iloc[0:4] gives 4 rows), just like Python lists.

    Example:
        df.loc[0, "Sales"]    → value at label 0, column "Sales"
        df.iloc[0, 3]         → value at row position 0, column position 3
"""

print("── Q1 Demo ──")
print("loc  [0, 'Sales']  :", df.loc[0, "Sales"])
print("iloc [0,  3]       :", df.iloc[0, 3])   # column 3 is 'Sales'

# =============================================================================
# Q2 – Filter rows where a column value is greater than average
# =============================================================================
print("\n── Q2: Filter rows where Sales > mean(Sales) ──")

avg_sales = df["Sales"].mean()
above_avg = df[df["Sales"] > avg_sales]

print(f"Average Sales      : ₹{avg_sales:.2f}")
print(f"Rows above average : {len(above_avg)}")
print(above_avg[["Date", "Category", "Region", "Sales"]].head(8).to_string(index=False))

# One-liner version (also acceptable)
above_avg_oneliner = df[df["Sales"] > df["Sales"].mean()]
print(f"\nOne-liner row count: {len(above_avg_oneliner)}")

# =============================================================================
# Q3 – What is the purpose of describe()? What insights can we get from it?
# =============================================================================
"""
Answer:
    describe() generates a quick statistical summary of all numeric columns.
    By default it shows: count, mean, std, min, 25th percentile (Q1),
    median (Q2 / 50%), 75th percentile (Q3), and max.

    Insights we can get:
    1. Central Tendency  – mean and median help understand the typical value.
    2. Spread / Variability – std and IQR (Q3 - Q1) show how spread out the data is.
    3. Range             – min and max reveal extreme values quickly.
    4. Skewness hint     – if mean >> median, data is right-skewed.
    5. Outlier detection – if max is far from Q3, there could be outliers.
    6. Missing data      – count < total rows → null values present.
"""

print("\n── Q3: describe() output ──")
print(df[["Sales", "Profit", "Quantity", "Discount"]].describe().round(2))
print("\nInterpretation:")
print("- Sales mean > median → right-skewed distribution (a few large orders).")
print("- Profit std ≈ 40 means profit varies significantly per transaction.")
print("- Discount range 0–0.4 confirms no extreme outliers in discount values.")
