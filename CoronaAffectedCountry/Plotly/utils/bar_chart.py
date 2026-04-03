import pandas as pd

DATASET_COLORS = {
    'Recovered': 'limegreen',
    'Confirmed': 'darkorange',
    'Death': 'crimson',
}


def _last_nonzero_index(row):
    """Return the index of the last non-zero value in a row, or the final index."""
    index = row[row != 0].last_valid_index()
    if index is None:
        return row.index[-1]
    return index


def get_color(df_type):
    """Return the chart color associated with a dataset type."""
    return DATASET_COLORS.get(df_type)


def format_df(df):
    """Collapse each row to its latest value, handling Recovered data specially.

    For 'Recovered' rows, uses the last non-zero value (since reporting
    may have stopped). For other rows, uses the most recent column.
    """
    data = {}
    for index, row in df.iterrows():
        dataset_type = index[0]
        if dataset_type == 'Recovered':
            col_idx = _last_nonzero_index(row)
        else:
            col_idx = -1
        data[index] = [row[col_idx]]

    result = pd.DataFrame(data).T
    result.columns = ['Value']
    return result
