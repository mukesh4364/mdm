from datetime import datetime
from uuid import uuid4
from pydantic import BaseModel, Field


class BaseEntity(BaseModel):
    '''
    every entity will automatically get id and timestamp
    '''

    id: str = Field(default_factory=lambda: str(uuid4()))
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
