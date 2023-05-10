# Plot
import plotly.graph_objs as go

# Custom
from utils import get_color


def covid_analyze_lines(fill_df):
    s_date = fill_df.columns[2].strftime('%d %b, %y')
    e_date = fill_df.columns[-1].strftime('%d %b, %y')

    # Create a list of traces for each country
    traces = []
    for country, c_df in fill_df.groupby('Country'):
        for d_type, t_df in c_df.groupby('Dataset'):
            t_df = t_df.iloc[:, 2:]
            trace = go.Scatter(x=t_df.columns,
                               y=t_df.values[0],
                               mode='lines',
                               name=f'{d_type}, {country}')
            traces.append(trace)

    layout = go.Layout(title=f'COVID Status from "{s_date}" to "{e_date}"',
                       xaxis=dict(title='Date'),
                       yaxis=dict(title='No. of People'))

    # Create the figure and add the traces and layout
    fig = go.Figure(data=traces, layout=layout)
    return fig


def covid_analyze_bars(df, df_types, s_date, e_date, top_k=10):
    s_date = s_date.strftime('%d %b, %y')
    e_date = e_date.strftime('%d %b, %y')

    filter_series = df.sort_values(by='Value', ascending=False)[:top_k]
    title = f'Covid "{df_types}" Stats for Top {top_k} Countries from "{s_date}" to "{e_date}"'

    # Create a list of traces for each country
    trace = go.Bar(x=filter_series.Country,
                   y=filter_series.Value,
                   marker=dict(color=get_color(df_types)))

    # Create the layout for the plot
    layout = go.Layout(
        title=title,
        xaxis=dict(title='Countries'),
        yaxis=dict(title='No. of People'),
        barmode='stack'
    )

    # Create the figure and add the traces and layout
    fig = go.Figure(data=[trace], layout=layout)

    # Show the plot
    return fig