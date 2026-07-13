# Data Model Design

**Project:** Enterprise Master Data Management (MDM) Platform

**Version:** 1.0

---

# 1. Overview

The Enterprise MDM Platform revolves around a **Canonical Data Model**.

Every incoming source record—regardless of whether it originates from a CSV file, REST API, relational database, event stream, or message queue—is transformed into a common representation before any downstream processing occurs.

This approach provides:

- Source independence
- Consistent processing
- Simplified validation
- Reusable business rules
- Easier testing
- Better scalability

---

# 2. Data Model Layers

```
                    Source Systems
                         │
                         ▼
                Source Record Models
                         │
                         ▼
               Canonical CustomerRecord
                         │
        ┌────────────────┼─────────────────┐
        ▼                ▼                 ▼
 Validation         Standardization    Metadata
        │                │                 │
        └───────────────┬──────────────────┘
                        ▼
               Identity Resolution
                        │
                        ▼
                 Match Result Model
                        │
                        ▼
                Golden Record Model
                        │
        ┌───────────────┴────────────────┐
        ▼                                ▼
    Lineage Model              Reconciliation
```

---

# 3. Entity Relationship Diagram

```
SourceRecord
      │
      │ transforms into
      ▼

CustomerRecord
      │
      │ validated by
      ▼

ValidationResult

CustomerRecord
      │
      │ compared with
      ▼

MatchResult

MatchResult
      │
      │ merged into
      ▼

GoldenRecord

GoldenRecord
      │
      │ traced using
      ▼

LineageRecord

Pipeline
      │
      │ generates
      ▼

ReconciliationReport
```

---

# 4. Core Entities

---

# 4.1 SourceRecord

Represents the raw record received from an external system.

Example

CRM

Claims

Employer

Partner API

---

### Attributes

| Field | Type | Description |
|---------|------|-------------|
| source | string | Source system |
| source_id | string | Original record identifier |
| payload | dict | Raw payload |
| batch_id | string | Batch identifier |
| received_at | datetime | Arrival timestamp |
| metadata | dict | Additional source metadata |

---

Example

```json
{
  "source":"CRM",
  "source_id":"101",
  "payload":{
      "name":"Mukesh Kumar",
      "phone":"9876543210"
  }
}
```

---

# 4.2 CustomerRecord (Canonical Model)

This is the most important entity.

Every downstream component uses this model.

---

### Attributes

| Field | Type | Required |
|---------|------|----------|
| source | string | Yes |
| source_id | string | Yes |
| first_name | string | Yes |
| last_name | string | No |
| full_name | string | Yes |
| phone | string | No |
| email | string | No |
| address | string | No |
| city | string | No |
| state | string | No |
| country | string | No |
| postal_code | string | No |
| birth_date | date | No |
| gender | string | No |
| last_updated | datetime | Yes |

---

Example

```json
{
    "source":"CRM",
    "source_id":"101",
    "full_name":"Mukesh Kumar",
    "phone":"9876543210",
    "email":"mukesh@gmail.com",
    "city":"Bangalore"
}
```

---

# 4.3 Metadata

Every CustomerRecord carries metadata.

### Attributes

| Field | Description |
|---------|-------------|
| batch_id | Processing batch |
| ingestion_time | Record arrival time |
| file_name | Source filename |
| pipeline_version | Pipeline version |
| checksum | Duplicate detection |
| processing_time | Processing duration |

---

# 4.4 ValidationResult

Represents outcome of Data Quality validation.

---

### Attributes

| Field | Description |
|---------|-------------|
| passed | Boolean |
| warnings | List |
| errors | List |
| rule_results | List |
| validation_time | Timestamp |

---

Example

```json
{
   "passed":false,
   "errors":[
      "Phone Missing",
      "Invalid Email"
   ]
}
```

---

# 4.5 ValidationRule

Represents one configurable business rule.

---

### Attributes

| Field | Description |
|---------|-------------|
| id | Rule identifier |
| name | Rule name |
| severity | Error/Warning |
| field | Target field |
| expression | Validation logic |
| enabled | Boolean |

---

Example

```yaml
id: DQ001
field: phone
rule: required
severity: ERROR
```

---

# 4.6 MatchResult

Stores duplicate matching outcome.

---

### Attributes

| Field | Description |
|---------|-------------|
| record1 | CustomerRecord |
| record2 | CustomerRecord |
| phone_score | float |
| email_score | float |
| name_score | float |
| address_score | float |
| total_score | float |
| matched | Boolean |

---

Example

```json
{
   "phone_score":60,
   "email_score":30,
   "name_score":10,
   "total_score":100,
   "matched":true
}
```

---

# 4.7 Duplicate Cluster

