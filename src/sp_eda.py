import pandas as pd
import numpy as np


def eda_preliminar (df):
  
  display(df.sample(5))
  print('------------------------')
  print('DIMENSIONES')
  print(f'nuestro conjunto de datos presenta {df.shape[0]} filas y {df.shape[1]} columnas')
  print('------------------------')
  print('INFO')
  display(df.info())
  print('------------------------')
  print('NULOS')
  display(df.isnull().sum()/df.shape[0]*100)
  print('------------------------')
  print('DUPLICADOS')
  print(f'tenemos un total de {df.duplicated().sum()} duplicados')
  print('------------------------')
  print('FRECUENCIA CATEGORICAS')
  # Mostrar todo sin truncar mientras dure este with
  with pd.option_context(
    "display.max_rows", None,        # no recortar filas
    "display.max_colwidth", None,    # no recortar texto
    "display.width", 0               # ajustar al ancho
):
    for col in df.select_dtypes(include="object").columns:
        # normaliza: quita espacios, unifica NaN
        s = df[col].astype(str).str.strip()
        s = s.replace({"": np.nan, "nan": np.nan, "None": np.nan})

        vc = s.value_counts(dropna=False)  # incluye NaN
        print(f"\n==== {col.upper()} (unique={vc.size}) ====")
        display(vc.to_frame("count"))