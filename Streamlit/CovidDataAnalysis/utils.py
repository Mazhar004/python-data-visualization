import pandas as pd


def date_filter(df, st_index, lt_index):
    return df.iloc[:, st_index:lt_index+1]


def build_bar_data(df, d_types):
    transform_df = df.mask(df == 0).ffill(axis=1)
    data = []
    for country, row in transform_df.iterrows():
        val = row.iloc[-1]
        try:
            val = float(val)
        except:
            val = 0
        data.append([country, val])

    columns = ['Country', 'Value']
    f_df = pd.DataFrame(data, columns=columns).sort_values(by='Value',
                                                           ascending=False)
    f_df['Dataset'] = d_types

    return f_df


def get_color(df_types):
    color = {'Recovered': 'limegreen',
             'Confirmed': 'darkorange', 'Death': 'crimson'}
    return color.get(df_types)
