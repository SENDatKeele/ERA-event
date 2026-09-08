# Start your chosen challenge

After the shared warm-up, choose a challenge in [TASK.md](../TASK.md) and open `starter.py` in this folder. It loads a CSV, selects a period and runs a simple calculation. You can then change it to investigate your group's question.

Use this README for setup instructions and short examples you can add to the starter. Choose only the examples that help with your question, or write your own code.

## Run the starter

The starter uses Python 3.10 or later and pandas, a package for working with tables of data.

1. Open the extracted project folder in VS Code.
2. Choose **Terminal > New Terminal**. The terminal should open in the project folder, where `TASK.md` is saved.
3. Check Python with `python --version`.
4. Install the package if needed with `python -m pip install -r code/requirements.txt`.
5. Open `code/starter.py`, then run `python code/starter.py` in the terminal.

If Windows recognises `py` instead of `python`, use `py` wherever a command starts with `python`. If Python is missing, installation is blocked or a command fails, ask for help.

On the first run, you should see the selected dates, 2,016 rows covering seven days, the first five rows, and the mean and maximum solar power. The example uses 1 to 7 June 2023.

## Make it your own

Write down the question your group wants to investigate. Change the four choices near the top of `starter.py`, save with `Ctrl+S`, then run it again:

| Choice | Meaning | Example |
| --- | --- | --- |
| `YEAR` | Which annual file to open | `2024` |
| `START` | First timestamp to include | `"2024-06-01"` |
| `END` | Stop before this timestamp | `"2024-06-08"` |
| `COLUMN` | Which measurement to analyse | `"power-con-ave"` |

Change the dates when you change the year. Keep quotation marks around dates and column names. The three column names are in the [data dictionary](../data/data_dictionary.md).

`data` is the full table. `period` is the selected part of it. `period[COLUMN]` selects one measurement. Text after `#` is a comment explaining the code. `print(...)` displays a result in the terminal.

Read the selected timestamps and row count before calculating. The files may start or end at a different time from the period you requested. These examples group by the supplied timestamp; they do not shift timestamps or infer whether a reading labels the start or end of an interval.

The `YOUR ANALYSIS` section at the bottom contains the example calculation. Keep the loading and selection code above it, then replace or extend this section as your question develops.

For example, to investigate peak demand, change `COLUMN` to `"power-con-ave"` and run the file again. Use the average and maximum snippet below to find when the peak occurred. Change the week to check whether the same pattern appears again.

## Choose a calculation

| Your question | Examples to start with |
| --- | --- |
| Challenge 2: compare years or months | Average and maximum power; energy during the selected period; monthly comparison |
| Challenge 3: find excess electricity | Find excess power; view your selected data in VS Plotter |
| Challenge 4: investigate zeros | Locate zeros; view your selected data in VS Plotter |
| Challenge 5: explore a flexible response | Find excess power, then investigate the size and timing of the opportunity |

Copy a code block into the `YOUR ANALYSIS` section of `starter.py`. The blocks use the data already loaded by the starter, so run the whole file rather than a block on its own. You can combine blocks, for example calculating excess before exporting the selected data.

Save and run after each change. Read the output in the terminal, check what it means and decide what to try next. Keep useful results and your assumptions in your own notes.

### Average and maximum power

Useful for comparing periods in Challenge 2. Choose the period and column at the top of the starter.

```python
values = period[COLUMN]
print(f"Mean {COLUMN}: {values.mean():.2f} kW")
print(f"Maximum {COLUMN}: {values.max():.2f} kW")
peak_row = values.idxmax()
print(f"First timestamp at that maximum: {period.loc[peak_row, 'DateTime']}")
```

Does the maximum describe a typical day? What changes if you choose a different week? For solar, remember that the mean includes night-time readings.

### Energy during the selected period

Useful for Challenge 2. Every reading is five-minute average power in kW. Dividing its sum by 12,000 gives energy in MWh.

```python
energy_mwh = period[COLUMN].sum() / 12000
print(f"{COLUMN}, selected period: {energy_mwh:.3f} MWh")
```

What changes if you double the selected period? Can you explain why summing kW readings alone does not give kWh?

### Monthly comparison

This block uses the whole file, `data`, rather than the selected week. It reports only the readings present in each calendar month.

```python
monthly = data.set_index("DateTime")[power_columns].resample("MS").sum() / 12000
monthly.columns = ["consumption_MWh", "wind_MWh", "solar_MWh"]
monthly["renewable_to_demand_ratio"] = (
    (monthly["wind_MWh"] + monthly["solar_MWh"])
    / monthly["consumption_MWh"].replace(0, float("nan"))
)
print(monthly.round(3).to_string())
print("Readings per month:")
print(data.set_index("DateTime").resample("MS").size().to_string())
```

Which months are complete? A boundary month may contain only a few readings. Compare the same months in another year by changing `YEAR`. The ratio compares total generation with total demand; it does not say how much demand was supplied by renewables at the same time.

### Find excess power

Useful for Challenges 3 and 5. Work out the sign of generation minus demand before running this block.

```python
period["generation_kW"] = period["power-gen-wt-ave"] + period["power-gen-pv-ave"]
period["balance_kW"] = period["generation_kW"] - period["power-con-ave"]
period["excess_kW"] = period["balance_kW"].clip(lower=0)
excess_rows = period["excess_kW"] > 0
print(f"Hours with excess: {excess_rows.sum() / 12:.2f}")
print(f"Excess energy: {period['excess_kW'].sum() / 12000:.3f} MWh")
print(f"Largest five-minute average excess: {period['excess_kW'].max():.2f} kW")
```

`.clip(lower=0)` replaces negative balances with zero. Why would adding negative balances give a different answer? The hours here may be scattered across many events; they are not the duration of one continuous event. Inspect demand and generation before trusting an apparent surplus. This calculation alone does not size a battery or electrolyser.

### Locate zeros

Useful for Challenge 4. Choose the measurement at the top of the starter.

```python
zero_rows = period[COLUMN] == 0
print(f"Zero readings: {zero_rows.sum()} out of {len(period)}")
print(period.loc[zero_rows, ["DateTime", COLUMN]].head(20).to_string(index=False))
```

Only the first 20 matching rows are displayed. What would you plot or compare to investigate the zeros? This block counts them; it does not identify failures, detect every quality problem or replace readings.

### View your selected data in VS Plotter

Use this after any other snippet if you want to inspect the selected rows and any new columns. It writes a new CSV beside the starter. It does not change the supplied data files.

```python
output = PROJECT / "code" / "selected-period.csv"
period.to_csv(output, index=False)
print(f"Saved {output}")
```

Open `code/selected-period.csv` with VS Plotter. Select `DateTime` as X and the measurements you want as Y. Running this export again replaces that output, so rename it first if you want to keep a previous result.
