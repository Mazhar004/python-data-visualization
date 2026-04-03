"""Streamlit application for analyzing call log data."""

from pathlib import Path

import pandas as pd
import streamlit as st

from utils.figconfig import func_dict
from utils.figview import call_time_fig, generate_fig, person_wise_stats
from utils.preprocessing import df_formatting, multiple_field_filter

# --- Page configuration ---

GITHUB_LOGO = "https://img.shields.io/badge/GitHub-Repo-blue?logo=github"
REPO_URL = (
    "https://github.com/Mazhar004/python-data-visualization"
    "/tree/master/Streamlit/CallLogAnalysis"
)

HIDE_STREAMLIT_UI = """
<style>
#MainMenu, footer {visibility: hidden;}
</style>
"""

st.set_page_config(page_title="Call Stats", layout="wide")
st.markdown(f"[![GitHub Repo]({GITHUB_LOGO})]({REPO_URL})", unsafe_allow_html=True)
st.markdown(HIDE_STREAMLIT_UI, unsafe_allow_html=True)


# --- Data loading ---

@st.cache_data
def load_dataframe(filename: str) -> pd.DataFrame:
    """Load CSV and apply formatting transformations."""
    df = pd.read_csv(filename)
    return df_formatting(df)


DATA_PATH = Path(__file__).parent / "data" / "Artifical_Call_Log_Data.csv"
df = load_dataframe(str(DATA_PATH))

# Consider only saved contacts
df = multiple_field_filter(df, {"Contact": "Saved"})


# --- Sidebar / method selection ---

SEPARATE_METHODS = ["My Call Schedule", "Person Wise Analysis"]
methods = list(func_dict.keys()) + SEPARATE_METHODS
contact_names = df["Name"].unique().tolist()

st.subheader("Analyze Your Call Records")
col1, col2 = st.columns([1, 1])

with col1:
    chosen_method = st.selectbox("Methods", methods, key="Methods")


# --- Render selected chart ---

if chosen_method in SEPARATE_METHODS:
    if chosen_method == "My Call Schedule":
        fig = call_time_fig(df)
        st.plotly_chart(fig, use_container_width=True)
    else:
        with col2:
            chosen_name = st.selectbox("Name", contact_names, key="Name")

        fig1, fig2 = person_wise_stats(df, chosen_name)
        st.plotly_chart(fig1, use_container_width=True)
        st.plotly_chart(fig2, use_container_width=True)

else:
    kwrgs = func_dict[chosen_method]()
    field_dict = kwrgs.pop("field_dict")

    fil_df = multiple_field_filter(df, field_dict)
    fig = generate_fig(fil_df, **kwrgs)
    st.plotly_chart(fig, use_container_width=True)
