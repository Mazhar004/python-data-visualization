"""Data preprocessing utilities for call log DataFrames."""

from datetime import timedelta

import pandas as pd


def time_conv(time_val: str) -> timedelta:
    """Convert a 'MM:SS' string to a timedelta. Returns zero for NaN values."""
    if pd.isna(time_val):
        minutes, seconds = 0, 0
    else:
        minutes, seconds = map(int, time_val.split(":"))
    return timedelta(minutes=minutes, seconds=seconds)


def df_formatting(df: pd.DataFrame) -> pd.DataFrame:
    """Parse date strings and convert duration strings in the DataFrame."""
    date_format = "%m/%d/%Y (%I:%M:%S %p)"
    df["Date"] = pd.to_datetime(df["Date"], format=date_format)
    df["Duration"] = df["Duration"].apply(time_conv)
    return df


def single_field_filter(df: pd.DataFrame, key: str, value: str) -> pd.DataFrame:
    """Filter a DataFrame on a single field.

    For the 'Contact' key, 'Saved' keeps rows where Name differs from Address
    (i.e., contacts that have a saved name), and any other value keeps the inverse.
    For all other keys, rows are kept where df[key] == value.
    """
    if key == "Contact":
        is_unsaved = df["Name"] == df["Address"].astype(str)
        if value == "Saved":
            return df[~is_unsaved]
        return df[is_unsaved]

    return df[df[key] == value]


def multiple_field_filter(
    df: pd.DataFrame, field_dict: dict[str, str]
) -> pd.DataFrame:
    """Apply multiple sequential filters to a DataFrame.

    Supported filter keys:
        Direction -- 'Incoming' or 'Outgoing'
        Status    -- 'Answered', 'Unanswered', 'Missed', or 'Call Rejected'
        Contact   -- 'Saved' or 'Unsaved'
    """
    fil_df = df.copy()
    for key, value in field_dict.items():
        fil_df = single_field_filter(fil_df, key, value)
    return fil_df
