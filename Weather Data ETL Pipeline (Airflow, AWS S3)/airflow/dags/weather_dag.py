from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import HttpOperator
import json

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 1),
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}

# define the DAG
with DAG(
    dag_id = 'weather_dag', # dag name must be unique
    default_args=default_args,
    schedule='@daily',
    catchup=False
) as dag:
    
    # sensor to check if the OpenWeatherMap API is responsive    
    is_weather_api_responsive = HttpSensor(
        task_id='is_weather_api_responsive', # task name must be unique
        http_conn_id='weathermap_api', # connection id created in Airflow UI
        endpoint='data/2.5/weather?q=Auckland&appid=d440696d648c087f73a5a238f346fe9e'
    )

    # operator to call the OpenWeatherMap API and get weather data
    extract_weather_data = HttpOperator(
        task_id='extract_weather_data',
        http_conn_id='weathermap_api',
        endpoint='data/2.5/weather?q=Auckland&appid=d440696d648c087f73a5a238f346fe9e',
        method='GET',
        response_filter=lambda response: json.loads(response.text),
        log_response=True
    )

    # set task dependencies
    is_weather_api_responsive >> extract_weather_data
