"""create crime_records table

Revision ID: 20260416_0001
Revises:
Create Date: 2026-04-16 18:45:00
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "20260416_0001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "crime_records",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("offence", sa.String(length=120), nullable=False),
        sa.Column("crime_count", sa.Integer(), nullable=False),
        sa.Column("population", sa.Integer(), nullable=False),
        sa.Column("data_source", sa.String(length=80), nullable=False),
        sa.Column("literacy_rate", sa.Float(), nullable=False),
        sa.Column("gdp_billion_usd", sa.Float(), nullable=False),
        sa.Column("unemployment_rate", sa.Float(), nullable=False),
        sa.Column("poverty_rate", sa.Float(), nullable=False),
        sa.Column("urbanization_rate", sa.Float(), nullable=False),
        sa.Column("crime_rate_per_100k", sa.Float(), nullable=False),
        sa.Column("gdp_per_capita_usd", sa.Float(), nullable=False),
        sa.Column("crime_category", sa.String(length=60), nullable=False),
        sa.Column("decade", sa.Integer(), nullable=False),
        sa.UniqueConstraint("year", "offence", name="uq_year_offence"),
    )
    op.create_index("ix_crime_records_year", "crime_records", ["year"])
    op.create_index("ix_crime_records_offence", "crime_records", ["offence"])
    op.create_index("ix_crime_records_crime_category", "crime_records", ["crime_category"])
    op.create_index("ix_crime_records_decade", "crime_records", ["decade"])


def downgrade() -> None:
    op.drop_index("ix_crime_records_decade", table_name="crime_records")
    op.drop_index("ix_crime_records_crime_category", table_name="crime_records")
    op.drop_index("ix_crime_records_offence", table_name="crime_records")
    op.drop_index("ix_crime_records_year", table_name="crime_records")
    op.drop_table("crime_records")
