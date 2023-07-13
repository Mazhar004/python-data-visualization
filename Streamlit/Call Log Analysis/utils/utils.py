def cal_total_min(df):
    total_min = df.Duration.sum().total_seconds() // 60
    return total_min


def average_total_sec(df):
    avg_sec = df.Duration.mean().total_seconds()
    return int(avg_sec)


def frequency_count(df):
    count_val = df.Duration.count()
    return count_val
