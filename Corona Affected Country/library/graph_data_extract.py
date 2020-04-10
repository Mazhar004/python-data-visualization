# Relevant Library
import os
from datetime import datetime as dt

# Numerical Data Process
import pandas as pd


def graph_data_extract():
    all_data = []
    for i in ['Confirmed', 'Recovered', 'Death']:
        if i == 'Recovered':
            url = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_recovered_global.csv&filename=time_series_covid19_recovered_global.csv'
        elif i == 'Death':
            url = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_deaths_global.csv&filename=time_series_covid19_deaths_global.csv'
        else:
            url = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv'
        os.makedirs('CSV', exist_ok=True)
        try:
            df = pd.read_csv(url)
            df = df.drop(['Lat', 'Long', 'Province/State'], axis=1)
            for j in df:
                try:
                    df[j] = pd.to_numeric(df[j])
                except:
                    pass
            df = df.groupby(by='Country/Region').sum()
            df.columns = [dt.strftime(dt.strptime(i, '%m/%d/%y'), '%d\n%b')
                          for i in df.columns]
            df.to_csv('CSV/'+i+'.csv', index=True)
        except:
            df = pd.read_csv('CSV/' + i + '.csv', index_col='Country/Region')
            for j in df:
                try:
                    df[j] = pd.to_numeric(df[j])
                except:
                    pass
        all_data.append(df)
    return all_data
