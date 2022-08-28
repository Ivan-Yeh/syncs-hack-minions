from contextlib import nullcontext
from enum import unique
import pages.space
from dash import Dash, html, dcc, Input, Output, callback
import dash
import dash_bootstrap_components as dbc
import plotly.express as px

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
    # discover.Selection.building = "ABS"
    return None

# locate 
@callback(Output("locate", "children"), [Input("ABS", "n_clicks"), Input("SIT", "n_clicks")])
def ABSDiscover(ABS, SIT):
    ctx = dash.callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    
    if input_id == "ABS":
        map = html.Div([
                html.Img(src="assets/ABS_Map.png", style={'height':'100%', 'width':'100%'})
            ])
    else:
        map = html.Div([
            html.Img(src="assets/SIT_Map.png", style={'height':'100%', 'width':'100%'})
        ])
    if ABS or SIT:
        return map
    return map