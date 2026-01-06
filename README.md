# Cloud Data Pipelines (Python + ETL)

This repository demonstrates a simple cloud-style data pipeline using Python.
It follows a classic ETL (Extract, Transform, Load) pattern with basic data quality checks
and containerized execution.

---

## What This Project Demonstrates

- Data extraction from raw CSV sources
- Data transformation and normalization
- Data quality validation checks
- Data loading into an analytics-friendly format
- Containerized execution using Docker

---

## Pipeline Flow

Extract  
↓  
Transform  
↓  
Quality Checks  
↓  
Load (Parquet)

---

## Tech Stack

- Python
- Pandas
- SQL (DDL and analytics queries)
- Docker

---

## Repository Structure

cloud-data-pipelines/
- pipelines/
  - extract.py
  - transform.py
  - quality_checks.py
  - load.py
- data/
  - sample.csv
- sql/
  - create_tables.sql
  - sample_queries.sql
- requirements.txt
- Dockerfile
- README.md

---

## Run Locally

Install dependencies:
pip install -r requirements.txt

Run pipeline:
python pipelines/load.py

---

## Run with Docker

Build image:
docker build -t cloud-data-pipelines:local .

Run container:
docker run --rm cloud-data-pipelines:local

---

## Why This Repository Matters

This project reflects real-world data engineering concepts used in cloud environments,
including ETL design, data validation, and containerized execution for reproducibility.
It complements cloud and DevOps workflows by focusing on data reliability and analytics readiness.

---

Author  
Fathima Gousiya  
Cloud Data / DevOps Engineer  
LinkedIn: https://linkedin.com/in/Fathima-gousiya
