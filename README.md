## Contexto del proyecto

El objetivo de este proyecto es automatizar la extracción de datos desde una fuente externa, limpiarlos y cargarlos en una base de datos para su análisis.

# stack

- Python (para el script de extracción y transformación)
- PostgreSQL (como Data Warehouse destino)
- Docker (para contenerizar la base de datos y el script).

# Futura mejora

Utilizar Apache Airflow (levantarlo en Docker) para orquestar y programar que este proceso se ejecute automáticamente todos los días a la misma hora.