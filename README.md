# mdm
Enterprise Customer MDM platform that ingests data from multiple sources, validates, cleans, standardizes, detects duplicate customers using configurable matching, creates Golden Records, and exposes trusted customer data via APIs, events, and analytics-ready datasets.
# Enterprise Master Data Management Platform

## Overview

Enterprise organizations receive customer information from multiple systems such as CRM, Claims, Mobile Applications, Employer Systems, and Partner APIs.

Each source contains different representations of the same customer.

Examples include

• Duplicate records
• Missing values
• Different phone formats
• Different address formats
• Conflicting information
• Invalid values

This project demonstrates how to build a modern Master Data Management (MDM) platform capable of producing a trusted Golden Record.

The project focuses on architecture, scalability, extensibility, observability, and production-ready engineering practices.

---

## Features

✔ Multi-source ingestion

✔ Canonical data model

✔ Configurable data standardization

✔ Configurable data quality framework

✔ Identity Resolution Engine

✔ Golden Record Generation

✔ Survivorship Rules

✔ Lineage Tracking

✔ Reconciliation Reports

✔ Metrics & Monitoring

✔ REST API

✔ Configuration-driven processing

✔ Plugin architecture

---

## High Level Flow

```

CRM CSV
Claims API
Mobile JSON
Employer DB

↓

Ingestion

↓

Canonical Model

↓

Standardization

↓

Data Quality

↓

Identity Resolution

↓

Golden Record

↓

Serving Layer

```

---

## Project Goals

The objective is to demonstrate enterprise-scale data engineering concepts rather than only ETL transformations.

The platform is designed around

- Separation of concerns
- Extensibility
- Scalability
- Maintainability
- Production readiness

---

## Technology Stack

Python

Pandas

RapidFuzz

FastAPI

DuckDB

YAML

Docker

Pytest

Prometheus

Grafana

---

## Sample Pipeline

```

python main.py

```

Pipeline Output

```

Source Records

↓

Canonical Records

↓

Standardized Records

↓

Validated Records

↓

Matched Records

↓

Golden Records

↓

Reconciliation Report

```

---

## Future Enhancements

Apache Spark

Kafka

Delta Lake

Iceberg

Airflow

Snowflake

AWS S3

ML-assisted Matching

Vector Search

LLM-assisted Data Quality

