"""Utility functions for call log data aggregation and formatting."""

import pandas as pd


def cal_total_min(df: pd.DataFrame) -> float:
    """Calculate total call duration in minutes."""
    return df.Duration.sum().total_seconds() // 60


def average_total_sec(df: pd.DataFrame) -> int:
    """Calculate average call duration in seconds."""
    return int(df.Duration.mean().total_seconds())


def frequency_count(df: pd.DataFrame) -> int:
    """Count the number of call records."""
    return df.Duration.count()


def hour_format(hour: int) -> str:
    """Convert 24-hour integer to 12-hour AM/PM string."""
    if hour == 0:
        return "12 AM"
    period = "AM" if hour < 12 else "PM"
    display_hour = hour if hour <= 12 else hour - 12
    return f"{display_hour} {period}"


def individual_count(
    person_df: pd.DataFrame, field: str, col_name: str = "Frequency"
) -> pd.DataFrame:
    """Count occurrences of each unique value in a given field."""
    temp_df = person_df[field].value_counts().to_frame(name=col_name)
    temp_df.index.name = "Field"
    return temp_df


def individual_group(
    person_df: pd.DataFrame,
    func: callable,
    index: dict,
    col_name: str = "Frequency",
) -> pd.DataFrame:
    """Group by Direction, apply an aggregation function, and rename the index."""
    temp_df = person_df.groupby("Direction").apply(func).to_frame(col_name)
    temp_df = temp_df.rename(index=index)
    temp_df.index.name = "Field"
    return temp_df
