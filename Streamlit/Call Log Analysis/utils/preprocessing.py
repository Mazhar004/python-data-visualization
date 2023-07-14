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


def single_field_filter(df, key, value):
    if key == 'Contact':
        bool_list = df['Name'] == df['Address'].astype(str)
        if value == 'Saved':
            df = df[~bool_list]
        else:
            df = df[bool_list]

    else:
        df = df[df[key] == value]
    return df


def multiple_field_filter(df, field_dict):
    '''
    # Direction [Incoming or Outgoing]
    # Status [Answered or Unanswered or Missed or 'Call Rejected']
    # Contact [Saved or Unsaved]
    '''
    fil_df = df.copy()
    for key, value in field_dict.items():
        fil_df = single_field_filter(fil_df, key, value)
    return fil_df
