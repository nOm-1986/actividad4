import dash
from dash import Dash, dcc, html

external_css = ["https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css", ]

app = Dash(__name__, pages_folder='../pages', use_pages=True, external_stylesheets=external_css)

brand_link = dcc.Link(["Aplicaciones I"], href="#", className="navbar-brand")
pages_links = [dcc.Link(page['name'], href=page["relative_path"], className="nav-link") for page in dash.page_registry.values()]

app.layout = html.Div([
	### Navbar
    html.Nav(children=[ html.Div([ html.Div([brand_link, ] + pages_links, className="navbar-nav")], className="container-fluid"),], className="navbar navbar-expand-lg bg-dark", **{"data-bs-theme": "dark"}),
  #### Main Page
    html.Div([html.Br(),html.P('Actividad 4', className="text-dark text-center fw-bold fs-1"),dash.page_container
	], className="col-6 mx-auto")
], style={"min-height":"100vh", "height": "auto", "background-color": "#e3f2fd"})

if __name__ == '__main__':
	app.run(debug=False)
