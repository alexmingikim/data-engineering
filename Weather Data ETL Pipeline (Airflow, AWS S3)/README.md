# Automated Weather Data ETL Pipeline using Airflow and AWS S3

This project automates an ETL (Extract, Transform, Load) pipeline that fetches current weather data from the OpenWeatherMap API, transforms it into a structured format, and loads it into an Amazon S3 bucket using Apache Airflow.

## Features 

- Automated Scheduling: Airflow DAG runs the ETL job on a defined schedule.

- API Integration: Retrieves live weather data using OpenWeatherMap API.

- Data Transformation: Cleans and structures JSON response into a tabular format (CSV/JSON).

- Cloud Storage: Uploads transformed data files to an Amazon S3 bucket.

- Modular Design: Each ETL step (Extract, Transform, Load) is implemented as a reusable task.