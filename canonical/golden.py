from datetime import datetime
from pydantic import BaseModel, EmailStr


class GoldenRecord(BaseModel):
    golden_id: str
    full_name: str
    phone: str | None = None
    email: EmailStr | None = None
    address: str | None = None
    confidence: float
    sources: list[str]
    created_at: datetime
