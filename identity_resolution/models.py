from enum import Enum

from pydantic import BaseModel, Field


class MatchDecision(str, Enum):
    """
    Final decision after comparing two records.
    """

    MATCH = "MATCH"

    POSSIBLE_MATCH = "POSSIBLE_MATCH"

    NO_MATCH = "NO_MATCH"


class MatchEvidence(BaseModel):
    """
    Evidence produced by a single matching rule.
    """

    rule: str

    matched: bool

    score: float = 0

    confidence: float = 0

    reason: str | None = None


class IdentityMatchResult(BaseModel):
    """
    Final output produced by Identity Resolution Engine.
    """

    decision: MatchDecision

    total_score: float

    evidence: list[MatchEvidence] = Field(default_factory=list)


class IdentityCluster1(BaseModel):
    """
    Represents one real-world entity.
    """

    cluster_id: str

    records: list

    golden_record_id: str | None = None

from enum import Enum

class EntityType(str, Enum):
    CUSTOMER = "customer"
    SUPPLIER = "supplier"
    PRODUCT = "product"
    EMPLOYEE = "employee"


class IdentityCluster(BaseModel):
    """
    Represents a group of records
    belonging to the same real-world entity.
    """

    cluster_id: str

    entity_type: str

    records: list = Field(default_factory=list)

    golden_record_id: str | None = None
