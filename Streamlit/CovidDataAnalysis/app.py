from datetime import datetime
from pathlib import Path

import pandas as pd
import streamlit as st

from covid_streamlit_view import covid_bars_stats, covid_lines_stats

GITHUB_LOGO = "https://img.shields.io/badge/GitHub-Repo-blue?logo=github"
REPO_URL = (
    "https://github.com/Mazhar004/python-data-visualization"
    "/tree/master/Streamlit/CovidDataAnalysis"
)
REPO_BADGE = f"[![GitHub Repo]({GITHUB_LOGO})]({REPO_URL})"

HIDE_STREAMLIT_STYLE = """
<style>
#MainMenu, footer {visibility: hidden;}
</style>
"""


def parse_date(date_str, fmt="%Y-%m-%d"):
    return datetime.strptime(date_str, fmt).date()


def load_data():
    current_dir = Path(__file__).resolve().parent
    csv_path = current_dir.parent.parent / "CoronaAffectedCountry/Plotly/data/full_stats.csv"

    index_cols = ["Dataset", "Country"]
    df = pd.read_csv(csv_path, index_col=index_cols)
    df = df.rename(columns=parse_date)
    return df


df = load_data()
cols = df.columns

min_date, max_date = min(cols), max(cols)
d_type_list = df.index.get_level_values(0).unique()
country_list = df.index.get_level_values(1).unique()

st.set_page_config(page_title="COVID Stats", layout="wide")
st.markdown(REPO_BADGE, unsafe_allow_html=True)
st.markdown(HIDE_STREAMLIT_STYLE, unsafe_allow_html=True)

covid_lines_stats(df, min_date, max_date, country_list, d_type_list)
covid_bars_stats(df, min_date, max_date, d_type_list)
