# Sequence Diagrams

**Project:** Enterprise Master Data Management (MDM) Platform

**Version:** 1.0

---

# 1. Overview

This document describes the runtime interaction between components in the Enterprise Master Data Management (MDM) Platform.

The platform follows a pipeline architecture where each stage transforms or enriches the data before passing it to the next stage.

Every stage captures metadata, logs execution details, emits metrics, and records lineage information.

---

# 2. End-to-End Processing Flow

```
        Source Systems
             │
             ▼
      Ingestion Framework
             │
             ▼
     Canonical Transformation
             │
             ▼
   Standardization Framework
             │
             ▼
    Data Quality Framework
             │
             ▼
 Identity Resolution Engine
             │
             ▼
   Golden Record Generator
             │
      ┌──────┴────────┐
      ▼               ▼
 Lineage         Reconciliation
      │               │
      └──────┬────────┘
             ▼
        Golden Record Store
             │
             ▼
          REST API
```

---

# 3. Complete Pipeline Sequence

```mermaid
sequenceDiagram

participant CRM
participant Claims
participant Mobile

participant Ingestion
participant Canonical
participant Standardizer
participant Validator
participant Matcher
participant Survivorship
participant Lineage
participant Reconciliation
participant Repository
participant API

CRM->>Ingestion: Read CSV
Claims->>Ingestion: Read JSON
Mobile->>Ingestion: Read API

Ingestion->>Canonical: Create CustomerRecord

Canonical->>Standardizer: Standardize fields

Standardizer->>Validator: Validate data quality

Validator->>Matcher: Valid records

Matcher->>Survivorship: Duplicate clusters

Survivorship->>Repository: Save Golden Record

Survivorship->>Lineage: Record merge decisions

Repository->>Reconciliation: Record counts

API->>Repository: Query Golden Record

Repository-->>API: Return Result
```

---

# 4. Data Ingestion Sequence

Purpose

- Read heterogeneous sources
- Capture metadata
- Convert into canonical model

```mermaid
sequenceDiagram

participant Source
participant Connector
participant Metadata
participant Canonical

Source->>Connector: Read Data

Connector->>Metadata: Capture metadata

Metadata-->>Connector: Metadata

Connector->>Canonical: Create CustomerRecord

Canonical-->>Connector: Success
```

---

# 5. Standardization Sequence

Purpose

Normalize all customer attributes.

```mermaid
sequenceDiagram

participant Pipeline
participant Phone
participant Email
participant Address
participant Name

Pipeline->>Phone: Normalize Phone

Phone-->>Pipeline: Standard Phone

Pipeline->>Email: Normalize Email

Email-->>Pipeline: Standard Email

Pipeline->>Address: Normalize Address

Address-->>Pipeline: Standard Address

Pipeline->>Name: Normalize Name

Name-->>Pipeline: Standard Name
```

---

# 6. Data Quality Validation

Purpose

Validate configurable business rules.

```mermaid
sequenceDiagram

participant Pipeline

participant RuleEngine

participant Rule1

participant Rule2

participant Rule3

Pipeline->>RuleEngine: Validate Record

RuleEngine->>Rule1: Required Fields

Rule1-->>RuleEngine: PASS

RuleEngine->>Rule2: Email Validation

Rule2-->>RuleEngine: PASS

RuleEngine->>Rule3: Phone Validation

Rule3-->>RuleEngine: FAIL

RuleEngine-->>Pipeline: ValidationResult
```

---

# 7. Identity Resolution

Purpose

Determine whether multiple records belong to the same customer.

```mermaid
sequenceDiagram

participant Matcher

participant Phone

participant Email

participant Name

participant Score

Matcher->>Phone: Compare Phone

Phone-->>Matcher: 60

Matcher->>Email: Compare Email

Email-->>Matcher: 30

Matcher->>Name: Compare Name

Name-->>Matcher: 10

Matcher->>Score: Total Score

Score-->>Matcher: 100

Matcher-->>Matcher: Duplicate Found
```

---

# 8. Golden Record Generation

Purpose

Generate one trusted customer record.

