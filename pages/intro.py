import dash
from dash import html

dash.register_page(__name__, path='/', name="Descripción", order=0)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Div(children=[
        html.H2("Aplicación web interactiva para el análisis de mortalidad en Colombia"),
        "La aplicación web debe incluir los siguientes elementos visuales que te permitirán explorar datos clave de mortalidad en Colombia, proporcionando una herramienta accesible y completa para identificar patrones demográficos y regionale",
        ]),
    html.Div(children=[
        html.Br(),
        html.H2("Gráficas a visualizar: "),
        html.Ul(
            [
                html.Li(
                  html.Div(children=[
                    html.B("Mapa: "),
                    "Visualización de la distribución total de muertes por departamento en Colombia para el año 2019."
                  ])
                ),
                html.Li(
                  html.Div(children=[
                    html.B("Gráfico de líneas: "),
                    "Representación del total de muertes por mes en Colombia, mostrando variaciones a lo largo del año."
                  ])
                ),
                html.Li(
                  html.Div(children=[
                    html.B("Gráfico de barras: "),
                    "Visualización de las 5 ciudades más violentas de Colombia, considerando homicidios (códigos X95, agresión con disparo de armas de fuego y casos no especificados)"
                  ])
                ),
                html.Li(
                  html.Div(children=[
                    html.B("Gráfico circular: "),
                    "Muestra las 10 ciudades con menor índice de mortalidad."
                  ])
                ),
                html.Li(
                  html.Div(children=[
                    html.B("Tabla: "),
                    "Listado de las 10 principales causas de muerte en Colombia, incluyendo su código, nombre y total de casos (ordenadas de mayor a menor)."
                  ])
                ),
                html.Li(
                  html.Div(children=[
                    html.B("Gráfico de barras apiladas: "),
                    "Comparación del total de muertes por sexo en cada departamento, para analizar diferencias significativas entre géneros."
                  ])
                ),
                html.Li(
                  html.Div(children=[
                    html.B("Histograma: "),
                    "Distribución de muertes, agrupando los valores de la variable GRUPO_EDAD1 según los rangos definidos en la tabla de referencia para identificar patrones de mortalidad a lo largo del ciclo de vida."
                  ])
                ),
            ]
        ),
    ])
], className="p-4 m-2", style={"background-color": "#e3f2fd", "height": "auto", })
