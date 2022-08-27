from cgitb import html
import parse_csv
import space
from dash import Dash, html, dcc, Input, Output, callback
import dash
import dash_bootstrap_components as dbc
import plotly.express as px
from parse_csv import file_df, space_ls

project_title = "Spot?"

dash.register_page(__name__, path = "/", title = project_title)

layout = html.Div(children = [
        dbc.Container([
            html.Div(children=[
                dcc.Dropdown(id = "select-study-space", options=file_df['space_name'].unique(), value='space_1'),
                dcc.Graph(id='test-graph')
            ])
        ])
])