import os

import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

pd.read_excel(os.path.join(DATA_DIR, "NoFetal.xlsx")).to_csv(os.path.join(DATA_DIR, "NoFetal.csv"), index=False)
pd.read_excel(os.path.join(DATA_DIR, "Divipola.xlsx")).to_csv(os.path.join(DATA_DIR, "Divipola.csv"), index=False)
pd.read_excel(os.path.join(DATA_DIR, "CodigosDeMuerte.xlsx")).to_csv(os.path.join(DATA_DIR, "CodigosDeMuerte.csv"), index=False)

