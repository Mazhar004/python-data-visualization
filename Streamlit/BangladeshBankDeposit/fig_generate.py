import plotly.graph_objects as go


def line_fig_gen(df, bank_name_col, date_col, title, bank_wise_flag):
    fig = go.Figure()

    count = -1
    for bank_name, temp_df in df.groupby(bank_name_col):
        # Ignore first 2 column [Bank Name, Date]
        for y_col in temp_df.columns[2:]:
            count += 1

            name = y_col[-1]
            if bank_wise_flag:
                name = bank_name

            fig.add_trace(go.Scatter(x=temp_df[date_col],
                                     y=temp_df[y_col],
                                     mode='lines',
                                     name=name))

            hover_text = [f"{val}%" for val in temp_df[y_col]]

            fig.data[count].update(hovertext=hover_text,
                                   hoverinfo='x+text')

    fig.update_layout(title=title,
                      xaxis=dict(title='Date'),
                      yaxis=dict(title="Interest rate(%)"))

    return fig
