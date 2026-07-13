from datetime import datetime
from pydantic import BaseModel
from .enums import PipelineStatus


class PipelineContext(BaseModel):
    pipeline_id: str
    batch_id: str
    started_at: datetime
    status: PipelineStatus
    records_processed: int = 0
