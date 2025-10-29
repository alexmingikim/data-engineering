# Data Analysis with DBT

This project demonstrates an end-to-end ELT (Extract, Load, Transform) data pipeline for analysing movie ratings data, using the MovieLens 20M dataset. The pipeline extracts data from CSV files, loads it into Amazon S3 and Snowflake as a raw landing zone, and uses DBT (data build tool) for modular SQL-based transformations.

The pipeline covers:
- Data Ingestion: Storing raw CSV files in S3 and loading via external stages in Snowflake.
- Data Transformation: Building modular SQL models in DBT to create fact and dimension tables, perform aggregations, and enable business intelligence.
- Data Quality: Implementing DBT tests for schema validation, uniqueness, and referential integrity.

## Data Stack

| Component | Technology | Purpose |
|-----------|-----------|----------|
| Storage | Amazon S3 &nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="Amazon S3" width="25" style="vertical-align:middle;"/> | Raw data lake for MovieLens CSVs |
| Data Warehouse | Snowflake &nbsp;<img src="https://www.vectorlogo.zone/logos/snowflake/snowflake-icon.svg" alt="Snowflake" width="25" style="vertical-align:middle;"/> | Scalable storage and querying of raw and transformed data |
| Transformation | DBT (dbt-snowflake adapter) &nbsp;<img src="https://raw.githubusercontent.com/dbt-labs/dbt-styleguide/master/_includes/icons/dbt-logo-full.svg" alt="DBT" width="35" style="vertical-align:middle;"/> | Modular SQL transformations, testing, and documentation |

## Project Structure
```
Data Analysis with dbt/
├── logs/                          # Global dbt run logs and outputs
├── netflix/                       # dbt project root
│   ├── analyses/                  # Ad-hoc SQL analyses
│   ├── dbt_internal_packages/     # Installed dbt packages (e.g., dbt_utils)
│   ├── logs                       # Project-specific logs
│   ├── macros/                    # Custom dbt macros
│   ├── models/                    # Core dbt models
│   │   ├── dim/                   # Dimension models 
│   │   ├── fact/                  # Fact models 
│   │   ├── mart/                  # Data mart
│   │   ├── staging/               # Staging models
│   │   ├── schema.yml             # Model configs, tests, and docs
│   │   └── sources.yml            # Source table definitions
│   ├── seeds/                     # Static CSV seeds
│   ├── snapshots/                 # Snapshot models
│   ├── target/                    # Compiled dbt artifacts (run outputs)
│   └── tests/                     # dbt test definitions (singular tests)
├── .gitignore                     
├── dbt_project.yml                # dbt project configuration
├── README.md                      # This file
├── requirements.txt               # Python dependencies (e.g., dbt-snowflake)
├── snowflake_setup_movielens.sql  # Snowflake DDL for setup
└── venv/                          # Virtual environment (Python)
```

## DBT Lineage Graph 

![DBT Lineage Graph](https://github.com/user-attachments/assets/552c4c55-6460-4aa4-9acc-83044dda581f)































