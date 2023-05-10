import datetime
import pandas as pd


def country_filter(df, countries):
    temp_df = df[df['Country'].isin(countries)]
    return temp_df


def dtype_filter(df, d_types):
    temp_df = df[df['Dataset'].isin(d_types)]
    return temp_df


def date_filter(df, start_date, end_date):
    start_date = datetime.datetime.combine(
        start_date, datetime.datetime.min.time())
    end_date = datetime.datetime.combine(
        end_date, datetime.datetime.min.time())

    temp_df = df.copy()
    start_loc = temp_df.columns.get_loc(start_date)
    temp_df = temp_df.iloc[:, :2].join(temp_df.iloc[:, start_loc:])

    end_loc = temp_df.columns.get_loc(end_date)
    temp_df = temp_df.iloc[:, :end_loc]

    return temp_df


def build_bar_data(df):
    transform_df = df.mask(df == 0).ffill(axis=1)
    data = []
    for _, row in transform_df.iterrows():
        val = row.iloc[-1]
        try:
            val = float(val)
        except:
            val = 0
        data.append([row.Dataset, row.Country, val])

    columns = ['Dataset', 'Country', 'Value']
    f_df = pd.DataFrame(data, columns=columns).sort_values(by='Value',
                                                           ascending=False)

    return f_df


def get_color(df_types):
    color = {'Recovered': 'limegreen',
             'Confirmed': 'darkorange', 'Death': 'crimson'}
    return color.get(df_types)
