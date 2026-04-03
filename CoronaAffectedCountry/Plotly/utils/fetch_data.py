from datetime import datetime
from pathlib import Path

import pandas as pd


def parse_date(date_str):
    """Parse a date string, trying MM/DD/YY format first, then YYYY-MM-DD."""
    try:
        return datetime.strptime(date_str, '%m/%d/%y')
    except ValueError:
        return datetime.strptime(date_str, '%Y-%m-%d')


def convert_columns_to_dates(df):
    """Convert DataFrame column names from date strings to datetime objects."""
    df.columns = [parse_date(col) for col in df.columns]
    return df


def df_get_format(url_dict):
    """Fetch CSVs from URLs, aggregate by country, and combine into a single DataFrame."""
    drop_cols = ['Province/State', 'Lat', 'Long']
    group_col = 'Country/Region'

    df_list = []
    for url in url_dict.values():
        t_df = pd.read_csv(url)
        t_df = t_df.drop(drop_cols, axis=1)
        t_df = t_df.groupby(group_col, as_index=True).apply(lambda x: x.sum())
        t_df = t_df.drop(group_col, axis=1)
        t_df = convert_columns_to_dates(t_df)
        df_list.append(t_df)

    return pd.concat(
        df_list,
        keys=url_dict.keys(),
        names=['Dataset', 'Country'],
    )


def get_data(online=True):
    """Fetch COVID-19 data either from remote CSVs or a local cache."""
    url_dict = {
        'Confirmed': (
            'https://data.humdata.org/hxlproxy/api/data-preview.csv'
            '?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19'
            '%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series'
            '%2Ftime_series_covid19_confirmed_global.csv'
            '&filename=time_series_covid19_confirmed_global.csv'
        ),
        'Recovered': (
            'https://data.humdata.org/hxlproxy/api/data-preview.csv'
            '?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19'
            '%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series'
            '%2Ftime_series_covid19_recovered_global.csv'
            '&filename=time_series_covid19_recovered_global.csv'
        ),
        'Death': (
            'https://data.humdata.org/hxlproxy/api/data-preview.csv'
            '?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19'
            '%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series'
            '%2Ftime_series_covid19_deaths_global.csv'
            '&filename=time_series_covid19_deaths_global.csv'
        ),
    }

    data_dir = Path('data')
    data_dir.mkdir(exist_ok=True)
    filepath = data_dir / 'full_stats.csv'

    if online:
        print('Fetching data online')
        df = df_get_format(url_dict)
        df.to_csv(filepath)
    else:
        try:
            print('Fetching data locally')
            df = pd.read_csv(filepath)
            df = df.set_index(['Dataset', 'Country'])
            df = convert_columns_to_dates(df)
        except FileNotFoundError:
            print('Data not available locally, fetching online.\nPlease wait...')
            df = df_get_format(url_dict)
            df.to_csv(filepath)

    return df
