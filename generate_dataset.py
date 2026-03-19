"""
generate_dataset.py
Generates a synthetic retail sales dataset with 600+ rows.
Run this first before any other part scripts.
"""

import pandas as pd
import numpy as np
import os

np.random.seed(42)

n = 600

regions     = ["North", "South", "East", "West"]
categories  = ["Electronics", "Clothing", "Furniture", "Sports", "Books"]

dates = pd.date_range(start="2022-01-01", periods=n, freq="D")

data = {
    "Date":         dates,
    "Region":       np.random.choice(regions, n),
    "Category":     np.random.choice(categories, n),
    "Sales":        np.round(np.random.exponential(scale=300, size=n) + 50, 2),
    "Quantity":     np.random.randint(1, 50, n),
    "Profit":       np.round(np.random.normal(loc=80, scale=40, size=n), 2),
    "Discount":     np.round(np.random.uniform(0, 0.4, n), 2),
    "Customer_Age": np.random.randint(18, 65, n),
}

df = pd.DataFrame(data)

os.makedirs("data", exist_ok=True)
df.to_csv("data/sales_data.csv", index=False)
print(f"Dataset saved → data/sales_data.csv  ({len(df)} rows, {len(df.columns)} columns)")
print(df.head())
