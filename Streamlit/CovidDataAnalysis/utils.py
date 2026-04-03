import pandas as pd

COLOR_MAP = {
    "Recovered": "limegreen",
    "Confirmed": "darkorange",
    "Death": "crimson",
}


def date_filter(df, st_index, lt_index):
    return df.iloc[:, st_index:lt_index + 1]


def build_bar_data(df, d_types):
    transform_df = df.mask(df == 0).ffill(axis=1)

    last_values = pd.to_numeric(transform_df.iloc[:, -1], errors="coerce").fillna(0)

    f_df = pd.DataFrame({
        "Country": transform_df.index,
        "Value": last_values.values,
        "Dataset": d_types,
    }).sort_values(by="Value", ascending=False)

    return f_df


def get_color(df_types):
    return COLOR_MAP.get(df_types)
