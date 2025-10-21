# Data Analysis with dbt

This project demonstrates an end-to-end ELT (Extract, Load, Transform) data pipeline for analyzing movie ratings data, using the MovieLens 20M dataset as a proxy for Netflix-like content recommendation and analysis. The pipeline extracts data from CSV files, loads it into Amazon S3 and Snowflake as a raw landing zone, and uses DBT (data build tool) for modular SQL-based transformations into analytics-ready models.
