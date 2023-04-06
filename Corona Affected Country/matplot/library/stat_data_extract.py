# Relevant Library
import os
from datetime import datetime

# Numerical Data Process
import pandas as pd

# Custom Library
from library.graph_data_extract import graph_data_extract


class CovidStatExtract():
    def __init__(self, threshold):
        os.makedirs('CSV', exist_ok=True)
        try:
            self.df = self.all_cases_form(graph_data_extract())
            self.csv_form()
            self.df.to_csv('CSV/Stat_updated.csv', index=True)
        except:
            self.df = pd.read_csv('CSV/Stat_updated.csv',
                                  index_col='Country/Region')
            for i in self.df.columns[:-1]:
                self.df[i] = pd.to_numeric(self.df[i])
        if threshold:
            self.df = self.df[self.df.total_case > threshold]

    def all_cases_form(self, data_list):
        index = data_list[0].index
        columns = ['TotalCases', 'TotalRecovered',
                   'TotalDeaths', 'ActiveCases', ]
        new_df = pd.DataFrame([], index=index, columns=columns)

        for k, i in enumerate(data_list):
            df = pd.DataFrame(i[i.columns[-1]])
            df.columns = [columns[k]]
            new_df.iloc[:, k] = df
        new_df.iloc[:, k+1] = new_df.iloc[:, 0] - \
            new_df.iloc[:, 1]-new_df.iloc[:, 2]
        return new_df

    def csv_form(self):
        data_dict = {}

        data_dict['total_case'] = self.df.TotalCases
        # Actual Data
        data_dict['ac_recover'] = self.df.TotalRecovered
        data_dict['ac_active'] = self.df.ActiveCases
        data_dict['ac_death'] = self.df.TotalDeaths

        # Country Wise Percentage
        data_dict['c_recover'] = data_dict['ac_recover']/self.df.TotalCases
        data_dict['c_active'] = data_dict['ac_active']/self.df.TotalCases
        data_dict['c_death'] = data_dict['ac_death']/self.df.TotalCases

        total_recover = sum(self.df.TotalRecovered)
        total_active = sum(self.df.ActiveCases)
        total_death = sum(self.df.TotalDeaths)

        # Worldwide wise percentage
        data_dict['w_recover'] = self.df.TotalRecovered/total_recover
        data_dict['w_active'] = self.df.ActiveCases/total_active
        data_dict['w_death'] = self.df.TotalDeaths/total_death

        self.df = pd.concat(list(data_dict.values()), axis=1)
        self.df.columns = list(data_dict.keys())

        date = pd.DataFrame(self.df.shape[0]*[[datetime.now().strftime(
            "%d %b,%Y")]], index=self.df.index.values, columns=['Date'])
        self.df = pd.concat([self.df, date], axis=1)


def stat_data_extract(threshold):
    data = CovidStatExtract(threshold)
    return data.df