# Keele campus energy hackathon

Your group will use Keele campus energy data to investigate a practical question:

> When do wind and solar generation match or exceed campus electricity demand, and what could Keele do with that information?

You do not need previous experience in energy, data analysis or coding. Useful contributions include spotting patterns, checking whether a result is credible, questioning assumptions and explaining what a finding could mean in practice.

## Start here

1. Download the project from GitHub. Select **Code**, then **Download ZIP**.
2. Extract the ZIP file before opening it.
3. Open the extracted folder in Visual Studio Code.
4. Read [TASK.md](TASK.md).
5. Check [data/data_dictionary.md](data/data_dictionary.md) before analysing the data.
6. Use VS Plotter to open one CSV file and complete the shared warm-up in [TASK.md](TASK.md#shared-warm-up).
7. Choose your next challenge in [TASK.md](TASK.md), then open [code/README.md](code/README.md) to start working in Python.

A GitHub account is not required.

## VS Plotter

Use [VS Plotter by Rafael Arvelo](https://marketplace.visualstudio.com/items?itemName=RafaelArvelo.vsplotter), extension ID `RafaelArvelo.vsplotter`. It lets you inspect and plot the CSV files without writing code.

In VS Code, open Extensions with `Ctrl+Shift+X`, search for `RafaelArvelo.vsplotter` and install it if needed. This folder also recommends the extension. On an event computer, ask a facilitator if it is unavailable.

The shared warm-up gives the plotting steps. After that, choose a challenge and use tools your group is comfortable with. Ask a facilitator if you need help getting started.

## Project files

- [TASK.md](TASK.md) contains the shared warm-up, four group challenges and the presentation requirements.
- [data/data_dictionary.md](data/data_dictionary.md) explains the columns, units and calculations.
- [code/starter.py](code/starter.py) loads the data and runs a first calculation for you to adapt to your chosen challenge.
- [code/README.md](code/README.md) explains how to run the starter and add calculations to it.
- `data/2023-Keele-Campus-Energy-Data.csv`
- `data/2024-Keele-Campus-Energy-Data.csv`
- `data/2025-Keele-Campus-Energy-Data.csv`
- The opening briefing is available as a [PDF](slides/ERA-Hackathon-Data-Briefing.pdf) or an editable [PowerPoint](slides/ERA-Hackathon-Data-Briefing.pptx).

## Keep these points in mind

- The readings are average power values in kilowatts for five-minute intervals.
- A zero does not automatically mean that equipment or a sensor failed.
- The 2023 file is reviewed and repaired. The 2024 and 2025 files are reconstructed datasets.
- These files contain historical observations.
- State your assumptions and explain anything you are unsure about.

## Group presentations

Prepare one slide for a short presentation of about one minute. Focus on one finding; you do not need to report everything you tried.

Show:

- one clearly labelled plot;
- one key finding or question from the data;
- why it matters or how it could be used.

State any assumption or limitation needed to understand your finding. Include a number where it helps. Facilitators will explain how to submit the slide on the day.

## Data acknowledgement and citation

If you share your event work or continue using these data afterwards, acknowledge the SEND team at Keele University and cite both the data repository and the associated paper. See [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md) for what to include, wording you can adapt and the full paper citation.
