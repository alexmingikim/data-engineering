from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.http.sensors.http import HttpSensor
import json

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 1),
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}

# Define the DAG
with DAG('weather_dag', # dag name must be unique
         default_args=default_args,
         schedule='@daily',
         catchup=False) as dag:
    
        # sensor to check if the OpenWeatherMap API is responsive    
        is_weather_api_responsive = HttpSensor(
            task_id='is_weather_api_responsive', # task name must be unique
            http_conn_id='weathermap_api', # connection id created in Airflow UI
            endpoint='/data/2.5/weather?q=Auckland&appid=d440696d648c087f73a5a238f346fe9e'
        )
