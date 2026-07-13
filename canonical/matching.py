from pydantic import BaseModel
from .enums import MatchStatus


class MatchScore(BaseModel):
    phone: float = 0
    email: float = 0
    name: float = 0
    address: float = 0
    total: float = 0


class MatchResult(BaseModel):
    left_record_id: str
    right_record_id: str
    score: MatchScore
    status: MatchStatus
