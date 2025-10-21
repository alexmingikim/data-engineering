# Data Engineering Projects 🚀

This repository contains a collection of data engineering projects that demonstrate practical applications of data pipelines, database management, ETL (Extract, Transform, Load) workflows, and big data tools. The projects are designed to showcase skills in building scalable, efficient, and reliable systems for handling data end-to-end.

## 🛠️ Technologies & Tools

Across the projects in this repo, you’ll find implementations using:
- Programming Languages: Python, SQL
- Databases: PostgreSQL, SQL Server, PostgreSQL
- Data Processing: Pandas, (PySpark)
- Workflow Orchestration: Airflow
- Data Warehousing: Snowflake
- Containers & Deployment: Docker
- Cloud Platforms: AWS

*(Not every project uses all tools; see project-specific READMEs for details*.)

## 📊 List of Projects
- Data Analysis with **dbt** (in-progress)
    - This project demonstrates an end-to-end ELT (Extract, Load, Transform) data pipeline for analysing movie ratings data, using the MovieLens 20M dataset as a proxy for Netflix-like content recommendation and analysis. The pipeline extracts data from CSV files, loads it into Amazon S3 and Snowflake as a raw landing zone, and uses DBT (data build tool) for SQL-based transformations into analytics-ready models.

- Weather Data ETL Pipeline **(Apache Airflow, AWS (EC2, S3))**
    - This project implements a simple ETL (Extract, Transform, Load) data pipeline using Apache Airflow to fetch real-time weather data from the OpenWeatherMap API, transform it into a structured format using Pandas, and load it into an AWS S3 bucket for storage.

- Stock Ticker Ingestion Pipeline **(Snowflake)** 
    - This project automates the extraction and loading of stock ticker data from the Polygon.io API into a Snowflake data warehouse.