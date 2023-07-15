import os

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
    </style>
    """,
    unsafe_allow_html=True
)


@st.cache_data
def dataframe_load(filename):
    df = pd.read_csv(filename)
    df = df_formatting(df)
    return df

current_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(current_dir,'data/Artifical_Call_Log_Data.csv')
df = dataframe_load(filename)

# Consider Only Saved Contacts
field_dict = {'Contact': 'Saved'}
df = multiple_field_filter(df, field_dict)


sep_method = ['My Call Schedule', 'Person Wise Analysis']
methods = list(func_dict.keys())+sep_method
contact_name = df['Name'].unique().tolist()


st.subheader('Analyze Your Call Records')
col1, col2 = st.columns([1, 1])

with col1:
    choosen_method = st.selectbox("Methods",
                                  methods,
                                  key='Methods')


if choosen_method in sep_method:
    if choosen_method == 'My Call Schedule':
        fig = call_time_fig(df)
        st.plotly_chart(fig, use_container_width=True)
    else:
        with col2:
            choosen_name = st.selectbox("Name",
                                        contact_name,
                                        key='Name')

        fig1, fig2 = person_wise_stats(df, choosen_name)
        st.plotly_chart(fig1, use_container_width=True)
        st.plotly_chart(fig2, use_container_width=True)

else:
    kwrgs = func_dict[choosen_method]()
    field_dict = kwrgs.pop('field_dict')

    fil_df = multiple_field_filter(df, field_dict)
    fig = generate_fig(fil_df, **kwrgs)
    st.plotly_chart(fig, use_container_width=True)
