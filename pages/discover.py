from cgitb import html
import parse_csv
import space
from dash import Dash, html, dcc, Input, Output, callback
import dash
import dash_bootstrap_components as dbc
import plotly.express as px
from parse_csv import file_df, space_ls

class Selection:
    building = "ABS"
    floor = "1"

project_title = "Spot?"

dash.register_page(__name__, path = "/discover", title = "Discover")

layout = html.Div(children = [
        dbc.Container([
            html.Div(children=[
                dcc.Dropdown(id = "select-study-space", options=file_df['space_name'].unique(), value='space_1'),
                dcc.Graph(id='test-graph')
            ])
        ])
])


# @callback(
#     Output(component_id='test-graph', component_property='figure'),
#     Input(component_id="select-study-space", component_property='value')
# )

# def update_graph(selected_space):
#     filtered_data = file_df[file_df['space_name'] == selected_space]
#     # Getting the space object from selected name
#     for space in space_ls:
#         if space.space_name == selected_space:
#             obj = space

#     my_fig = px.histogram(obj.visitor_dist,
#                             x = "time", y = "visitors",
#                             title=f'Number of visitors per hour in {selected_space}')
#     return my_fig