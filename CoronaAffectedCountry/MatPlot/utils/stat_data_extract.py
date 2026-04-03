from datetime import datetime
from pathlib import Path

import pandas as pd

from utils.graph_data_extract import graph_data_extract

DATA_DIR = Path("data")
STAT_CSV = DATA_DIR / "Stat_updated.csv"
CASE_COLUMNS = ["TotalCases", "TotalRecovered", "TotalDeaths", "ActiveCases"]


class CovidStatExtract:
    def __init__(self, threshold, online=False):
        DATA_DIR.mkdir(exist_ok=True)
        try:
            self.df = self._all_cases_form(graph_data_extract(online=online))
            self._build_stat_columns()
            self.df.to_csv(STAT_CSV, index=True)
        except Exception:
            self.df = pd.read_csv(STAT_CSV, index_col="Country/Region")
            for col in self.df.columns[:-1]:
                self.df[col] = pd.to_numeric(self.df[col])

        if threshold:
            self.df = self.df[self.df.total_case > threshold]

    @staticmethod
    def _all_cases_form(data_list):
        index = data_list[0].index
        new_df = pd.DataFrame([], index=index, columns=CASE_COLUMNS)

        for k, series_df in enumerate(data_list):
            last_col = pd.DataFrame(series_df[series_df.columns[-1]])
            last_col.columns = [CASE_COLUMNS[k]]
            new_df.iloc[:, k] = last_col

        # ActiveCases = TotalCases - TotalRecovered - TotalDeaths
        new_df.iloc[:, k + 1] = (
            new_df.iloc[:, 0] - new_df.iloc[:, 1] - new_df.iloc[:, 2]
        )
        return new_df

    def _build_stat_columns(self):
        total_cases = self.df.TotalCases

        data = {
            "total_case": total_cases,
            # Actual counts
            "ac_recover": self.df.TotalRecovered,
            "ac_active": self.df.ActiveCases,
            "ac_death": self.df.TotalDeaths,
            # Country-wise percentages
            "c_recover": self.df.TotalRecovered / total_cases,
            "c_active": self.df.ActiveCases / total_cases,
            "c_death": self.df.TotalDeaths / total_cases,
            # Worldwide percentages
            "w_recover": self.df.TotalRecovered / self.df.TotalRecovered.sum(),
            "w_active": self.df.ActiveCases / self.df.ActiveCases.sum(),
            "w_death": self.df.TotalDeaths / self.df.TotalDeaths.sum(),
        }

        self.df = pd.concat(list(data.values()), axis=1)
        self.df.columns = list(data.keys())

        date_col = pd.DataFrame(
            [[datetime.now().strftime("%d %b,%Y")]] * self.df.shape[0],
            index=self.df.index.values,
            columns=["Date"],
        )
        self.df = pd.concat([self.df, date_col], axis=1)


def stat_data_extract(threshold, online=False):
    return CovidStatExtract(threshold, online).df
