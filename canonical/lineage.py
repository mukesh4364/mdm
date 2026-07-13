from datetime import datetime
from pydantic import BaseModel


class LineageRecord(BaseModel):
    golden_id: str
    source: str
    source_id: str
    attribute: str
    selected_value: str
    reason: str
    timestamp: datetime
