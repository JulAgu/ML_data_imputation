import pandas as pd
import numpy as np

df = pd.read_csv("src/raw_om_data.csv", encoding="UTF-8")
df = df.loc[:, ["date", "latitude", "longitude",
                "elevation", "temperature_2m_mean", "temperature_2m_max",
                "temperature_2m_min", "precipitation_sum", "daylight_duration", "wind_speed_10m_max",
                "wind_gusts_10m_max", "shortwave_radiation_sum", "et0_fao_evapotranspiration"]]
df.to_csv("src/marengo.csv", encoding="UTF-8", index=False)
PORCENTAJE = 0.1

# Número de elementos a convertir en NaN
n_nans = int(df.size * PORCENTAJE)
# Seleccionar posiciones aleatorias
flat_indices = np.random.choice(df.size, n_nans, replace=False)
# Convertir a coordenadas (fila, columna)
rows, cols = np.unravel_index(flat_indices, df.shape)

# Introducir NaNs
df_nan = df.copy()
for fila, col in zip(rows, cols):
    if col > 3: # Evitar NaN en columnas de coordenadas y elevación
        df_nan.iat[fila, col] = np.nan

df_nan.to_csv("src/marengo_nans.csv", encoding="UTF-8", index=False)