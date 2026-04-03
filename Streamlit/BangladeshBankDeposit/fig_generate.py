import plotly.graph_objects as go


def line_fig_gen(df, bank_name_col, date_col, title, bank_wise_flag):
    """Generate a line chart figure from bank deposit data."""
    fig = go.Figure()

    for bank_name, group_df in df.groupby(bank_name_col):
        # Skip first 2 columns (Bank Name, Date)
        for y_col in group_df.columns[2:]:
            name = bank_name if bank_wise_flag else y_col[-1]
            hover_text = [f"{val}%" for val in group_df[y_col]]

            fig.add_trace(
                go.Scatter(
                    x=group_df[date_col],
                    y=group_df[y_col],
                    mode="lines",
                    name=name,
                    hovertext=hover_text,
                    hoverinfo="x+text",
                )
            )

    fig.update_layout(
        title=title,
        xaxis={"title": "Date"},
        yaxis={"title": "Interest rate(%)"},
    )

    return fig
