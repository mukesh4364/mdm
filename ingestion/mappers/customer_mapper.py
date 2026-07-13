from datetime import datetime

from canonical import CustomerRecord, RecordMetadata
from canonical.enums import SourceType


class CustomerMapper:
    """Converts source-specific dictionaries into CustomerRecord."""

    @staticmethod
    def from_crm(row: dict) -> CustomerRecord:
        return CustomerRecord(
            source=SourceType.CRM,
            source_id=str(row["customer_id"]),
            full_name=row["name"],
            phone=row.get("phone"),
            email=row.get("email"),
            address=row.get("address"),
            city=row.get("city"),
            last_updated=datetime.fromisoformat(row["last_updated"]),
            metadata=RecordMetadata(
                batch_id="batch-001",
                pipeline_version="1.0",
                ingestion_time=datetime.utcnow().isoformat(),
                source_file="crm.csv",
            ),
        )
