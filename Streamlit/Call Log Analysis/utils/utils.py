def cal_total_min(df):
    total_min = df.Duration.sum().total_seconds() // 60
    return total_min


def average_total_sec(df):
    avg_sec = df.Duration.mean().total_seconds()
    return int(avg_sec)


def frequency_count(df):
    count_val = df.Duration.count()
    return count_val


def hour_format(x):
    flag = 'AM'

    if x == 0:
        return f'12 {flag}'

    if x > 11:
        flag = 'PM'

    if x > 12:
        x = x % 12

    return f'{x} {flag}'


def individual_count(person_df, field, col_name='Frequency'):
    temp_df = person_df[field].value_counts().to_frame(name=col_name)
    temp_df.index.name = 'Field'
    return temp_df


