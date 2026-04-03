import datetime
import os
from itertools import product

import pandas as pd
import streamlit as st

from fig_generate import line_fig_gen
from map_keys import BANK_ABBREVIATION, DEPOSIT_TYPE, TENURE

st.set_page_config(page_title="Bank Stats", layout="wide")
st.markdown(
    """
    <style>
    #MainMenu, footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

GITHUB_LOGO = "https://img.shields.io/badge/GitHub-Repo-blue?logo=github"
REPO_URL = (
    "https://github.com/Mazhar004/python-data-visualization"
    "/tree/master/Streamlit/BangladeshBankDeposit"
)
st.markdown(f"[![GitHub Repo]({GITHUB_LOGO})]({REPO_URL})", unsafe_allow_html=True)


def parse_date(str_date, fmt="%Y-%m-%d"):
    """Parse a date string into a date object."""
    return datetime.datetime.strptime(str_date, fmt).date()


@st.cache_data
def data_load(csv_path):
    """Load and prepare the bank deposit CSV data."""
    df = pd.read_csv(csv_path, header=[0, 1])

    bank_name_col, date_col, *_ = df.columns

    df[bank_name_col] = df[bank_name_col].replace(BANK_ABBREVIATION)
    df[date_col] = df[date_col].apply(parse_date)
    bank_name_list = df[bank_name_col].unique()

    min_date, max_date = (
        df[date_col].iloc[0].strftime("%d %b, %Y"),
        df[date_col].iloc[-1].strftime("%d %b, %Y"),
    )
    subheader = (
        f"Deposit Rate Analysis for Banks of Bangladesh "
        f"from ({min_date} - {max_date})"
    )

    return df, bank_name_list, subheader


# Dynamic filepath load
current_dir = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(current_dir))
filename = "Streamlit/BangladeshBankDeposit/data/Processed_11 Aug 2023.csv"
csv_path = os.path.join(root, filename)

# Data Load
df, bank_name_list, subheader = data_load(csv_path)
bank_name_col, date_col, *columns = df.columns

st.subheader(subheader)

COMP_TYPES = ["Bank Wise", "Same Bank Deposit Wise"]
comp = st.selectbox("Comparision Type", COMP_TYPES, key="Comparision Type")

bank_wise_flag = comp == COMP_TYPES[0]

col1, col2, col3 = st.columns(3)
with col1:
    if bank_wise_flag:
        name_list = st.multiselect(
            "Select Bank Names", BANK_ABBREVIATION.values(), key="Bank Name"
        )
    else:
        name_list = st.selectbox(
            "Select Bank Names", BANK_ABBREVIATION.values(), key="Bank Name"
        )

with col2:
    dtype = st.selectbox("Select Deposit Type", DEPOSIT_TYPE, key="Deposit Name")

with col3:
    if dtype:
        if bank_wise_flag:
            duration = st.selectbox(
                "Select Amount/Duration of Deposit",
                TENURE[dtype],
                key="Deposit Duration",
            )
        else:
            duration = st.multiselect(
                "Select Amount/Duration of Deposit",
                TENURE[dtype],
                key="Deposit Duration",
            )

if name_list and dtype and duration:
    name_list = name_list if isinstance(name_list, list) else [name_list]
    duration = duration if isinstance(duration, list) else [duration]

    resolved_durations = []
    duration_labels = []
    for d in duration:
        if d == "Not Applicable":
            resolved_durations.append(DEPOSIT_TYPE[dtype])
        else:
            resolved_durations.append(d)
            duration_labels.append(d)

    duration_text = '" VS "'.join(duration_labels).strip()

    if bank_wise_flag:
        title = f'{comp} comparision "{dtype}"'
        if duration_text:
            title += f' for "{duration_text}"'
    else:
        title = f'"{name_list[0]}" comparision of "{dtype}"'

    y_cols = list(product([DEPOSIT_TYPE[dtype]], resolved_durations))
    final_col = [bank_name_col, date_col, *y_cols]

    # Bank Filter
    temp_df = df[df[bank_name_col].isin(name_list)]
    # Column Filter
    temp_df = temp_df.get(final_col).reset_index(drop=True)

    fig = line_fig_gen(temp_df, bank_name_col, date_col, title, bank_wise_flag)
    st.plotly_chart(fig, use_container_width=True)
