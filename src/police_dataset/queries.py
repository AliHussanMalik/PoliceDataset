import pandas as pd
from sqlalchemy import text

from .db import engine


def offense_trend(offence: str) -> pd.DataFrame:
    query = text(
        """
        SELECT year, crime_count
        FROM crime_records
        WHERE offence = :offence
        ORDER BY year ASC
        """
    )
    return pd.read_sql(query, engine, params={"offence": offence})


def top_offences(year: int, n: int = 10) -> pd.DataFrame:
    query = text(
        """
        SELECT offence, crime_count
        FROM crime_records
        WHERE year = :year
        ORDER BY crime_count DESC
        LIMIT :n
        """
    )
    return pd.read_sql(query, engine, params={"year": year, "n": n})
