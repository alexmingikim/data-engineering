# Data Engineering Projects 🚀

This repository contains a collection of data engineering projects that demonstrate practical applications of data pipelines, database management, ETL/ELT workflows, and big data tools. The projects are designed to demonstrate skills in building scalable, efficient, and reliable systems for handling data end-to-end.

## 🛠️ Technologies & Tools

Across the projects in this repo, you’ll find implementations using:
- Programming Languages: Python, SQL
- Databases: PostgreSQL, SQL Server, PostgreSQL
- Data Processing: Pandas, DBT, (PySpark)
- Workflow Orchestration: Airflow
- Data Warehousing: Snowflake
- Containers & Deployment: Docker
- Cloud Platforms: AWS

## 📊 List of Projects
- Azure End-to-End Data Engineering Project &nbsp;<img src="https://code.benco.io/icon-collection/azure-icons/Data-Factory.svg" alt="Data Factory" width="20" style="vertical-align:middle;"/> &nbsp;<img src="https://code.benco.io/icon-collection/azure-icons/Data-Lake-Storage-Gen1.svg" alt="Azure Data Lake Storage Gen2" width="20" style="vertical-align:middle;"/> &nbsp;<img src="https://upload.wikimedia.org/wikipedia/commons/9/9d/Databricks-logo.svg" alt="Databricks" width="35" style="vertical-align:middle;"/> &nbsp;<img src="https://upload.wikimedia.org/wikipedia/commons/f/f3/Apache_Spark_logo.svg" alt="PySpark" width="30" style="vertical-align:middle;"/> &nbsp;<img src="https://code.benco.io/icon-collection/azure-icons/Azure-Synapse-Analytics.svg" alt="Azure Synapse Analytics" width="20" style="vertical-align:middle;"/> &nbsp;<img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg" alt="Power BI" width="20" style="vertical-align:middle;"/> (in-progress)
    - This project demonstrates a complete end-to-end data engineering pipeline on Microsoft Azure. It processes the Adventure Works dataset through ingestion, transformation, and serving stages. The pipeline implements the Medallion Architecture (Bronze: raw data, Silver: cleaned/transformed data, Gold: aggregated/serving-ready data) to ensure organised data flow. It covers dynamic ETL pipelines, big data transformations with Spark, secure API integrations, and BI visualisations.

- Data Analysis with **DBT** &nbsp;<img src="https://raw.githubusercontent.com/dbt-labs/dbt-styleguide/master/_includes/icons/dbt-logo-full.svg" alt="DBT" width="35" style="vertical-align:middle;"/> &nbsp;<img src="https://www.vectorlogo.zone/logos/snowflake/snowflake-icon.svg" alt="Snowflake" width="20" style="vertical-align:middle;"/> &nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="Amazon S3" width="25" style="vertical-align:middle;"/>
    - This project demonstrates an end-to-end ELT (Extract, Load, Transform) data pipeline for analysing movie ratings data, using the MovieLens 20M dataset. The pipeline extracts data from CSV files, loads it into Amazon S3 and Snowflake as a raw landing zone, and uses DBT (data build tool) for SQL-based transformations.

- Weather Data ETL Pipeline **(Apache Airflow, AWS (EC2, S3))** &nbsp;<img src="https://upload.wikimedia.org/wikipedia/commons/7/71/AirflowLogo.svg" alt="Apache Airflow" width="35" style="vertical-align:middle;"/> &nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="Amazon S3" width="25" style="vertical-align:middle;"/>
    - This project implements a simple ETL (Extract, Transform, Load) data pipeline using Apache Airflow to fetch real-time weather data from the OpenWeatherMap API, transform it into a structured format using Pandas, and load it into an AWS S3 bucket for storage.

- Stock Ticker Ingestion Pipeline **(Snowflake)** &nbsp;<img src="https://www.vectorlogo.zone/logos/snowflake/snowflake-icon.svg" alt="Snowflake" width="20" style="vertical-align:middle;"/>
    - This project automates the extraction and loading of stock ticker data from the Polygon.io API into a Snowflake data warehouse.