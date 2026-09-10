# Keele campus energy challenge

## Your aim

Use the 2023 to 2025 SEND campus energy data to find a useful pattern, check whether the data support it and explain what Keele could responsibly do next.

Everyone completes the shared warm-up. Your group then chooses one challenge.

## Shared warm-up

1. Open one annual CSV file in VS Code.
2. Identify the date range, four columns and their units.
3. Plot campus consumption, wind generation and solar generation for one day or one week.
4. Record one pattern that looks reasonable.
5. Record one feature that you would check before relying on it.

Use [VS Plotter by Rafael Arvelo](https://marketplace.visualstudio.com/items?itemName=RafaelArvelo.vsplotter). You do not need to write code.

With the CSV open, press `Ctrl+Shift+P` and run `VSPlotter: Create Plot from file`. Select `DateTime` for X and all three power columns for Y: `power-con-ave`, `power-gen-wt-ave` and `power-gen-pv-ave`. Drag across the plot to zoom into one day or week; double-click to reset the view.

Check that X shows dates and times, and identify each series using the data dictionary. All three Y columns are in kW. If the time axis does not display correctly, ask a facilitator before interpreting the plot.

Discuss what you notice before moving to a challenge. You can use your own code or AI assistance for further analysis, but check the results and be ready to explain what was calculated.

## Choose one challenge

Choose a question below, then open the [code folder guide](code/README.md). Open `starter.ipynb` and run its cells to load the data and see your first plot. Change the dates and measurement to suit your question, then use the notebook's optional examples or your own code to investigate further.

### Challenge 2: compare the years

How did campus electricity demand and renewable generation change between 2023, 2024 and 2025?

Investigate annual or monthly demand, wind generation and solar generation. Identify the periods with the highest and lowest renewable-generation-to-demand ratios.

Report:

- the comparison you made;
- one important difference between years;
- whether the difference could reflect the way the datasets were prepared;
- what the comparison does not prove.

Do not describe total renewable generation divided by total demand as the proportion of campus demand supplied by renewables. Supply depends on whether generation and demand occur at the same time.

### Challenge 3: find excess renewable electricity

When, how often and for how long did renewable generation exceed campus demand?

Calculate total generation and excess power:

```text
generation_kW = wind_kW + solar_kW
balance_kW = generation_kW - consumption_kW
excess_kW = max(balance_kW, 0)
```

Investigate:

- the total number of excess intervals or hours;
- the months and times of day when excess occurred most often;
- the largest or longest excess event;
- whether the event was linked to high generation, low demand or both.

Check suspicious values before assuming an apparent excess event is real.

### Challenge 4: audit the zeros

Which zero values look expected, and which need further investigation?

Look for:

- solar zeros that occur at night;
- wind zeros that could reflect calm weather, turbine availability or a data problem;
- consumption zeros or long repeated runs;
- missing timestamps or irregular time gaps.

Create a simple data-quality rule for one decision, such as calculating annual energy, finding a five-minute peak or sizing storage. Explain why your rule suits that decision.

The data alone cannot prove that a sensor or piece of equipment failed. Use terms such as **expected**, **plausible**, **suspicious** and **needs checking**.

### Challenge 5: advise

What flexible response could make use of one recurring excess-energy pattern?

Choose an observed pattern and consider battery storage, electric-vehicle charging, hydrogen production or flexible building demand.

Report:

- the size of the opportunity in kW or MWh;
- how long the pattern usually lasts;
- which response appears compatible with it;
- the assumptions behind your suggestion;
- what Keele would need to measure or confirm before acting.

The datasets do not contain asset capacities, efficiencies, availability, costs or genuine forecasts so treat your answer as an evidence-based proposal instead of direct proof that the option is feasible.

## Useful calculations

Each row records average power during a five-minute interval.

```text
Energy in MWh = sum of five-minute power readings in kW / 12,000
```

For the total duration of a set of five-minute intervals:

```text
Hours = number of intervals / 12
```

Read [data/data_dictionary.md](data/data_dictionary.md) before using the formulas.

## Your one-minute presentation

Prepare one slide with:

1. One clearly labelled plot.
2. One key finding or question from the data.
3. Why it matters or how it could be used.

Aim for about one minute. You do not need to present everything you did. Include a number where it helps, and state any assumption or limitation needed to understand your finding. There will be time for discussion during the wrap-up.

Facilitators will explain how to submit your slide on the day. You do not need a GitHub account or write access to this repository.
