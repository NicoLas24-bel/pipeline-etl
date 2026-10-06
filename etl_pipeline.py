import requests
import pandas as pd
from sqlalchemy import create_engine

def extract_data():
    print("1. Extracting data from the API...")
    url = "https://api.open-meteo.com/v1/forecast?latitude=-38.7363&longitude=-72.5974&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=America%2FSantiago&past_days=7"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data from API. Status code: {response.status_code}")



def transform_data(data):
    print("2. Transforming data...")
    daily_data = data['daily']
    df = pd.DataFrame(daily_data)
    df = df.rename(columns={
        'time': 'fecha',
        'temperature_2m_max': 'temp_max_c',
        'temperature_2m_min': 'temp_min_c',
        'precipitation_sum': 'precipitacion_mm',
        '': ''
    })

    df['fecha'] = pd.to_datetime(df['fecha'])
    
    df = df.dropna()

    return df


def load_data(df):
    print("3. Cargando datos a PostgreSQL...")
    engine = create_engine('postgresql+psycopg2://admin:123@localhost:5433/clima_db')
    
    # Escribimos el DataFrame en la tabla 'clima_historico'. 
    # Si la tabla existe, agregamos las filas (append)
    df.to_sql('clima_historico', engine, if_exists='append', index=False)
    print("¡Carga exitosa!")

# --- Bloque principal de ejecución ---
if __name__ == "__main__":
    try:
        datos_crudos = extract_data()
        datos_limpios = transform_data(datos_crudos)
        load_data(datos_limpios)
        
        # Mostramos una muestra por consola para verificar
        print("\nPipeline ETL completado exitosamente.")
        print(datos_limpios)
    except Exception as e:
        print(f"Error en el pipeline: {e}")