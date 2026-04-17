from pathlib import Path

import pandas as pd

from .config import RAW_DATA_PATH
from .db import SessionLocal
from .models import CrimeRecord


def load_csv(path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def seed_database(path: Path = RAW_DATA_PATH) -> int:
    df = load_csv(path)
    records = df.to_dict(orient="records")

    session = SessionLocal()
    try:
        session.query(CrimeRecord).delete()
        session.bulk_insert_mappings(CrimeRecord, [
            {
                "year": int(row["Year"]),
                "offence": str(row["Offence"]),
                "crime_count": int(row["Crime_Count"]),
                "population": int(row["Population"]),
                "data_source": str(row["Data_Source"]),
                "literacy_rate": float(row["Literacy_Rate"]),
                "gdp_billion_usd": float(row["GDP_Billion_USD"]),
                "unemployment_rate": float(row["Unemployment_Rate"]),
                "poverty_rate": float(row["Poverty_Rate"]),
                "urbanization_rate": float(row["Urbanization_Rate"]),
                "crime_rate_per_100k": float(row["Crime_Rate_Per_100K"]),
                "gdp_per_capita_usd": float(row["GDP_Per_Capita_USD"]),
                "crime_category": str(row["Crime_Category"]),
                "decade": int(row["Decade"]),
            }
            for row in records
        ])
        session.commit()
        return len(records)
    finally:
        session.close()


if __name__ == "__main__":
    total = seed_database()
    print(f"Loaded {total} records into database.")
