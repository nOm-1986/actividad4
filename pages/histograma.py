import os

import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html

# Registrar la página
dash.register_page(__name__, path='/histograma', name="Distribución por edad 🎂", order=9)

# 📂 Directorios
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# 🔹 Cargar datos
nofetal = pd.read_csv(os.path.join(DATA_DIR, "NoFetal.csv"))

# 🔹 Validar columnas necesarias
required_cols = ["AÑO", "GRUPO_EDAD1"]
for col in required_cols:
  if col not in nofetal.columns:
    raise ValueError(f"Falta la columna '{col}' en NoFetal.csv")

# 🔹 Filtrar año 2019
nofetal_2019 = nofetal[nofetal["AÑO"] == 2019]

# ---------------------------------------------------
# 🔸 Mapeo de GRUPO_EDAD1 → Categoría de edad (según DANE)
# ---------------------------------------------------
def clasificar_edad(codigo):
  if codigo in range(0, 5):  # 0–4
    return "Mortalidad neonatal (0–1 mes)"
  elif codigo in range(5, 7):  # 5–6
    return "Mortalidad infantil (1–11 meses)"
  elif codigo in range(7, 9):  # 7–8
      return "Primera infancia (1–4 años)"
  elif codigo in range(9, 11):  # 9–10
    return "Niñez (5–14 años)"
  elif codigo == 11:
    return "Adolescencia (15–19 años)"
  elif codigo in range(12, 14):  # 12–13
      return "Juventud (20–29 años)"
  elif codigo in range(14, 17):  # 14–16
    return "Adultez temprana (30–44 años)"
  elif codigo in range(17, 20):  # 17–19
    return "Adultez intermedia (45–59 años)"
  elif codigo in range(20, 25):  # 20–24
    return "Vejez (60–84 años)"
  elif codigo in range(25, 29):  # 25–28
    return "Longevidad / Centenarios (85–100+ años)"
  elif codigo == 29:
    return "Edad desconocida"
  else:
    return "Sin clasificación"

# 🔹 Aplicar clasificación
nofetal_2019["Categoría_Edad"] = nofetal_2019["GRUPO_EDAD1"].apply(clasificar_edad)

# 🔹 Contar muertes por categoría
distribucion = (
  nofetal_2019.groupby("Categoría_Edad")
  .size()
  .reset_index(name="Total_Muertes")
  .sort_values("Total_Muertes", ascending=False)
)

# 🔹 Crear histograma
fig = px.bar(
  distribucion,
  x="Categoría_Edad",
  y="Total_Muertes",
  text="Total_Muertes",
  title="Distribución de muertes por grupo de edad (2019)",
  labels={"Categoría_Edad": "Grupo de Edad", "Total_Muertes": "Total de Muertes"},
)

# 🔹 Personalización visual
fig.update_traces(marker_color="#007BFF", textposition="outside")
fig.update_layout(
  plot_bgcolor="#f9f9f9",
  paper_bgcolor="#e3f2fd",
  xaxis_tickangle=-25,
  font=dict(size=12),
  title_x=0.5
)

# ---------------------------------------------------
# 🔸 Layout de la página
# ---------------------------------------------------
layout = html.Div([
  html.Br(),
  html.H2("Distribución de muertes por grupo de edad en Colombia (2019)", className="fw-bold text-center"),
  dcc.Graph(figure=fig, style={"height": "700px"})
], className="p-4 m-2", style={"background-color": "#e3f2fd", "height": "auto", })
