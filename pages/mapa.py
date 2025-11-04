import json
import os

import dash
import pandas as pd
import plotly.express as px
import requests
from dash import Dash, dcc, html

dash.register_page(__name__, path='/mapa', name="Mapa 🗺️", order=1)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # sube desde /pages
DATA_DIR = os.path.join(BASE_DIR, "data")

nofetal = pd.read_csv(os.path.join(DATA_DIR, "NoFetal.csv"))
divipola = pd.read_csv(os.path.join(DATA_DIR, "Divipola.csv"))

# print("✅ NoFetal:", nofetal.shape)
# print("✅ Divipola:", divipola.shape)
# print("Columnas NoFetal:", list(nofetal.columns))
# print("Columnas Divipola:", list(divipola.columns))


# ==============================
# Filtrar año 2019
# ==============================
nofetal_2019 = nofetal[nofetal["AÑO"] == 2019]
#print("Muertes 2019:", len(nofetal_2019))

muertes_por_depto = (
    nofetal_2019.groupby("COD_DEPARTAMENTO")
    .size()
    .reset_index(name="TOTAL_MUERTES")
)

# ==============================
# Unir con nombres de departamentos
# ==============================
df_merged = muertes_por_depto.merge(
    divipola[["COD_DEPARTAMENTO", "DEPARTAMENTO"]],
    on="COD_DEPARTAMENTO",
    how="left"
)

#print("Departamentos únicos en df_merged:", df_merged["DEPARTAMENTO"].unique()[:10])
df_merged["DEPARTAMENTO"] = df_merged["DEPARTAMENTO"].str.upper().str.strip()

# ==============================
# Leer GeoJSON
# ==============================
url_geojson = "https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json"
response = requests.get(url_geojson)
geojson = json.loads(response.text)

# ==============================
# Mapa
# ==============================

def create_map():
  fig = px.choropleth(
    df_merged,
    geojson=geojson,
    locations="DEPARTAMENTO",
    featureidkey="properties.NOMBRE_DPT",
    color="TOTAL_MUERTES",
    hover_name="DEPARTAMENTO",
    color_continuous_scale="Reds",
    title="Distribución total de muertes por departamento - 2019",
  )
  fig.update_geos(fitbounds="geojson", visible=False)
  fig.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
  return fig


# ==============================
# Dash app
# ==============================
# app = Dash(__name__)
# app.layout = html.Div([
#     html.H1("Distribución de Muertes No Fetales - Colombia 2019", style={'textAlign': 'center'}),
#     dcc.Graph(figure=fig)
# ])

# if __name__ == "__main__":
#     app.run(debug=True)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    html.H2("Mapa", className="fw-bold text-center"),
    dcc.Graph(id="Mapa", figure=create_map())
], className="p-4 m-2", style={"background-color": "#e3f2fd", "height": "auto", })
