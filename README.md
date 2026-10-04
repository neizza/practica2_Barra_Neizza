# Práctica 2 — Modelo M/M/1 aplicado a una clínica

**Estudiante:** Neizza Simona Barra Cuellar
**Materia:** Simulacion
**Fecha:** 4-Octubre-2026

## Descripción
Simulación y análisis de un sistema de colas M/M/1 en un módulo de atención de una clínica, con 40 pacientes y semilla 2026.

## Estructura
practica2_Barra_Neizza
├── datos/clinica_datos.csv
├── scripts/genera_datos_clinica.py
├── scripts/modelo_atencion_clinica.py
├── reporte/informe.txt
└── README.md

## Resultados principales
| Métrica | Valor |
|---|---|
| λ | 0.1218 pac/min |
| μ | 0.1395 pac/min |
| ρ | 0.8733 |
| L | 6.8930 |
| Lq | 6.0197 |
| W | 56.5832 min |
| Wq | 49.4144 min |
| P0 | 0.1267 |

## Outliers (Z-Score)
- Fuertes: 0 en llegadas, 0 en servicio
- Moderados: 1 en llegadas, 1 en servicio

## Conclusión
Sistema congestionado (ρ = 0.8733), con espera promedio de ~49 min. Se recomienda ampliar la capacidad de atención.

## Ejecución
```bash
pip install numpy pandas scipy
python scripts/genera_datos_clinica.py
python scripts/modelo_atencion_clinica.py