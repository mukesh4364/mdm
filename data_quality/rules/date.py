from datetime import datetime

from data_quality.interfaces import ValidationRule
from data_quality.models import RuleResult


class DateRule(ValidationRule):
    """
    Validates whether the value is a valid ISO-8601 date.

    Examples:
        2026-07-01      ✅
        2026-13-01      ❌
        01/07/2026      ❌
    """

    def validate(
        self,
        field_name: str,
        value,
        config: dict,
    ) -> RuleResult:

        if value is None:
            return RuleResult(passed=True)

        if isinstance(value, datetime):
            return RuleResult(passed=True)

        try:
            datetime.fromisoformat(str(value))
            return RuleResult(passed=True)

        except ValueError:
            return RuleResult(
                passed=False,
                message="Invalid ISO-8601 date.",
                error_code="DQ301",
            )
