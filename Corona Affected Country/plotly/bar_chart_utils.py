import pandas as pd


def get_index(row):
    index = row[row != 0].last_valid_index()
    if index is None:
        return row.index[-1]
    return index


def handle_recovered(df):
    col = max(df.columns)

    col_list = df.apply(get_index, axis=1).to_dict()
    filter_series = full_df.apply(lambda x: x[col_list[x.name]], axis=1)

    df = pd.DataFrame(filter_series, columns=[col])
    return df, col


def get_color(df_types):
    color = {'Recovered': 'limegreen',
             'Confirmed': 'darkorange', 'Death': 'crimson'}
    return color.get(df_types)


def format_df(df):
    data = {}
    for index, row in df.iterrows():
        if index[0] == 'Recovered':
            index_val = get_index(row)
        else:
            index_val = -1
        data[index] = [row[index_val]]
    df = pd.DataFrame(data).T
    df.columns = ['Value']
    return df
