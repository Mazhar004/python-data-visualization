import calendar
import os
from datetime import datetime

import pandas as pd
import requests

URL = "https://www.bb.org.bd/en/index.php/financialactivity/interestdeposit"


def df_format(dfs, date_val):
    """Format the scraped HTML table into a clean DataFrame with a date column."""
    df = dfs[0].drop([0, 1], axis=0).reset_index(drop=True)
    df.insert(1, "Date", [date_val] * len(df))
    return df


def get_data(month, year):
    """Fetch deposit rate data for a given month and year from Bangladesh Bank."""
    data = {
        "select_month": calendar.month_name[month],
        "select_year": year,
        "bank_deposit_rate_submit": "Search",
    }
    return requests.post(URL, data=data)


def get_all_data():
    """Scrape deposit rate data for all available months from 2013 to present."""
    current_year = datetime.now().year

    all_df = []
    for year in range(2013, current_year + 1):
        for month in range(1, 13):
            date_val = datetime(year, month, 1)
            res = get_data(month, year)

            dfs = pd.read_html(res.text)
            if len(dfs[0]) == 0:
                print(f"Data not available for {date_val}")
                break

            df = df_format(dfs, date_val)
            all_df.append(df)

    return all_df


def convert_cell(cell):
    """Convert a cell value to float.

    Handles plain numbers (e.g. "12" -> 12.0) and
    ranges (e.g. "23-25" -> 24.0, the average).
    Returns 0 for unparseable values.
    """
    try:
        return float(cell)
    except (ValueError, TypeError):
        try:
            a, b = map(float, cell.split("-"))
            return (a + b) / 2
        except (ValueError, TypeError, AttributeError):
            return 0


def process_columns(df, columns):
    """Apply numeric conversion to the specified columns."""
    processed_df = df.copy()
    for col in columns:
        processed_df[col] = processed_df[col].apply(convert_cell)
    return processed_df


def data_process(main_df):
    """Process all data columns (excluding bank name and date) to numeric."""
    return process_columns(main_df, main_df.columns[2:])


def data_store(main_df, processed_df):
    """Save original and processed DataFrames to CSV files."""
    os.makedirs("data", exist_ok=True)

    current_date = datetime.now().strftime("%d %b %Y")
    main_df.to_csv(f"data/Original_{current_date}.csv", index=False)
    processed_df.to_csv(f"data/Processed_{current_date}.csv", index=False)


def main():
    all_df = get_all_data()
    main_df = pd.concat(all_df).reset_index(drop=True)
    processed_df = data_process(main_df)
    data_store(main_df, processed_df)


if __name__ == "__main__":
    main()