Multiple records representing one person.

```
CRM

↓

Claims

↓

Employer

↓

Mobile

↓

Cluster
```

---

Attributes

| Field | Description |
|---------|-------------|
| cluster_id | Duplicate cluster |
| members | Source records |
| confidence | Cluster confidence |

---

# 4.8 GoldenRecord

Trusted enterprise customer.

---

### Attributes

| Field | Description |
|---------|-------------|
| golden_id | Enterprise identifier |
| full_name | Selected value |
| phone | Selected value |
| email | Selected value |
| address | Selected value |
| confidence | Overall confidence |
| created_at | Timestamp |
| updated_at | Timestamp |

---

Example

```json
{
  "golden_id":"G100001",
  "full_name":"Mukesh Kumar",
  "phone":"9876543210",
  "email":"mukesh@gmail.com"
}
```

---

# 4.9 SurvivorshipDecision

Stores why a field was selected.

---

### Attributes

| Field | Description |
|---------|-------------|
| attribute | Field name |
| selected_source | Winning source |
| selected_value | Selected value |
| rule | Applied rule |

---

Example

```
Phone

↓

CRM

↓

9876543210

↓

Highest Priority
```

---

# 4.10 LineageRecord

Maintains complete traceability.

---

### Attributes

| Field | Description |
|---------|-------------|
| golden_id | Golden Record |
| source | Source system |
| source_id | Original identifier |
| operation | Transformation |
| timestamp | Processing time |
| reason | Explanation |

---

Example

```
Golden

↓

Phone

↓

Selected

↓

CRM

↓

Highest Priority
```

---

# 4.11 ReconciliationReport

Compares counts across stages.

---

### Attributes

| Field | Description |
|---------|-------------|
| source_count | Original records |
| canonical_count | Canonical records |
| standardized_count | Standardized |
| validated_count | Valid |
| duplicate_count | Duplicate |
| golden_count | Golden |
| rejected_count | Failed |

---

Example

| Stage | Count |
|--------|------:|
| Source | 1000 |
| Canonical | 1000 |
| Standardized | 998 |
| Validated | 972 |
| Golden | 810 |

---

# 4.12 PipelineExecution

Represents one pipeline execution.

---

### Attributes

| Field | Description |
|---------|-------------|
| pipeline_id | Execution identifier |
| start_time | Start timestamp |
| end_time | End timestamp |
| duration | Execution time |
| status | SUCCESS/FAILED |
| records_processed | Count |

---

# 4.13 Processing Metrics

Metrics emitted by every component.

| Metric | Description |
|---------|-------------|
| records_read | Records read |
| records_failed | Failed records |
| duplicates_found | Duplicate entities |
| golden_created | Golden Records |
| processing_time | Stage duration |
| throughput | Records/sec |

---

# 5. Relationships

```
SourceRecord

1

↓

1

CustomerRecord

↓

1

ValidationResult

↓

1

MatchResult

↓

N

DuplicateCluster

↓

1

GoldenRecord

↓

N

LineageRecord
```

---

# 6. Data Lifeccle

```
Raw Source

↓

SourceRecord

↓

CustomerRecord

↓

Standardized CustomerRecord

↓

Validated CustomerRecord

↓

Matched Records

↓

Duplicate Cluster

↓

Golden Record

↓

Published API
```

---

# 7. Schema Evolution

The canonical model is versioned.

```
CustomerRecord

v1

↓

v2

↓

v3
```

New attributes are added without breaking existing consumers.

Rules

- Never remove existing fields.
- Add optional fields first.
- Version API contracts.
- Maintain backward compatibility.

---

# 8. Persistence Strategy

| Entity | Storage |
|----------|---------|
| SourceRecord | Bronze Layer |
| CustomerRecord | Silver Layer |
| GoldenRecord | Gold Layer |
| LineageRecord | Metadata Store |
| Metrics | Time Series DB |
| Configuration | YAML Repository |

---

# 9. Future Enhancements

Future versions may include:

- Organization entity
- Household entity
- Employer entity
- Relationship graph
- Address history
- Contact history
- ML feature store
- Embedding vectors for semantic matching
- Knowledge graph integration

---

# 10. Summary

The Enterprise MDM Platform is centered around a canonical CustomerRecord that enables all downstream processing to remain independent of source-specific schemas.

Supporting entities such as ValidationResult, MatchResult, GoldenRecord, LineageRecord, and ReconciliationReport provide the metadata, traceability, and auditability required for enterprise-scale Master Data Management systems. This layered data model is designed to evolve over time while maintaining backward compatibility and supporting future enhancements such as streaming ingestion, machine learning-assisted matching, and cloud-native lakehouse architectures.
