from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sqlalchemy import text

from .config import PLOTS_DIR
from .db import engine


sns.set_theme(style="whitegrid")


def _read_df() -> pd.DataFrame:
    return pd.read_sql(text("SELECT * FROM crime_records"), engine)


def make_visualizations(output_dir: Path = PLOTS_DIR) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    df = _read_df()
    saved_files: list[Path] = []

    yearly = (
        df.groupby("year", as_index=False)["crime_count"]
        .sum()
        .sort_values("year")
    )
    plt.figure(figsize=(12, 5))
    sns.lineplot(data=yearly, x="year", y="crime_count", marker="o")
    plt.title("Total Recorded Crimes by Year")
    plt.xlabel("Year")
    plt.ylabel("Crime Count")
    path_1 = output_dir / "yearly_crime_trend.png"
    plt.tight_layout()
    plt.savefig(path_1, dpi=150)
    plt.close()
    saved_files.append(path_1)

    latest_year = int(df["year"].max())
    latest_top = (
        df[df["year"] == latest_year]
        .sort_values("crime_count", ascending=False)
        .head(10)
    )
    plt.figure(figsize=(12, 6))
    sns.barplot(data=latest_top, x="crime_count", y="offence", hue="crime_category", dodge=False)
    plt.title(f"Top 10 Offences in {latest_year}")
    plt.xlabel("Crime Count")
    plt.ylabel("Offence")
    path_2 = output_dir / "top_offences_latest_year.png"
    plt.tight_layout()
    plt.savefig(path_2, dpi=150)
    plt.close()
    saved_files.append(path_2)

    return saved_files


if __name__ == "__main__":
    files = make_visualizations()
    print("Saved visualizations:")
    for file in files:
        print(file)
