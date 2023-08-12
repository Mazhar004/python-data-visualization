from itertools import product
import os
import datetime
import pandas as pd

# Web
import streamlit as st

from map_keys import BANK_ABBREVIATION, DEPOSIT_TYPE, TENURE
from fig_generate import line_fig_gen

st.set_page_config(page_title="Bank Stats", layout="wide")
# Disable Streamlit menu button and footer
st.markdown(
    """
    <style>
    #MainMenu, footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

github_logo = 'https://img.shields.io/badge/GitHub-Repo-blue?logo=github'
repo_url = 'https://github.com/Mazhar004/python-data-visualization/tree/master/Streamlit/BangladeshBankDeposit'
repo = f'[![GitHub Repo]({github_logo})]({repo_url})'
st.markdown(repo, unsafe_allow_html=True)


def date_conv(str_date, format='%Y-%m-%d'):
    str_date = datetime.datetime.strptime(str_date, format).date()
    return str_date


@st.cache_data
def data_load(csv_path):
    df = pd.read_csv(csv_path, header=[0, 1])

    bank_name_col, date_col, *_ = df.columns

    df[bank_name_col] = df[bank_name_col].replace(BANK_ABBREVIATION)
    df[date_col] = df[date_col].apply(date_conv)
    bank_name_list = df[bank_name_col].unique()

    temp_dates = df[date_col].iloc[0], df[date_col].iloc[-1]
    min_date, max_date = map(lambda x: x.strftime("%d %b, %Y"), temp_dates)
    subheader = f'Deposit Rate Analysis for Banks of Bangladesh from ({min_date} - {max_date})'

    return df, bank_name_list, subheader


# Dynamic filepath load
current_dir = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(current_dir))
filename = "Streamlit\BangladeshBankDeposit\data\Processed_11 Aug 2023.csv"
csv_path = os.path.join(root, filename)

# Data Load
df, bank_name_list, subheader = data_load(csv_path)
bank_name_col, date_col, *columns = df.columns


st.subheader(subheader)

comp_type = ["Bank Wise", "Same Bank Deposit Wise"]
comp = st.selectbox("Comparision Type",
                    comp_type,
                    key='Comparision Type')

bank_wise_flag = comp == comp_type[0]

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if bank_wise_flag:
        name_list = st.multiselect("Select Bank Names",
                                   BANK_ABBREVIATION.values(),
                                   key='Bank Name')
    else:
        name_list = st.selectbox("Select Bank Names",
                                 BANK_ABBREVIATION.values(),
                                 key='Bank Name')

with col2:
    dtype = st.selectbox("Select Deposit Type",
                         DEPOSIT_TYPE,
                         key='Deposit Name')
with col3:
    if dtype:
        if bank_wise_flag:
            duration = st.selectbox("Select Amount/Duration of Deposit",
                                    TENURE[dtype],
                                    key='Deposit Duration')
        else:
            duration = st.multiselect("Select Amount/Duration of Deposit",
                                      TENURE[dtype],
                                      key='Deposit Duration')

if name_list and dtype and duration:
    name_list = name_list if isinstance(name_list, list) else [name_list]
    duration = duration if isinstance(duration, list) else [duration]

    temp_list = []
    duration_text = []
    for d in duration:
        if d == "Not Applicable":
            temp_list.append(DEPOSIT_TYPE[dtype])
            continue
        temp_list.append(d)
        duration_text.append(d)

    duration = temp_list
    duration_text = "\" VS \"".join(duration_text).strip()

    if bank_wise_flag:
        title = f"{comp} comparision \"{dtype}\""
        if duration_text:
            title += f" for \"{duration_text}\""

    else:
        title = f"\"{name_list[0]}\" comparision of \"{dtype}\""

    y_cols = list(product([DEPOSIT_TYPE[dtype]], duration))
    final_col = [bank_name_col, date_col]+y_cols

    # Bank Filter
    temp_df = df[df[bank_name_col].isin(name_list)]
    # Column Filter
    temp_df = temp_df.get(final_col).reset_index(drop=True)

    fig = line_fig_gen(temp_df,
                       bank_name_col,
                       date_col,
                       title,
                       bank_wise_flag)
    st.plotly_chart(fig, use_container_width=True)
