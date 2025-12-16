import pandas as pd

df = pd.read_csv("afluencia-diaria-metro-simplificado.csv")

resumen = (
    df.groupby(['anio', 'mes', 'linea', 'ESTACION_URI'], as_index=False)
      .agg(afluencia_media=('afluencia', 'mean'))
)

resumen.to_csv("afluencia_media_mensual.csv", index=False)

print(resumen.head())
