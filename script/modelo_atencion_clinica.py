import pandas as pd
from scipy import stats
import numpy as np

# Uso del archivo .csv generado anteriormente
df = pd.read_csv("clinica_datos.csv", decimal=",", sep=";")

# Lectura de datos desde el archivo .csv
llegadas = df["tiempo_entre_llegadas_min"]
servicio = df["tiempo_servicio_min"]

# Cálculo de tiempo de llegadas y tiempo de servicios
media_llegadas = llegadas.mean()
media_servicio = servicio.mean()

# Promedios de atención y servicios
Lambda_ = 1 / media_llegadas
mu      = 1 / media_servicio

# Utilización
rho = Lambda_ / mu

# Medidas de desempeño M/M/1
L  = Lambda_ / (mu - Lambda_)
Lq = (Lambda_ ** 2) / (mu * (mu - Lambda_))
W  = 1 / (mu - Lambda_)
Wq = Lambda_ / (mu * (mu - Lambda_))
P0 = 1 - rho

# Salida por pantalla
print("== Modelo M/M/1 - Clínica ==")
print(f"lambda: {Lambda_:.4f} pacientes/min")
print(f"mu:     {mu:.4f} pacientes/min")
print(f"rho:    {rho:.4f}")
print(f"numero promedio en sistema L:  {L:.4f}")
print(f"numero promedio en cola Lq:    {Lq:.4f}")
print(f"tiempo promedio en sistema W:  {W:.4f} min")
print(f"tiempo promedio en cola Wq:    {Wq:.4f} min")
print(f"Probabilidad de sistema vacio P0: {P0:.4f}")