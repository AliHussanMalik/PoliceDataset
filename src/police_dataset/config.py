from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "pakistan_crimes_national_2000_2024.csv"
DB_PATH = PROJECT_ROOT / "data" / "processed" / "crimes.db"
PLOTS_DIR = PROJECT_ROOT / "outputs" / "plots"
DATABASE_URL = f"sqlite:///{DB_PATH.as_posix()}"
