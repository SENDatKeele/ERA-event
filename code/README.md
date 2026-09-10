# Start your chosen challenge

After the shared warm-up, choose a question in [TASK.md](../TASK.md), then open [starter.ipynb](starter.ipynb). The notebook combines short explanations, editable code, tables and plots. Start with sections 1–4, then choose the optional examples that help with your question.

## Set up VS Code

You need Python 3.10 or later and Microsoft's Python and Jupyter extensions.

1. Open the extracted project folder in VS Code, where `TASK.md` is saved.
2. Open Extensions with `Ctrl+Shift+X`. Install **Python** by Microsoft, extension ID `ms-python.python`, and **Jupyter** by Microsoft, extension ID `ms-toolsai.jupyter`. This project recommends both alongside VS Plotter.
3. Choose **Terminal > New Terminal**. Check Python with `python --version`.
4. Install the notebook packages with `python -m pip install -r code/requirements.txt`. These provide data tables, plots and the Python notebook kernel.
5. Open `code/starter.ipynb`. At the top right, choose **Select Kernel**, then **Python Environments**, and select the Python environment where you installed the packages. A kernel is the Python session that runs the cells.

If Windows recognises `py` instead of `python`, use `py` in the terminal commands. If Python is missing, installation is blocked or you cannot select a kernel, ask for help. See the [official VS Code notebook guide](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) for further setup help.

## Run and explore

Click the run button beside a code cell, or select it and press **Shift+Enter**. Run the first four sections from top to bottom. Tables and plots appear directly beneath their code. The default example selects 1–7 June 2023, with 2,016 readings covering 168 hours.

Change the year, dates or measurement in section 1 to investigate your question. Change `WINDOW_HOURS` in section 4 to try different rolling averages. The comments beside these settings suggest values to try. You can leave the data-loading code as it is.

When you change a cell, rerun it and the later cells that use its results. Editing a setting does not automatically update earlier outputs. If results seem inconsistent, use **Restart Kernel**, then **Run All**. All examples can run in order; the optional CSV export is switched off by default.

## Develop your answer

The optional sections cover energy totals, monthly comparisons, excess electricity and zero readings. Each uses the data from sections 1–2. Run only the examples useful for your question, and adapt or add code as needed.

Use **+ Code** to add a calculation and **+ Markdown** to add notes. Double-click a text cell to edit it, then press **Shift+Enter** to display it. Record your group's question, findings and limitations in the final section. Save with **Ctrl+S** to keep the notebook and its displayed results.

GitHub can display a saved notebook, but it does not run its cells. Download and open the project locally to work with it.

## If something goes wrong

- **A package is missing:** check that the selected kernel matches the Python used for installation. You can run `import sys; print(sys.executable)` in a code cell and `python -c "import sys; print(sys.executable)"` in the terminal to compare them.
- **A name such as `period` is not defined:** run sections 1–2 first. Restarting the kernel clears its variables.
- **No rows are selected:** check that the dates match the chosen year and that `START` is earlier than `END`.
- **The data folder cannot be found:** open the extracted project folder in VS Code, then reopen the notebook.

If you share your work or continue it after the event, follow [ACKNOWLEDGEMENTS.md](../ACKNOWLEDGEMENTS.md).
