import pages.space
from dash import Dash, html, dcc, Input, Output, callback
import pandas as pd
import dash
import dash_bootstrap_components as dbc
import plotly.express as px
import parse_csv

space_ls, file_df = parse_csv.main()

dash.register_page(__name__, path = "/discover", title = "Discover")

layout = dbc.Container([
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.H3("Select a study space"),
            dcc.Dropdown(id = "select-study-space", options=file_df['space_name'].unique(), value='Space 1'),
            html.Hr(),
            html.Div(id = "additional-info")
            
            
            
            
        ]),
        dbc.Col([
            html.Div(id = "floor-map")
        ]),
        dbc.Col([
            html.Div(id = "space-info")
        ])
        
    ]),
    
])

@callback([Output("space-info", "children"), Output("floor-map", "children"), Output("additional-info", "children")], Input("select-study-space", "value"))
def display(selected_space):

    for space in space_ls:
        if space.space_name == selected_space:
            obj = space
            break
    
    output = html.Div(children =[
        dcc.Graph(figure = px.histogram(obj.visitor_dist, x = "time", y = "visitors", title=f'Number of visitors over time {selected_space}')),
        html.Hr(),
        dcc.Graph(figure = px.histogram(obj.noise_dist, x = "time", y = "noise_level", title=f'Noise level over time in {selected_space}')),
    ])
    floor_map = html.Div(children = [html.Img(src = "assets/lvl_" + obj.floor + ".png", style={'height':'100%', 'width':'100%'})])
    
    if obj.has_charger:
        charger_info = html.H5("Yes")
    else:
        charger_info = html.H5("No")
    
    if obj.has_comp:
        comp_info = html.H5("Yes")
    else:
        comp_info = html.H5("No")
        
    additional_info = html.Div(children = [
        html.H3("Additional Information"),
        html.H4("Opening Hours: " + obj.open_hr + " to " + obj.close_hr, style={"font-weight": "bold"}),
        html.Br(),
        html.H5("Charging Spots Available?", style={"font-weight": "bold"}),
        charger_info,
        html.H5("Computers Available?", style={"font-weight": "bold"}),
        comp_info
        
    ])
    return output, floor_map, additional_info