from datetime import timedelta
import pandas as pd


def time_conv(time_val):
    if pd.isna(time_val):
        m, s = 0, 0
    else:
        m, s = map(int, time_val.split(':'))
    return timedelta(minutes=m, seconds=s)
