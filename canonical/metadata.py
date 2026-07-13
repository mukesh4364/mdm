from pydantic import BaseModel


class RecordMetadata(BaseModel):
    '''
    Metadata travels with every record.
    '''
    source_file: str | None = None
    batch_id: str
    pipeline_version: str
    ingestion_time: str
    checksum: str | None = None
    processing_time_ms: float = 0
