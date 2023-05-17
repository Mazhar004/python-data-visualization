import datetime
import pandas as pd

# Web
import streamlit as st

# Custom
from covid_streamlit_view import covid_lines_stats, covid_bars_stats

github_logo = 'https://img.shields.io/badge/GitHub-Repo-blue?logo=github'
repo_url = 'https://github.com/Mazhar004/python-data-visualization/tree/master/Streamlit/covid'
repo = f'[![GitHub Repo]({github_logo})]({repo_url})'


def date_conv(str_date, format='%Y-%m-%d'):
    str_date = datetime.datetime.strptime(str_date, format).date()
    return str_date


csv_path = '../../Corona Affected Country/plotly/data/full_stats.csv'
df_index = ['Dataset', 'Country']
df = pd.read_csv(csv_path, index_col=df_index)
df = df.rename(columns=date_conv)
cols = df.columns


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
