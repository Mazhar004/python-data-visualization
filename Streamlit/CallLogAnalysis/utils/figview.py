"""Figure generation functions for call log visualizations."""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.preprocessing import multiple_field_filter
from utils.utils import (
    average_total_sec,
    cal_total_min,
    frequency_count,
    hour_format,
    individual_count,
    individual_group,
)


def generate_fig(
    df: pd.DataFrame,
    group_by: list[str],
    function: callable,
    col_name: str,
    title: str,
    fig_attr: dict | None = None,
    top_k: int | None = None,
) -> go.Figure:
    """Generate a bar chart from grouped/aggregated call data."""
    if fig_attr is None:
        fig_attr = {}

    temp_df = df.groupby(group_by).apply(function)
    temp_df = temp_df.to_frame(name=col_name).reset_index()
    temp_df = temp_df.sort_values(by=col_name, ascending=False)

    if top_k:
        temp_df = temp_df.iloc[:top_k]

    return px.bar(temp_df, x=group_by[0], y=col_name, title=title, **fig_attr)


def time_fig_generate(
    df: pd.DataFrame,
    group_by: list[str],
    function: callable,
    col_name: str,
    title: str,
    fig_attr: dict | None = None,
) -> go.Figure:
    """Generate a bar chart with hourly time distribution."""
    if fig_attr is None:
        fig_attr = {}

    fil_df = df.copy()
    fil_df["Hour"] = fil_df["Date"].dt.hour

    fil_df = fil_df.groupby(group_by).apply(function)
    fil_df = fil_df.to_frame(name=col_name).reset_index()
    fil_df["Hour_Hover"] = fil_df["Hour"].apply(hour_format)

    fil_df = fil_df.sort_values(by="Hour", ascending=False)
    return px.bar(
        fil_df,
        x=group_by[0],
        y=col_name,
        title=title,
        hover_name="Hour_Hover",
        **fig_attr,
    )


def call_time_fig(df: pd.DataFrame, name: str = "My") -> go.Figure:
    """Generate a call-schedule chart showing hourly Incoming vs Outgoing frequency."""
    fil_df = multiple_field_filter(df, {"Status": "Answered"})

    group_by = ["Hour", "Direction"]
    col_name = "Frequency"
    title = f"{name} Call Schedule"
    fig_attr = {"color": "Direction", "barmode": "group"}

    return time_fig_generate(
        fil_df, group_by, frequency_count, col_name, title, fig_attr
    )


def person_wise_stats(
    df: pd.DataFrame, name: str
) -> tuple[go.Figure, go.Figure]:
    """Generate two charts for a specific contact: overall stats and call schedule."""
    index_dict = {
        "call_time": {
            "Incoming": "Incoming CallTime (Minute)",
            "Outgoing": "Outgoing CallTime (Minute)",
        },
        "avg_call_time": {
            "Incoming": "Incoming Avg CallTime (Seconds)",
            "Outgoing": "Outgoing Avg CallTime (Seconds)",
        },
    }
    field_rename = {
        "Unanswered": f"Rejected by {name}",
        "Call Rejected": "Rejected by Me",
    }

    person_df = df[df["Name"] == name]

    direction_df = individual_count(person_df, "Direction")
    status_df = individual_count(person_df, "Status")
    call_time = individual_group(
        person_df, cal_total_min, index_dict["call_time"]
    )
    avg_call_time = individual_group(
        person_df, average_total_sec, index_dict["avg_call_time"]
    )

    temp_df = pd.concat(
        [direction_df, status_df, call_time, avg_call_time]
    ).rename(index=field_rename)

    fig1 = px.bar(
        temp_df,
        x=temp_df.index,
        y="Frequency",
        title=f"{name} Call Stats",
        color=temp_df.index,
    )
    fig2 = call_time_fig(person_df, name)

    return fig1, fig2
