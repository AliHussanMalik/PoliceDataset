from sqlalchemy import Float, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .db import Base


class CrimeRecord(Base):
    __tablename__ = "crime_records"
    __table_args__ = (UniqueConstraint("year", "offence", name="uq_year_offence"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    year: Mapped[int] = mapped_column(Integer, index=True)
    offence: Mapped[str] = mapped_column(String(120), index=True)
    crime_count: Mapped[int] = mapped_column(Integer)
    population: Mapped[int] = mapped_column(Integer)
    data_source: Mapped[str] = mapped_column(String(80))
    literacy_rate: Mapped[float] = mapped_column(Float)
    gdp_billion_usd: Mapped[float] = mapped_column(Float)
    unemployment_rate: Mapped[float] = mapped_column(Float)
    poverty_rate: Mapped[float] = mapped_column(Float)
    urbanization_rate: Mapped[float] = mapped_column(Float)
    crime_rate_per_100k: Mapped[float] = mapped_column(Float)
    gdp_per_capita_usd: Mapped[float] = mapped_column(Float)
    crime_category: Mapped[str] = mapped_column(String(60), index=True)
    decade: Mapped[int] = mapped_column(Integer, index=True)
