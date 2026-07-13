import re

from mdm.data_quality.interfaces import ValidationRule
from mdm.data_quality.models import RuleResult


class EmailRule(ValidationRule):
    """
    Validates email format.

    Examples:
        abc@gmail.com      ✅
        abc@yahoo.co.in    ✅
        abc@gmail          ❌
        abc.com            ❌
    """

    EMAIL_PATTERN = re.compile(
        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    )

    def validate(
        self,
        field_name: str,
        value,
        config: dict,
    ) -> RuleResult:

        if value is None:
            return RuleResult(passed=True)

        value = str(value).strip()

        if self.EMAIL_PATTERN.fullmatch(value):
            return RuleResult(passed=True)

        return RuleResult(
            passed=False,
            message="Invalid email address.",
            error_code="DQ201",
        )
