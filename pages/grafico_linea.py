import os

import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html

dash.register_page(__name__, path='/grafico_linea', name="Grafico de líneas 📈", order=2)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

nofetal = pd.read_csv(os.path.join(DATA_DIR, "NoFetal.csv"))
divipola = pd.read_csv(os.path.join(DATA_DIR, "Divipola.csv"))

required_cols = ["AÑO", "MES", "COD_DEPARTAMENTO"]
missing = [c for c in required_cols if c not in nofetal.columns]
if missing:
    raise ValueError(f"Faltan columnas requeridas: {missing}")

# Filtrar año 2019
nofetal_2019 = nofetal[nofetal["AÑO"] == 2019]

# Agrupar por mes
muertes_por_mes = (
    nofetal_2019.groupby("MES")
    .size()
    .reset_index(name="Total_Muertes")
    .sort_values("MES")
)

# Convertir número de mes a nombre (opcional)
meses_nombres = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}
muertes_por_mes["MES_NOMBRE"] = muertes_por_mes["MES"].map(meses_nombres)

# Crear gráfico de líneas
def create_line_graph():
  fig = px.line(
    muertes_por_mes,
    x="MES_NOMBRE",
    y="Total_Muertes",
    markers=True,
    title="Total de muertes por mes en Colombia (2019)",
    labels={"MES_NOMBRE": "Mes", "Total_Muertes": "Número de muertes"},
  )
  fig.update_traces(line_color="#007BFF", line_width=3)
  fig.update_layout(
      title_x=0.5,
      template="plotly_white",
      font=dict(size=14),
      hovermode="x unified"
  )
  return fig

# # Layout de la página Dash
# app.layout = html.Div([
#     html.H2("Distribución mensual de muertes en Colombia - 2019", style={'textAlign': 'center'}),
#     dcc.Graph(figure=fig)
# ])

# # Ejecutar la app
# if __name__ == "__main__":
#     app.run(debug=True)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    html.H2("Gráfico de líneas", className="fw-bold text-center"),
    dcc.Graph(id="grafico_linea", figure=create_line_graph())
], className="p-4 m-2", style={"background-color": "#e3f2fd", "height": "auto", })
