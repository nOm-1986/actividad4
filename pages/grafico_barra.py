import os

import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html

dash.register_page(__name__, path='/grafico_barra', name="Grafico de barras 📊", order=3)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

nofetal = pd.read_csv(os.path.join(DATA_DIR, "NoFetal.csv"))
divipola = pd.read_csv(os.path.join(DATA_DIR, "Divipola.csv"))

# Verificamos columnas requeridas
required_nofetal = ["AÑO", "COD_DANE", "COD_MUERTE"]
required_divipola = ["COD_DANE", "MUNICIPIO", "DEPARTAMENTO"]
for c in required_nofetal:
    if c not in nofetal.columns:
        raise ValueError(f"Falta la columna {c} en NoFetal")
for c in required_divipola:
    if c not in divipola.columns:
        raise ValueError(f"Falta la columna {c} en Divipola")

nofetal_2019 = nofetal[nofetal["AÑO"] == 2019]
# filtro por código de muerte
homicidios = nofetal_2019[nofetal_2019["COD_MUERTE"].astype(str).str.startswith("X95")]

homicidios_por_mun = (
    homicidios.groupby("COD_DANE")
    .size()
    .reset_index(name="Total_Homicidios")
)

# Combinar con nombres de municipio y departamento
homicidios_por_mun = homicidios_por_mun.merge(divipola, on="COD_DANE", how="left")
# Obtener las 5 ciudades más violentas
top5 = homicidios_por_mun.nlargest(5, "Total_Homicidios")

def create_bar_graph():
  fig = px.bar(
      top5,
      x="MUNICIPIO",
      y="Total_Homicidios",
      color="DEPARTAMENTO",
      text="Total_Homicidios",
      title="Top 5 ciudades más violentas de Colombia (Homicidios por arma de fuego - 2019)",
      labels={"MUNICIPIO": "Ciudad", "Total_Homicidios": "Número de homicidios"},
  )
  fig.update_traces(textposition="outside")
  fig.update_layout(
      title_x=0.5,
      template="plotly_white",
      font=dict(size=14),
      showlegend=True,
      yaxis=dict(title="Número de homicidios"),
      xaxis=dict(title="Ciudad"),
  )
  return fig

# # Layout de la app
# app.layout = html.Div([
#     html.H2("Top 5 ciudades más violentas de Colombia (2019)", style={'textAlign': 'center'}),
#     dcc.Graph(figure=fig)
# ])

# # Ejecutar servidor
# if __name__ == "__main__":
#     app.run(debug=False)

layout = html.Div(children=[
    html.Br(),
    html.H2("Gráfico de líneas", className="fw-bold text-center"),
    dcc.Graph(id="grafica_barra", figure=create_bar_graph())
], className="p-4 m-2", style={"background-color": "#e3f2fd", "height": "auto", })
