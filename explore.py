import pages.space
from dash import Dash, html, dcc, Input, Output, callback
import pandas as pd
import dash
import dash_bootstrap_components as dbc
import plotly.express as px
import parse_csv



space_ls, file_df = parse_csv.main()

dash.register_page(__name__, path = "/explore", title = "Explore")

layout = dbc.Container([
    dcc.Dropdown(id = "select-study-space", options=file_df['space_name'].unique(), value='space_1'),
    html.Div(id = "space-info")
])

@callback(Output("space-info", "graph"), Input("select-study-space", "value"))
def display(selected_space):
    # filtered_data = file_df[file_df['space_name'] == selected_space]
    # Getting the space object from selected name
    # space_ls = parse_csv.main()[0]
    i = 0
    for space in space_ls:
        # print(space.visitor_dist)
        if space.space_name == selected_space:
            break
        i += 1
    # print(obj.space_name)
    output = html.Div([px.histogram(space_ls[i].visitor_dist, x = "time", y = "visitors", )])
    # fig = px.histogram(space_ls[i].visitor_dist, title=f'Number of visitors per hour in {selected_space}')
    return fig