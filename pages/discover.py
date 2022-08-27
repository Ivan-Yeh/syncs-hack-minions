from subprocess import call
import pages.space
from dash import Dash, html, dcc, Input, Output, callback, ctx
import dash
import dash_bootstrap_components as dbc
import plotly.express as px
from parse_csv import file_df, space_ls

class Selection:
    building = "ABS"
    floor = "1"
    card = "1"

project_title = "Alcove"

dash.register_page(__name__, path = "/discover", title = "Discover")

layout = html.Div(children = [
        dbc.Container([
            html.Div(children=[
                dcc.Dropdown(id = "select-study-space", options=file_df['space_name'].unique(), value='space_1'),
                dcc.Graph(id='test-graph')
            ])
        ])
])

@callback(
    Output(component_id='test-graph', component_property='figure'),
    Input(component_id="select-study-space", component_property='value')
)

def update_graph(selected_space):
    filtered_data = file_df[file_df['space_name'] == selected_space]
    # Getting the space object from selected name
    for space in space_ls:
        if space.space_name == selected_space:
            obj = space

    my_fig = px.histogram(obj.visitor_dist,
                            x = "time", y = "visitors",
                            title=f'Number of visitors per hour in {selected_space}')
    return my_fig

# cards = []
# buttonIDList = []
# for space in space_ls:
#     if space.floor == Selection.floor:
#         card = dbc.Card(
#             [
#                 dbc.CardBody(
#                     [
#                         html.H4(space.space_name, className="card-title"),
#                         html.P(
#                             f"Some example text for {space.space_name}.",
#                             className="card-text",
#                         ),
#                         dbc.Button("Details", color="primary", id="button-"+space.space_name[-1:]),
#                     ]
#                 ),
#             ],
#             style={"width": "18rem", "padding": "2rem 1rem"},
#         )
#         buttonIDList.append("button-"+space.space_name[-1:])
#         cards.append(card)

# layout = html.Div(children=[
#         dbc.Container([
#             html.Div(
#                 [
#                     dbc.Row(
#                         [
#                         dbc.Col(html.Div(cards)),
#                         dbc.Col(html.Div(html.Img(src="assets/1.png"), id="col_2_1")),
#                         dbc.Col(id="none"),
#                         dbc.Col(html.Div("column three")),
#                         ]
#                     ),
#                 ])
#         ])
# ])


# @callback(
#     Output(component_id='col_2', component_property='children'),
#     Input("button-1", "n_clicks"),
#     Input("button-2", "n_clicks")
# )
# def changeMap(n_clicks):
#     if n_clicks:
#         # for space in space_ls:
#         if :
#             return html.Img(src="assets/1.png")
#         elif "button-2" == ctx.triggered_id:
#             return html.Img(src="assets/2.png")

# isCalled = False
# for buttonID in buttonIDList:
#     # Button callback on cards
#     @callback(
#         Output(component_id='col_2', component_property='children'),
#         Input(buttonID, 'n_clicks')
#     )
#     def changeMap(n_clicks):
#         isCalled = True
#         if n_clicks:
#             for space in space_ls:
#                 num = space.space_name[-1:]
#                 if "button-"+num == ctx.triggered_id:
#                     return html.Img(src="assets/"+num+".png")
#             if buttonIDList[-1] == buttonID:
#                 return html.Img(src="assets/1.png")
#     if isCalled:
#         break

