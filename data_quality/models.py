from pydantic import BaseModel, Field


class RuleResult(BaseModel):
    """
    Result returned by every validation rule.
    """

    passed: bool

    message: str | None = None

    severity: str = "ERROR"

    error_code: str | None = None


class ValidationError(BaseModel):
    """
    Validation error collected from failed rules.
    """

    field: str

    rule: str

    message: str

    severity: str = "ERROR"

    error_code: str | None = None


class ValidationResult(BaseModel):
    """
    Final validation result for one CustomerRecord.
    """

    passed: bool

    errors: list[ValidationError] = Field(default_factory=list)

    warnings: list[ValidationError] = Field(default_factory=list)
