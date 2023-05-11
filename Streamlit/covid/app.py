import datetime
import pandas as pd

# Web
import streamlit as st

# Custom
from covid_streamlit_view import covid_lines_stats, covid_bars_stats

github_logo = 'https://img.shields.io/badge/GitHub-Repo-blue?logo=github'
repo_url = 'https://github.com/Mazhar004/python-data-visualization/tree/streamlit_covid_app/Streamlit/covid'
repo = f'[![GitHub Repo]({github_logo})]({repo_url})'


def date_conv(str_date, format='%Y-%m-%d'):
    str_date = datetime.datetime.strptime(str_date, format)
    return str_date


df = pd.read_csv('../../Corona Affected Country/plotly/data/full_stats.csv')
date_formatted = {item: date_conv(item) for item in df.columns[2:]}
df = df.rename(columns=date_formatted).replace({-1: 0})


st.set_page_config(page_title="COVID Stats", layout="wide")
st.markdown(repo, unsafe_allow_html=True)
# Disable Streamlit menu button and footer
st.markdown(
    """
    <style>
    #MainMenu, footer {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

### StreamLit View ###
covid_lines_stats(df)
covid_bars_stats(df)
