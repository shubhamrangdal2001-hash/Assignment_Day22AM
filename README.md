# Week 04 – Day 22 (AM Session) Assignment
**PG Diploma · AI-ML & Agentic AI Engineering · IIT Gandhinagar**

Topics: Pandas (loc, iloc, Filtering, describe) · Matplotlib (Histogram, Bar Plot, Line Chart, KDE Plot)
Gitlink: https://github.com/shubhamrangdal2001-hash/Assignment_Day22AM.git
---

## Folder Structure

```
.
├── data/
│   └── sales_data.csv          # auto-generated dataset (600 rows)
├── outputs/
│   ├── a5_histogram_sales.png
│   ├── a6_bar_category_sales.png
│   ├── a7_line_monthly_sales.png
│   ├── a8_kde_sales.png
│   ├── b2_grouped_bar.png
│   ├── b3_line_sales_profit.png
│   ├── b3_kde_sales_profit.png
│   └── d_validated_histogram.png
├── generate_dataset.py         # Step 1 – create the CSV
├── part_a.py                   # Part A – loc, iloc, filter, describe, plots
├── part_b.py                   # Part B – grouped analysis & comparison
├── part_c.py                   # Part C – interview Q&A + code
├── part_d.py                   # Part D – AI-augmented task
└── README.md
```

---

## How to Run

### 1. Install dependencies
```bash
pip install pandas matplotlib scipy numpy
```

### 2. Generate the dataset
```bash
python generate_dataset.py
```

### 3. Run each part
```bash
python part_a.py
python part_b.py
python part_c.py
python part_d.py
```

All charts are saved to the `outputs/` folder.

---

## Dataset Description

Synthetic retail sales data with **600 rows** and the following columns:

| Column | Type | Description |
|---|---|---|
| Date | datetime | Transaction date (2022-01-01 onwards) |
| Region | string | North / South / East / West |
| Category | string | Electronics / Clothing / Furniture / Sports / Books |
| Sales | float | Transaction value (₹) |
| Quantity | int | Units sold |
| Profit | float | Profit per transaction (can be negative) |
| Discount | float | Discount rate (0.0 – 0.4) |
| Customer_Age | int | Customer age (18–64) |

---

## Key Findings

- Sales distribution is **right-skewed** – most transactions are under ₹400 but some large orders exist.
- **Electronics** tends to have the highest average sales across categories.
- Profit has a roughly normal distribution centred around ₹80.
- No strong seasonal trend is visible in the monthly sales line chart.
