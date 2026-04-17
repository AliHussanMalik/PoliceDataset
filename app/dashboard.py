import pandas as pd
import streamlit as st
from sqlalchemy import text

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

sys.path.insert(0, str(SRC))

from police_dataset.db import engine

# from police_dataset.db import engine


st.set_page_config(page_title="Pakistan Crime Dashboard", layout="wide")
st.title("Pakistan National Crime Dashboard (2000-2024)")


@st.cache_data
def load_data() -> pd.DataFrame:
    return pd.read_sql(text("SELECT * FROM crime_records"), engine)


df = load_data()

categories = sorted(df["crime_category"].unique().tolist())
selected_category = st.sidebar.selectbox("Crime Category", ["All"] + categories)

year_min, year_max = int(df["year"].min()), int(df["year"].max())
selected_range = st.sidebar.slider("Year Range", year_min, year_max, (year_min, year_max))

filtered = df[(df["year"] >= selected_range[0]) & (df["year"] <= selected_range[1])]
if selected_category != "All":
    filtered = filtered[filtered["crime_category"] == selected_category]

st.subheader("Snapshot")
col1, col2, col3 = st.columns(3)
col1.metric("Rows", f"{len(filtered):,}")
col2.metric("Years", f"{filtered['year'].nunique()}")
col3.metric("Total Crime Count", f"{int(filtered['crime_count'].sum()):,}")

st.subheader("Trend")
trend = filtered.groupby("year", as_index=False)["crime_count"].sum()
st.line_chart(trend.set_index("year"))

st.subheader("Latest Year Top Offences")
if not filtered.empty:
    latest_year = int(filtered["year"].max())
    latest_top = (
        filtered[filtered["year"] == latest_year]
        .sort_values("crime_count", ascending=False)
        .head(10)[["offence", "crime_count", "crime_category"]]
    )
    st.dataframe(latest_top, use_container_width=True)
else:
    st.info("No data in selected filter.")
