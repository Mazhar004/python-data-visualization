import datetime
import pandas as pd

# Web
import streamlit as st

# Custom
from covid_streamlit_view import covid_lines_stats, covid_bars_stats


def date_conv(str_date, format='%Y-%m-%d'):
    str_date = datetime.datetime.strptime(str_date, format)
    return str_date


df = pd.read_csv('../../Corona Affected Country/plotly/data/full_stats.csv')
date_formatted = {item: date_conv(item) for item in df.columns[2:]}
df = df.rename(columns=date_formatted)


st.set_page_config(layout="wide")

### StreamLit View ###
covid_lines_stats(df)
covid_bars_stats(df)
