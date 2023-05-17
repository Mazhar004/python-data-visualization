from itertools import product

# Web
import streamlit as st

# Custom
from utils import date_filter, build_bar_data
from covid_fig import covid_analyze_lines, covid_analyze_bars


def covid_lines_stats(df, min_date, max_date, country_list, d_type_list):
    st.subheader('COVID-19 Line Chart by Country')

    col1, col2 = st.columns([1, 3])
    with col1:
        countries = st.multiselect(
            "Select countries to analyze", country_list, key='Country Name')
        d_types = st.multiselect(
            "Select data types", d_type_list, key='Data Type')
        date_range = st.slider("Select a date range", min_value=min_date,
                               max_value=max_date, value=(min_date, max_date), key='Line Date')
    with col2:
        indexes = list(product(d_types, countries))
        temp_df = df.loc[indexes, :]

        st_index = (date_range[0]-min_date).days+2
        lt_index = (date_range[1] - date_range[0]).days + st_index
        temp_df = date_filter(temp_df, st_index, lt_index)

        fig = covid_analyze_lines(temp_df)
        st.plotly_chart(fig, use_container_width=True)


def covid_bars_stats(df):
    # Top Country
    d_type_list = df['Dataset'].unique().tolist()

    min_date = min(df.columns[2:]).date()
    max_date = max(df.columns[2:]).date()

    st.subheader('Top Countries Affected by COVID-19')

    col1, col2 = st.columns([1, 3])
    with col1:
        top_k = st.selectbox(
            "Select number of countries", [10, 15, 20, 25, 30], key='Top K')
        d_types = st.selectbox(
            "Select data type", d_type_list, key='Data Type Single')
        date_range = st.slider("Select a date range", min_value=min_date,
                               max_value=max_date, value=(min_date, max_date), key='Bar Date')
    with col2:
        temp_df = dtype_filter(df, [d_types])
        temp_df = date_filter(temp_df, date_range[0], date_range[1])
        temp_df = build_bar_data(temp_df)

        fig = covid_analyze_bars(
            temp_df, d_types, date_range[0], date_range[1], top_k)
        st.plotly_chart(fig, use_container_width=True)
