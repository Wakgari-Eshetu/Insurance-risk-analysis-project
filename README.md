**Project:** Insurance Risk Analysis

- **Description:** Small project for exploring an insurance dataset and performing data understanding, EDA, and visualization. Contains helper modules in `src/` and notebooks in `notebook/`.

**Quick Start**
- Create a virtual environment (recommended):
  - Windows PowerShell:
    ```powershell
    python -m venv .venv; .\.venv\Scripts\Activate.ps1
    ```
- Install dependencies:
  ```powershell
  pip install -r requirements.txt
  ```
- Run the main script from project root:
  ```powershell
  python main.py
  ```

**Notes**
- The project uses a Jupyter notebook `notebook/dataunderstanding.ipynb` which `main.py` may import via `import-ipynb`. That package is listed in `requirements.txt`.
- If you prefer a stable importable module, convert the notebook to a Python script and place it in `src/`:
  ```powershell
  jupyter nbconvert --to script notebook/dataunderstanding.ipynb
  Move-Item notebook\dataunderstanding.py src\dataunderstanding.py -Force
  ```
- Data file used: `data/MachineLearningRating_v3.txt` (pipe-delimited). Ensure that file exists in the `data/` folder.

**Troubleshooting**
- If import of the notebook fails, install `import-ipynb` and restart Python:
  ```powershell
  pip install import-ipynb
  ```
- If you see date-parsing errors when loading data, `src/dataloader.py` will auto-coerce common date columns; make sure your file uses the expected delimiters.

**Files of interest**
- `main.py`: entry point
- `src/`: helper modules (dataloader, dataclean, eda, visualizer, utils)
- `notebook/dataunderstanding.ipynb`: DataUnderstanding class and exploratory code
- `data/`: original dataset files

If you want, I can also add a simple `Makefile` or PowerShell script to automate setup and run steps.
# Insurance-risk-analysis-project