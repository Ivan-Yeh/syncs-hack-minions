from contextlib import nullcontext
from enum import unique
import pages.space
from dash import Dash, html, dcc, Input, Output, callback
import dash
import dash_bootstrap_components as dbc
import plotly.express as px
from parse_csv import file_df, space_ls
import pages.discover as discover

project_title = "Alcove"

dash.register_page(__name__, path = "/", title = project_title)

building_name_dict = {"ABS": "University of Sydney Business School", "SIT": "School of Computer Science"}

name = "ABS"

layout = dbc.Container(children = [
    html.Div([html.Br()]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H3(building_name_dict["ABS"]),
                    html.Div(dbc.Button("Locate", id = "ABS")),
                    html.Br(),
                    html.Div(dbc.Button("Discover", id = "ABS-discover", href = "/discover")),
                ]),
            ]),
            dbc.Card([
                dbc.CardBody([
                    html.H3(building_name_dict["SIT"]),
                    html.Div(dbc.Button("Locate", id = "SIT")),
                    html.Br(),
                    html.Div(dbc.Button("Discover", id = "SIT-discover"))
                ]),
             ])
        ]),
        dbc.Col([html.Div(id = "maps"), html.Div(id = "locate")], style = {"right-margin": "auto", "left-margin": "auto"})
    ])
])

# discover ABS
@callback(Output("maps", "children"), Input("ABS-discover", "n_clicks"))
def ABSDiscover(n_clicks):
    discover.Selection.building = "ABS"
    return None

# locate ABS
@callback(Output("locate", "children"), Input("ABS", "n_clicks"))
def ABSDiscover(n_clicks):
    map = html.Div([
            html.Img(src="assets/ABS_Map.png", style={'height':'100%', 'width':'100%'})
        ])
    if n_clicks:
        return map
    return map