```mermaid
sequenceDiagram

participant Cluster

participant Survivorship

participant Rules

participant Golden

Cluster->>Survivorship: Duplicate Records

Survivorship->>Rules: Source Priority

Rules-->>Survivorship: CRM Wins

Survivorship->>Golden: Create Golden Record

Golden-->>Survivorship: Success
```

---

# 9. Lineage Tracking

Purpose

Maintain complete auditability.

```mermaid
sequenceDiagram

participant Pipeline

participant Lineage

participant Repository

Pipeline->>Lineage: Transformation

Pipeline->>Lineage: Validation

Pipeline->>Lineage: Matching

Pipeline->>Lineage: Merge Decision

Lineage->>Repository: Persist Lineage
```

---

# 10. Reconciliation

Purpose

Compare record counts between stages.

```mermaid
sequenceDiagram

participant Pipeline

participant Metrics

participant Report

Pipeline->>Metrics: Source Count

Pipeline->>Metrics: Canonical Count

Pipeline->>Metrics: Valid Count

Pipeline->>Metrics: Duplicate Count

Pipeline->>Metrics: Golden Count

Metrics->>Report: Generate Report
```

---

# 11. REST API Lookup

Purpose

Expose Golden Records to downstream systems.

```mermaid
sequenceDiagram

participant Client

participant API

participant Repository

Client->>API: GET /customers/G1001

API->>Repository: Fetch Golden Record

Repository-->>API: Golden Record

API-->>Client: JSON Response
```

---

# 12. Error Handling Flow

```mermaid
sequenceDiagram

participant Component

participant Logger

participant Metrics

participant Pipeline

Component->>Logger: Log Error

Component->>Metrics: Increment Failure Count

Component-->>Pipeline: Error Response

Pipeline-->>Pipeline: Retry or Continue
```

---

# 13. Pipeline Lifecycle

```
Read Sources

↓

Capture Metadata

↓

Canonical Transformation

↓

Standardization

↓

Validation

↓

Identity Resolution

↓

Duplicate Clustering

↓

Golden Record Creation

↓

Lineage Recording

↓

Reconciliation

↓

Persist

↓

Serve API
```

---

# 14. Processing States

```
RAW

↓

INGESTED

↓

CANONICAL

↓

STANDARDIZED

↓

VALIDATED

↓

MATCHED

↓

MERGED

↓

GOLDEN

↓

PUBLISHED
```

---

# 15. Parallel Processing Opportunities

The following stages can execute concurrently:

### Source Ingestion

```
CRM
Claims
Mobile
Employer
Partner

↓

Parallel Readers
```

---

### Standardization

```
Phone

Email

Address

Name

↓

Independent Execution
```

---

### Validation

```
Rule 1

Rule 2

Rule 3

Rule N

↓

Parallel Rule Evaluation
```

---

### Identity Resolution

Duplicate detection can be partitioned by:

- Country
- State
- Customer Hash
- Blocking Keys

This enables horizontal scaling across multiple workers.

---

# 16. Sequence Summary

| Stage | Input | Output |
|---------|--------|---------|
| Ingestion | Raw Data | CustomerRecord |
| Canonical | Source Record | Canonical Record |
| Standardization | Canonical Record | Standard Record |
| Validation | Standard Record | ValidationResult |
| Matching | Valid Records | Duplicate Clusters |
| Survivorship | Duplicate Cluster | Golden Record |
| Lineage | Pipeline Events | LineageRecord |
| Reconciliation | Pipeline Metrics | Report |
| API | Golden ID | Customer Response |

---

# 17. Future Enhancements

The sequence diagrams are designed to accommodate future capabilities without changing the overall processing flow.

Future enhancements include:

- Apache Kafka event-driven ingestion
- Change Data Capture (CDC)
- Apache Spark distributed execution
- Delta Lake / Apache Iceberg persistence
- ML-assisted entity matching
- AI-assisted survivorship recommendations
- Event publishing after Golden Record creation
- Workflow orchestration with Apache Airflow or Argo Workflows

The modular sequence ensures that new components can be inserted between existing stages while preserving loose coupling and maintainability.
