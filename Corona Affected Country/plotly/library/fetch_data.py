# Built In
import os
from datetime import datetime

# Data analysis
import pandas as pd


def date_conv(str_date):
    try:
        str_date = datetime.strptime(str_date, '%m/%d/%y')
    except Exception as _:
        str_date = datetime.strptime(str_date, '%Y-%m-%d')
    return str_date


def col_conv(df):
    col = map(date_conv, df.columns)
    df.columns = list(col)
    return df


def df_get_format(url_dict):
    drop_col = ['Province/State', 'Lat', 'Long']
    col = 'Country/Region'
    df_list = []
    for df_type, url in url_dict.items():
        t_df = pd.read_csv(url)

        t_df = t_df.drop(drop_col, axis=1)
        t_df = t_df.groupby(col, as_index=True).apply(lambda x: x.sum())
        t_df = t_df.drop([col], axis=1)

        t_df = col_conv(t_df)

        df_list.append(t_df)

    df = pd.concat(df_list,
                   keys=url_dict.keys(),
                   names=['Dataset', 'Country'])
    return df


def get_data(online=True):
    confirmed_url = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv'
    recovered_url = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_recovered_global.csv&filename=time_series_covid19_recovered_global.csv'
    death_url = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_deaths_global.csv&filename=time_series_covid19_deaths_global.csv'

    url_dict = {'Confirmed': confirmed_url,
                'Recovered': recovered_url,
                'Death': death_url,
                }

    os.makedirs('data', exist_ok=True)
    filename = 'data/full_stats.csv'

    if online:
        print('Online Data fetching')
        df = df_get_format(url_dict)
        df.to_csv(filename)
    else:
        try:
            print('Locally Data fetching')
            df = pd.read_csv(filename)
            df = df.set_index(['Dataset', 'Country'])
            df = col_conv(df)
        except Exception as _:
            print('Data not available locally, needed to fecth online.\nPlease wait..')
            df = df_get_format(url_dict)
            df.to_csv(filename)
    return df
