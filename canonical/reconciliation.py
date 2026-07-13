from pydantic import BaseModel


class ReconciliationReport(BaseModel):
    source_records: int
    standardized_records: int
    validated_records: int
    duplicate_records: int
    golden_records: int
    rejected_records: int
