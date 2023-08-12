from datetime import datetime
import os
import pandas as pd
import requests as rq


MONTHS = {1: "January", 2: "February", 3: "March", 4: "April",
          5: "May", 6: "June", 7: "July", 8: "August",
          9: "September", 10: "October", 11: "November", 12: "December"}

URL = "https://www.bb.org.bd/en/index.php/financialactivity/interestdeposit"


def df_format(dfs, date_val):
    df = dfs[0]
    df = df.drop([0, 1], axis=0).reset_index(drop=True)
    date_row = len(df)*[date_val]
    df.insert(1, "Date", date_row)
    return df


def get_data(month, year, bank_deposit_rate_submit="Search"):
    data = {"select_month": MONTHS[month],
            "select_year": year,
            "bank_deposit_rate_submit": bank_deposit_rate_submit}

    res = rq.post(URL, data=data)
    return res


def get_all_data():
    current_year = datetime.now().year

    all_df = []
    for year in range(2013, current_year+1):
        for month in MONTHS:
            date_val = datetime(year, month, 1)
            res = get_data(month, year)

            dfs = pd.read_html(res.text)
            if len(dfs[0]) == 0:
                print(f"Data not available for {date_val}")
                break
            df = df_format(dfs, date_val)
            all_df.append(df)
    return all_df


def conv(cell):
    # Convert string into float
    # 12 -> 12.0
    # if 23-25 -> (23+25)/2
    try:
        val = float(cell)
    except ValueError:
        try:
            a, b = map(float, cell.split("-"))
            val = (a+b)/2
        except:
            val = 0
    return val


def plot_process(df, columns):
    processed_df = df.copy()
    for col in columns:
        processed_df[col] = processed_df[col].apply(conv)
    return processed_df


def data_process_plot(main_df):
    apply_column = main_df.columns[2:]
    processed_df = plot_process(main_df, apply_column)
    return processed_df


def data_store(main_df, processed_df):
    os.makedirs("data", exist_ok=True)

    current_data = datetime.now().strftime("%d %b %Y")
    main_df.to_csv(f"data/Original_{current_data}.csv", index=False)
    processed_df.to_csv(f"data/Processed_{current_data}.csv", index=False)


def main():
    all_df = get_all_data()
    main_df = pd.concat(all_df).reset_index(drop=True)
    processed_df = data_process_plot(main_df)
    data_store(main_df, processed_df)


if __name__ == "__main__":
    main()
