# Data Processing
import pandas as pd

# Web
import streamlit as st

# Custom
from utils.figconfig import func_dict
from utils.figview import generate_fig, person_wise_stats, call_time_fig
from utils.preprocessing import df_formatting, multiple_field_filter


github_logo = 'https://img.shields.io/badge/GitHub-Repo-blue?logo=github'
repo_url = 'https://github.com/Mazhar004/python-data-visualization/tree/master/Streamlit/Call%20Log%20Analysis'
repo = f'[![GitHub Repo]({github_logo})]({repo_url})'

st.set_page_config(page_title="Call Stats", layout="wide")
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


@st.cache_data
def dataframe_load(filename):
    df = pd.read_csv(filename)
    df = df_formatting(df)
    return df


filename = 'data/Artifical_Call_Log_Data.csv'
df = dataframe_load(filename)

