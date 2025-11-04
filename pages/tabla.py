import os

import dash
import pandas as pd
from dash import dash_table, dcc, html

dash.register_page(__name__, path='/tabla', name="Tabla 📈", order=7)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

nofetal = pd.read_csv(os.path.join(DATA_DIR, "NoFetal.csv"))
codigos = pd.read_csv(os.path.join(DATA_DIR, "CodigosDeMuerte.csv"))
# 🔹 Verificar columnas requeridas
required_nofetal = ["AÑO", "COD_MUERTE"]
required_codigos = ["COD_MUERTE", "NOMBRE"]

for c in required_nofetal:
    if c not in nofetal.columns:
        raise ValueError(f"Falta la columna {c} en NoFetal")

for c in required_codigos:
    if c not in codigos.columns:
        raise ValueError(f"Falta la columna {c} en CodigosDeMuerte")

# 🔹 Filtrar año 2019
nofetal_2019 = nofetal[nofetal["AÑO"] == 2019]

# 🔹 Agrupar por código de causa de muerte
causas = (
    nofetal_2019.groupby("COD_MUERTE")
    .size()
    .reset_index(name="Total_Casos")
)

# 🔹 Unir con nombres desde CodigosDeMuerte
causas = causas.merge(codigos, on="COD_MUERTE", how="left")
# 🔹 Ordenar de mayor a menor y tomar las 10 principales
top10_causas = causas.sort_values("Total_Casos", ascending=False).head(10)
# 🔹 Reordenar columnas
top10_causas = top10_causas[["COD_MUERTE", "NOMBRE", "Total_Casos"]]

def table_graph():
  tabla = dash_table.DataTable(
      columns=[
        {"name": "Código de Muerte", "id": "COD_MUERTE"},
        {"name": "Causa de Muerte", "id": "NOMBRE"},
        {"name": "Total de Casos", "id": "Total_Casos"},
      ],
      data=top10_causas.to_dict("records"),
      sort_action="native",
      filter_action="native",
      page_size=10,
      style_cell={'textAlign': 'left', 'padding': '8px', 'fontFamily': 'Arial'},
      style_header={'backgroundColor': '#007BFF', 'color': 'white', 'fontWeight': 'bold'},
      style_table={'width': '80%', 'margin': 'auto', 'marginTop': '30px'},
      style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': '#f9f9f9'
        }
      ],
  )
  return tabla

layout = html.Div(children=[
    html.Br(),
    html.H2("Tabla - 10 principales causas de muerte en Colombia (2019)", className="fw-bold text-center"),
    table_graph(),
], className="p-4 m-2", style={"background-color": "#e3f2fd", "height": "auto", })
