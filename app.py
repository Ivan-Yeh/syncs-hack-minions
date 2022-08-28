import pages.space
from dash import Dash, html, dcc, Input, Output, page_container
import dash_bootstrap_components as dbc
import plotly.express as px
import webbrowser

project_title = "Alcove"

app = Dash(__name__, use_pages = True, title = project_title, suppress_callback_exceptions = True)

navbar = dbc.NavbarSimple(children = [
    dbc.NavItem(dbc.NavLink("Home", href = "/")),
    dbc.NavItem(dbc.NavLink("Explore", href = "/discover")),
    ],
    brand = project_title,
    brand_href = "/"
)


app.layout = html.Div(children = [
    dcc.Loading([navbar, page_container, html.Br()], fullscreen = True),
])

if __name__ == '__main__':
    webbrowser.open_new_tab("http://127.0.0.1:8050/")
    app.run_server(debug = True)