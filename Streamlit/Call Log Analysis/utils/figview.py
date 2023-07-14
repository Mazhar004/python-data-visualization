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

