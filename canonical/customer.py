from datetime import datetime
from pydantic import EmailStr
from .base import BaseEntity
from .enums import SourceType
from .metadata import RecordMetadata
from pydantic import field_validator

class CustomerRecord(BaseEntity):
    '''
    CustomerRecord is now completely source independent.
    '''
    source: SourceType
    source_id: str
    full_name: str
    phone: str | None = None
    email: EmailStr | None = None
    address: str | None = None
    city: str | None = None
    state: str | None = None
    country: str = "India"
    postal_code: str | None = None
    last_updated: datetime
    metadata: RecordMetadata

    @field_validator("phone", mode="before")
    @classmethod
    def normalize_phone(cls, value):
        print(f"Validator received: {value} ({type(value)})")

        if value is None:
            return None
        if isinstance(value, float):
            return str(int(value))
        return str(value)
