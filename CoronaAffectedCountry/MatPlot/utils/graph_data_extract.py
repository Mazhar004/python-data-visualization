from pathlib import Path

import pandas as pd

BASE_URL = (
    "https://data.humdata.org/hxlproxy/api/data-preview.csv"
    "?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData"
    "%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data"
    "%2Fcsse_covid_19_time_series%2F"
)

DATA_URLS = {
    "Confirmed": f"{BASE_URL}time_series_covid19_confirmed_global.csv"
                 "&filename=time_series_covid19_confirmed_global.csv",
    "Recovered": f"{BASE_URL}time_series_covid19_recovered_global.csv"
                 "&filename=time_series_covid19_recovered_global.csv",
    "Death":     f"{BASE_URL}time_series_covid19_deaths_global.csv"
                 "&filename=time_series_covid19_deaths_global.csv",
}

DATA_DIR = Path("data")
CATEGORIES = ["Confirmed", "Recovered", "Death"]


def _coerce_numeric(df):
    """Convert all convertible columns to numeric types in place."""
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="ignore")
    return df


def graph_data_extract(online=False):
    DATA_DIR.mkdir(exist_ok=True)
    all_data = []

    for category in CATEGORIES:
        if online:
            df = pd.read_csv(DATA_URLS[category])
            df = df.drop(["Lat", "Long", "Province/State"], axis=1)
            df = _coerce_numeric(df)
            df = df.groupby(by="Country/Region").sum()
            df.to_csv(DATA_DIR / f"{category}.csv", index=True)
        else:
            df = pd.read_csv(
                DATA_DIR / f"{category}.csv", index_col="Country/Region"
            )
            df = _coerce_numeric(df)

        all_data.append(df)

    return all_data
