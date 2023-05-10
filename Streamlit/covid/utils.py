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
    def get_row_index(x):
        return x[(x != 0).last_valid_index()]
    data = []
    for d_type, t_df in df.groupby('Dataset'):
        for country, tt_df in t_df.groupby('Country'):
            data.append([d_type, country, tt_df.apply(
                get_row_index, axis=1).iloc[0]])

    columns = ['Dataset', 'Country', 'Value']
    f_df = pd.DataFrame(data, columns=columns).sort_values(
        by='Value', ascending=False)

    return f_df


def get_color(df_types):
    color = {'Recovered': 'limegreen',
             'Confirmed': 'darkorange', 'Death': 'crimson'}
    return color.get(df_types)
