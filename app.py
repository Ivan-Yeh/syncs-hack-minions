from cgitb import html
import parse_csv
import space
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
from parse_csv import file_df, space_ls

app = Dash()

dropdown = dcc.Dropdown(options=file_df['space_name'].unique(), value='space_1')

app.layout = html.Div(children=[
    html.H1(children='Study Space Dashboard'),
    dropdown,
    dcc.Graph(id='test-graph')
])

@app.callback(
    Output(component_id='test-graph', component_property='figure'),
    Input(component_id=dropdown, component_property='value')
)

def update_graph(selected_space):
    filtered_data = file_df[file_df['space_name'] == selected_space]
    # Getting the space object from selected name
    for space in space_ls:
        if space.space_name == selected_space:
            obj = space

    my_fig = px.histogram(space.visitor_dist,
                            x = "time", y = "visitors",
                            title=f'Number of visitors per hour in {selected_space}')
    return my_fig

if __name__ == '__main__':
    app.run_server(debug=True)