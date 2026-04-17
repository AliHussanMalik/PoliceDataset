# Pakistan Crime Analytics Project

This repository is structured for a reproducible data workflow:
- CSV raw data in `data/raw/`
- SQLite database in `data/processed/crimes.db`
- Alembic migrations in `alembic/`
- Python package code in `src/police_dataset/`
- Notebook analysis in `notebooks/`
- Streamlit app in `app/dashboard.py`

## 1) Virtual Environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If your Python build cannot bootstrap pip (you may see `No module named pip`), repair Python installation features (ensure `pip`/`venv` are included), then recreate `.venv`.

## 2) Install Dependencies
```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## 3) Run Migrations
```powershell
.\scripts\run_migrations.ps1
```

## 4) Load Data
```powershell
.\scripts\load_data.ps1
```

## 5) Generate Visualizations
```powershell
.\scripts\plot_charts.ps1
```
Generated charts are saved in `outputs/plots/`.

## 6) Launch Dashboard
```powershell
$env:PYTHONPATH = "$(Resolve-Path .\src)"
.\.venv\Scripts\python.exe -m streamlit run .\app\dashboard.py
```

## 7) Open Notebook
```powershell
$env:PYTHONPATH = "$(Resolve-Path .\src)"
.\.venv\Scripts\python.exe -m jupyter notebook
```
Then open `notebooks/01_crime_analysis.ipynb`.
