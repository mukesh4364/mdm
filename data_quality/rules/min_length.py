from mdm.data_quality.interfaces import ValidationRule
from mdm.data_quality.models import RuleResult


class MinLengthRule(ValidationRule):
    """
    Validates minimum string length.

    YAML Example

    rules:
      - type: min_length
        value: 3
    """

    def validate(
        self,
        field_name: str,
        value,
        config: dict,
    ) -> RuleResult:

        if value is None:
            return RuleResult(passed=True)

        value = str(value)

        minimum = config.get("value", 0)

        if len(value) >= minimum:
            return RuleResult(passed=True)

        return RuleResult(
            passed=False,
            message=f"Minimum length should be {minimum}.",
            error_code="DQ401",
        )
