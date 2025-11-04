import os

import dash
import pandas as pd
import plotly.express as px
from dash import Input, Output, dcc, html

# Registrar la página en el proyecto Dash
dash.register_page(__name__, path='/grafico_barra_apilada', name="G. Barra apilada 🧍‍♂️🧍‍♀️", order=8)

# 📂 Directorios
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# 🔹 Cargar datos
nofetal = pd.read_csv(os.path.join(DATA_DIR, "NoFetal.csv"))
divipola = pd.read_csv(os.path.join(DATA_DIR, "Divipola.csv"))

# 🔹 Validar columnas necesarias
required_nofetal = ["AÑO", "COD_DEPARTAMENTO", "SEXO"]
required_divipola = ["COD_DEPARTAMENTO", "DEPARTAMENTO"]

for col in required_nofetal:
  if col not in nofetal.columns:
    raise ValueError(f"Falta la columna '{col}' en NoFetal.csv")

for col in required_divipola:
  if col not in divipola.columns:
    raise ValueError(f"Falta la columna '{col}' en Divipola.csv")

# 🔹 Unir con Divipola para obtener el nombre del departamento
nofetal = nofetal.merge(divipola, on="COD_DEPARTAMENTO", how="left")

# 🔹 Obtener los años disponibles
anios_disponibles = sorted(nofetal["AÑO"].dropna().unique())

# -----------------------------
# 🔸 Layout de la página
# -----------------------------
layout = html.Div([
    html.Br(),
    html.H2("Comparación de muertes por sexo en Colombia", className="fw-bold text-center"),

    # Dropdown para seleccionar año
    html.Div([
      html.Label("Selecciona un año:", className="fw-bold"),
      dcc.Dropdown(
        id="dropdown_anio",
        options=[{"label": str(anio), "value": anio} for anio in anios_disponibles],
        value=2019,
        clearable=False,
        style={"width": "auto"}
      ),
    ], style={"textAlign": "center", "marginBottom": "20px", "height": "30px"}),

    # Gráfico
    dcc.Graph(id="grafico_sexo_departamento", style={"height": "700px"})
], className="p-4 m-2", style={"background-color": "#blue", "height": "200vh", })

# -----------------------------
# 🔸 Callback para actualizar el gráfico según el año
# -----------------------------
@dash.callback(
  Output("grafico_sexo_departamento", "figure"),
  Input("dropdown_anio", "value")
)
def actualizar_grafico(anio):
  # Filtrar por año seleccionado
  df_filtrado = nofetal[nofetal["AÑO"] == anio]
  # Agrupar por departamento y sexo
  muertes_por_sexo = (
    df_filtrado.groupby(["DEPARTAMENTO", "SEXO"])
    .size()
    .reset_index(name="Total_Muertes")
  )
  # Crear gráfico de barras apiladas
  fig = px.bar(
    muertes_por_sexo,
    x="DEPARTAMENTO",
    y="Total_Muertes",
    color="SEXO",
    title=f"Comparación de muertes por sexo en cada departamento ({anio})",
    labels={"DEPARTAMENTO": "Departamento", "Total_Muertes": "Total de muertes"},
  )
  # Estilo del gráfico
  fig.update_layout(
    barmode="stack",
    xaxis_tickangle=-45,
    plot_bgcolor="#f9f9f9",
    paper_bgcolor="#e3f2fd",
    font=dict(size=12),
    legend_title_text="Sexo"
  )
  return fig
