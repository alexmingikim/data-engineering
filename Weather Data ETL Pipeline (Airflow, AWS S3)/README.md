# Weather Data ETL Pipeline (Apache Airflow + AWS S3)

This project implements a simple ETL (Extract, Transform, Load) data pipeline using Apache Airflow to fetch real-time weather data from the OpenWeatherMap API, transform it into a structured format using Pandas, and load it into an AWS S3 bucket for storage.

## Overview

The pipeline performs the following key steps:

- Extract — Uses an HTTP connection to fetch current weather data for a specific city (Auckland) from the OpenWeatherMap API.
- Transform — Parses and transforms the JSON response to extract relevant fields (temperature, humidity, wind speed, etc.) and converts units where needed.
- Load — Saves the transformed dataset as a CSV file in an AWS S3 bucket

## Architecture 

![Architecture](https://github.com/user-attachments/assets/cb548a08-6568-48b3-9121-964fdb30aa25)

## Airflow DAG flow diagram

![Airflow DAG Flow](https://github.com/user-attachments/assets/fc6a76fd-fc9c-480e-987d-1dd2d7e63196)

### Tasks:

- is_weather_api_responsive — Uses HttpSensor to check API availability.
- extract_weather_data — Calls the API and pulls JSON weather data.
- transform_load_weather_data — Transforms the JSON response into a clean CSV and uploads it to S3.

## Project Structure

```
weather-data-etl/
├── dags/
│ └── weather_dag.py                    # Main DAG definition
├── airflow/
│ ├── airflow.cfg                       # Airflow configuration (not on github)
│ ├── airflow.db                        # Metadata database
│ └── logs/                             # Task execution logs
├── aws_credentials.txt                 # Local AWS credentials file (not on github)
├── requirements.txt                    # Python dependencies
└── README.md                           # Project documentation
```


## Output

![Output Screenshot](https://github.com/user-attachments/assets/744312f4-e4fb-44b1-8cd5-641df59bae52)

Structured csv file stored within an AWS S3 bucket. 