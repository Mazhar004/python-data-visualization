from datetime import timedelta
import pandas as pd


def time_conv(time_val):
    if pd.isna(time_val):
        m, s = 0, 0
    else:
        m, s = map(int, time_val.split(':'))
    return timedelta(minutes=m, seconds=s)


def df_formatting(df):
    fotmat = "%m/%d/%Y (%I:%M:%S %p)"
    df['Date'] = pd.to_datetime(df['Date'], format=fotmat)
    df['Duration'] = df['Duration'].apply(time_conv)
    return df


