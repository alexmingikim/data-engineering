from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import HttpOperator
from airflow.providers.standard.operators.python import PythonOperator
import pandas as pd
import json
import os

def transform_load_data(task_instance):
    # pull data from previous task
    data = task_instance.xcom_pull(task_ids='extract_weather_data')
    
    # Transform: create a simplified dictionary with relevant fields
    transformed_data = {
        'City': data['name'],
        'Description': data['weather'][0]['description'],
        'Temperature (C)': round(data['main']['temp'] - 273.15, 1),
        'Feels Like (C)': round(data['main']['feels_like'] - 273.15, 1),
        'Minimum Temperature (C)': round(data['main']['temp_min'] - 273.15, 1),
        'Maximum Temperature (C)': round(data['main']['temp_max'] - 273.15, 1),
        'Pressure': data['main']['pressure'],
        'Humidity': data['main']['humidity'],  
        'Wind Speed': data['wind']['speed'],
        'Time of Record': datetime.fromtimestamp(data['dt'] + data['timezone']),
        'Sunrise (local time)': datetime.fromtimestamp(data['sys']['sunrise'] + data['timezone']),
        'Sunset (local time)': datetime.fromtimestamp(data['sys']['sunset'] + data['timezone'])
    }
    # convert dictionary to DataFrame
    df_data = pd.DataFrame([transformed_data])

    # load AWS credentials
    with open("aws_credentials.txt") as f:
        for line in f:
            name, value = line.strip().split("=", 1)
            os.environ[name] = value

    aws_credentials = {
        "key": os.environ.get("AWS_ACCESS_KEY_ID"),
        "secret": os.environ.get("AWS_SECRET_ACCESS_KEY"),
        "token": os.environ.get("AWS_SESSION_TOKEN")
    }        

    now = datetime.now().strftime("%d%m%Y_%H%M%S")
    # save to S3 bucket
    filename = f"s3://weatherapiairflowbucket-amk/current_weather_data_auckland_{now}.csv"
    df_data.to_csv(filename, index=False, storage_options=aws_credentials)

    # test locally
    # filename = f"current_weather_data_auckland_{now}.csv"
    # df_data.to_csv(filename, index=False)

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

    # task to transform and load the weather data
    transform_load_weather_data = PythonOperator(
        task_id='transform_load_weather_data',
        python_callable=transform_load_data # function defined above
    )

    # set task dependencies
    is_weather_api_responsive >> extract_weather_data >> transform_load_weather_data
