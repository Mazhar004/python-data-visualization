import plotly.graph_objs as go

from utils import get_color


def covid_analyze_lines(fill_df):
    columns = fill_df.columns
    s_date = columns[0].strftime("%d %b, %y")
    e_date = columns[-1].strftime("%d %b, %y")

    traces = [
        go.Scatter(
            x=t_df.columns,
            y=t_df.values[0],
            mode="lines",
            name=f"{dataset}, {country}",
        )
        for (dataset, country), t_df in fill_df.groupby(["Dataset", "Country"])
    ]

    layout = go.Layout(
        title=f'COVID Status from "{s_date}" to "{e_date}"',
        xaxis=dict(title="Date"),
        yaxis=dict(title="No. of People"),
    )

    return go.Figure(data=traces, layout=layout)


def covid_analyze_bars(df, df_types, s_date, e_date, top_k=10):
    s_date_str = s_date.strftime("%d %b, %y")
    e_date_str = e_date.strftime("%d %b, %y")

    filter_series = df.sort_values(by="Value", ascending=False)[:top_k]
    title = (
        f'Covid "{df_types}" Stats for Top {top_k} Countries '
        f'from "{s_date_str}" to "{e_date_str}"'
    )

    trace = go.Bar(
        x=filter_series.Country,
        y=filter_series.Value,
        marker=dict(color=get_color(df_types)),
    )

    layout = go.Layout(
        title=title,
        xaxis=dict(title="Countries"),
        yaxis=dict(title="No. of People"),
        barmode="stack",
    )

    return go.Figure(data=[trace], layout=layout)
