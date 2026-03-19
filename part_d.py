"""
part_d.py
Part D – AI-Augmented Task
Documents the AI prompt used, evaluates the AI output, and demonstrates
the validated code from that output.
"""

# =============================================================================
# Prompt sent to AI (Claude / ChatGPT)
# =============================================================================
PROMPT = """
Explain how to perform data analysis using Pandas and visualization using
Matplotlib with examples.
"""

# =============================================================================
# AI Output (summarised and documented)
# =============================================================================
AI_OUTPUT_SUMMARY = """
The AI gave a clear step-by-step response covering:

1. Loading data with pd.read_csv()
2. Exploring data with .head(), .info(), .describe()
3. Filtering with boolean conditions
4. Grouping with .groupby() and .agg()
5. Plotting with matplotlib – hist(), bar(), plot(), and KDE using scipy

Example code it provided (for histogram):

    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv("data.csv")
    df["Sales"].hist(bins=20, color="steelblue", edgecolor="white")
    plt.title("Sales Distribution")
    plt.xlabel("Sales")
    plt.ylabel("Frequency")
    plt.show()
"""

# =============================================================================
# Evaluation of AI Output
# =============================================================================
EVALUATION = """
Evaluation:
- Are the plots correct?
  YES. The histogram code is correct. The bins, labels, and show() call are
  all properly placed. I ran it and it produced the expected output.

- Is the explanation meaningful?
  YES. The AI broke down each step clearly. The groupby explanation was
  especially useful – it showed both .mean() and .agg({}) syntax.

- What needed fixing?
  Minor: The AI used plt.show() which doesn't work in headless/save mode.
  I replaced it with plt.savefig() for file output.
  Also, it didn't mention parse_dates when loading date columns – I added
  that manually.

Overall the AI output was about 85% ready to use directly. The remaining
15% needed small fixes based on my understanding of the dataset.
"""

# =============================================================================
# Validated / corrected code from AI output
# =============================================================================
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os

matplotlib.use("Agg")
os.makedirs("outputs", exist_ok=True)

df = pd.read_csv("data/sales_data.csv", parse_dates=["Date"])   # added parse_dates

# Validated histogram from AI suggestion
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(df["Sales"], bins=20, color="steelblue", edgecolor="white")
ax.set_title("Sales Distribution")
ax.set_xlabel("Sales")
ax.set_ylabel("Frequency")
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("outputs/d_validated_histogram.png", dpi=120)  # replaced show() with savefig()
plt.close()

print("Part D – Documentation")
print("=" * 50)
print("PROMPT USED:")
print(PROMPT)
print("AI OUTPUT SUMMARY:")
print(AI_OUTPUT_SUMMARY)
print("EVALUATION:")
print(EVALUATION)
print("Validated plot saved → outputs/d_validated_histogram.png")
