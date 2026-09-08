"""Start your chosen challenge here. Run with: python code/starter.py"""

from pathlib import Path

import pandas as pd


# Choose a year, a period and a measurement to investigate.
YEAR = 2023
START = "2023-06-01"
END = "2023-06-08"  # Stop before this date, so this selects seven days.
COLUMN = "power-gen-pv-ave"

# Find the data folder beside the code folder, wherever this project was saved.
PROJECT = Path(__file__).resolve().parent.parent
file = PROJECT / "data" / f"{YEAR}-Keele-Campus-Energy-Data.csv"
data = pd.read_csv(file)
data["DateTime"] = pd.to_datetime(data["DateTime"], errors="raise")
power_columns = ["power-con-ave", "power-gen-wt-ave", "power-gen-pv-ave"]
data[power_columns] = data[power_columns].apply(pd.to_numeric, errors="raise")

# Stop if missing readings or irregular times would make our sums misleading.
if data[["DateTime"] + power_columns].isna().any().any():
    raise ValueError("Missing values found. Ask a facilitator before calculating.")
gaps = data["DateTime"].diff().iloc[1:]
if not gaps.eq(pd.Timedelta(minutes=5)).all():
    raise ValueError("Timestamps are not five minutes apart. Ask a facilitator.")
if COLUMN not in power_columns:
    raise ValueError("Choose COLUMN from the three names in power_columns.")
if pd.Timestamp(START) >= pd.Timestamp(END):
    raise ValueError("START must be earlier than END.")

# Each row is one observation. Keep rows at or after START and before END.
period = data.loc[
    (data["DateTime"] >= START) & (data["DateTime"] < END)
].copy()
if period.empty:
    raise ValueError("No rows selected. Check YEAR, START and END.")

print(f"File: {file.name}")
print(f"Available timestamps: {data['DateTime'].min()} to {data['DateTime'].max()}")
print(f"Selected timestamps: {period['DateTime'].min()} to {period['DateTime'].max()}")
print(f"Selected rows: {len(period):,}; represented hours: {len(period) / 12:.2f}")
print(period.head().to_string(index=False))

# YOUR ANALYSIS
# Run this example first, then change COLUMN or the dates and compare the result.
# Replace or extend this section with snippets from code/README.md or your own code.
values = period[COLUMN]
print(f"Mean {COLUMN}: {values.mean():.2f} kW")
print(f"Maximum {COLUMN}: {values.max():.2f} kW")
