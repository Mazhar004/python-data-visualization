import pandas as pd

# Visualize
import plotly.express as px

# Custom
from utils.preprocessing import multiple_field_filter
from utils.utils import cal_total_min, average_total_sec, frequency_count, hour_format, individual_count, individual_group


def generate_fig(df,
                 group_by,
                 function,
                 col_name,
                 title,
                 fig_attr={},
                 top_k=None):
    temp_df = df.groupby(group_by).apply(function)
    temp_df = temp_df.to_frame(name=col_name).reset_index()
    temp_df = temp_df.sort_values(by=col_name, ascending=False)

    if top_k:
        temp_df = temp_df.iloc[:top_k]

    fig = px.bar(temp_df, x=group_by[0], y=col_name, title=title, **fig_attr)
    return fig


def time_fig_generate(df, group_by, function, col_name, title, fig_attr={}):
    fil_df = df.copy()
    fil_df['Hour'] = fil_df.Date.apply(lambda x: x.hour)

    fil_df = fil_df.groupby(group_by).apply(function)
    fil_df = fil_df.to_frame(name=col_name).reset_index()
    fil_df['Hour_Hover'] = fil_df.Hour.apply(hour_format)

    fil_df = fil_df.sort_values(by='Hour', ascending=False)
    fig = px.bar(fil_df,
                 x=group_by[0],
                 y=col_name,
                 title=title,
                 hover_name='Hour_Hover',
                 **fig_attr)
    return fig


def call_time_fig(df, name='My'):
    field_dict = {'Status': 'Answered'}
    fil_df = multiple_field_filter(df, field_dict)

    group_by = ['Hour', 'Direction']
    col_name = 'Frequency'
    title = f'{name} Call Schedule'
    fig_attr = {'color': 'Direction', 'barmode': 'group'}

    fig = time_fig_generate(fil_df, group_by, frequency_count, col_name, title,
                            fig_attr)
    return fig


