# Actividad4 - Aplicación web interactiva para el análisis de mortalidad en Colombia

## Análisis de Mortalidad en Colombia 2019 – Aplicación Interactiva con Dash Plotly

## 📘 Introducción

Esta actividad presenta una aplicación web desarrollada en **Dash (Plotly)** la cual permite analizar la mortalidad en Colombia durante el año 2019. A través de diferentes visualizaciones interactivas, el sistema facilita la exploración de patrones y causas de muerte por sexo, grupo de edad, departamento y ciudad, integrando datos abiertos del DANE. La información se carga por medio de archivos CSV. Los cuales puede descargar desde:
https://microdatos.dane.gov.co/index.php/catalog/696/get-microdata

---

## 🎯 Objetivo

La aplicación busca desarollar habilidades en el análisis de datos utilizando el lenguaje de programación Python y herramientas de visualización interactivas, además, identificar tendencias y diferencias significativas en los índices de mortalidad a partir de fuentes oficiales. Dentro de las gráficas podremos visualizar información relevante como:

- Las principales causas de muerte a nivel nacional.
- Las diferencias entre sexos en cada departamento.
- La distribución de muertes por grupos de edad.
- Las ciudades con menor índice de mortalidad.

Con ello, se pretende aportar una herramienta de análisis visual útil para entidades de salud pública, investigadores y estudiantes interesados en epidemiología y análisis de datos.

---

## 🏛️ Estructura del Proyecto

```bash
├── data/
│ ├── CodigosDeMuerte.csv
│ ├── Divipola.csv
│ └── NoFetal.csv
├── pages/
│ ├── grafico_barra_apilada.py
│ ├── grafico_barra.py
│ ├── grafico_circular.py
│ ├── grafico_linea.py
│ ├── histograma.py
│ ├── intro.py
│ ├── mapa.py
│ └── tabla.py
├── src/
│ ├── convertidor.py # Los archivos xlsx deben ser convertidos a csv para poder funcionar
│ └── main.py
└── requirements.txt
```

---

## 📋 Requisitos

Asegúrate de tener instalado **Python 3.11+**. para poder crear el entorno virtual (venv)
Las dependencias necesarias se encuentran registradas en el archivo requirements.txt
Dentro de este archivo encontrará paquetes como:

- dash==3.2.0
- geopandas==1.1.1
- pandas==2.3.3

_(Puedes instalar todas las dependencias con `pip install -r requirements.txt`)_
... etc.

---

## Software Utilizado

- **Python 3.11+**
- **Dash** – Framework principal para la creación de interfaces web interactivas.
- **Plotly** – Librería para visualización de datos en gráficos dinámicos.
- **Pandas** – Procesamiento y análisis de datos tabulares.
- **Gunicorn** – Servidor WSGI utilizado para el despliegue en Render.
- **VS Code** – Entornos de desarrollo.

---

## 💻 Instalación y Ejecución Local
