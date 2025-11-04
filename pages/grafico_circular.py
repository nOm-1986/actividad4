import os

import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html

dash.register_page(__name__, path='/grafico_circular', name="Grafico circular 📈", order=4)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

nofetal = pd.read_csv(os.path.join(DATA_DIR, "NoFetal.csv"))
divipola = pd.read_csv(os.path.join(DATA_DIR, "Divipola.csv"))

# Verificar columnas necesarias
required_nofetal = ["AÑO", "COD_DANE"]
required_divipola = ["COD_DANE", "MUNICIPIO", "DEPARTAMENTO"]

for c in required_nofetal:
  if c not in nofetal.columns:
      raise ValueError(f"Falta la columna {c} en NoFetal")

for c in required_divipola:
  if c not in divipola.columns:
    raise ValueError(f"Falta la columna {c} en Divipola")

nofetal_2019 = nofetal[nofetal["AÑO"] == 2019]

muertes_por_mun = (
  nofetal_2019.groupby("COD_DANE")
  .size()
  .reset_index(name="Total_Muertes")
)

# 🔹 Combinar con nombres de municipio y departamento
muertes_por_mun = muertes_por_mun.merge(divipola, on="COD_DANE", how="left")

# 🔹 Tomar las 10 ciudades con menor número de muertes
top10_menor = muertes_por_mun.nsmallest(10, "Total_Muertes")

def create_pie_graph():
  fig = px.pie(
      top10_menor,
      names="MUNICIPIO",
      values="Total_Muertes",
      color="DEPARTAMENTO",
      title="10 ciudades con menor índice de mortalidad en Colombia (2019)",
      hole=0.3,  # Para hacerlo tipo 'donut' (puedes quitarlo si prefieres círculo sólido)
  )

  # Personalización visual
  fig.update_traces(textposition="inside", textinfo="label+percent")
  fig.update_layout(
      title_x=0.5,
      template="plotly_white",
      font=dict(size=14),
  )

  return fig

layout = html.Div(children=[
    html.Br(),
    html.H2("Gráfico circular", className="fw-bold text-center"),
    dcc.Graph(id="grafico_circular", figure=create_pie_graph())
], className="p-4 m-2", style={"background-color": "#e3f2fd", "height": "auto", })
