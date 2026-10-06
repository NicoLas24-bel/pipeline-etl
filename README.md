# Contexto del proyecto

El objetivo de este proyecto es automatizar la extracción de datos desde una fuente externa, limpiarlos y cargarlos en una base de datos para su análisis.

## stack

- Python (para el script de extracción y transformación)
- PostgreSQL (como Data Warehouse destino)
- Docker (para contenerizar la base de datos y el script).

## Futura mejora

Utilizar Apache Airflow (levantarlo en Docker) para orquestar y programar que este proceso se ejecute automáticamente todos los días a la misma hora.

# Como ejecutar

## 1) clonar proyecto
 - git clone  https://github.com/NicoLas24-bel/pipeline-etl

## 2) crear e iniciar entorno virtual en python
 Ejecutar comando en la terminal, raiz del proyecto (Linux)
 
 - python3 -m venv venv
 - source venv/bin/activate

## 3) instalar dependencias a usar
 - pip install -r requirements.txt

## 4) ejecutar programa
 - python3 etl_pipeline.py