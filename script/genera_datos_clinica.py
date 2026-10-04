import numpy as np
import pandas as pd

# Generación aleatoria
rng = np.random.default_rng(2026)

# Tiempo medio entre llegadas: 8 minutos
# Tiempo medio de servicio: 6 minutos
tiempos_entre_llegadas = rng.exponential(scale=8.0, size=40)
tiempos_servicio       = rng.exponential(scale=6.0, size=40)

# Armado de datos para ser exportado a formato CSV
df = pd.DataFrame({
    "id_paciente": np.arange(1, 41),
    "tiempo_entre_llegadas_min": tiempos_entre_llegadas.round(2),
    "tiempo_servicio_min":       tiempos_servicio.round(2)
})

# Archivo de salida
df.to_csv("clinica_datos.csv", index=False, decimal=",", sep=";")
print("Archivo 'clinica_datos.csv' generado correctamente.")