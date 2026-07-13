from pydantic import BaseModel
from .enums import ValidationStatus


class RuleResult(BaseModel):
    rule_id: str
    field: str
    status: ValidationStatus
    message: str


class ValidationResult(BaseModel):
    passed: bool
    results: list[RuleResult]
    errors: list[str]
    warnings: list[str]
