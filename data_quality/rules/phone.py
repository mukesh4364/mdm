from mdm.data_quality.interfaces import ValidationRule
from mdm.data_quality.models import RuleResult
import re

class PhoneRule(ValidationRule):

    def validate(
        self,
        field_name,
        value,
        config,
    ) -> RuleResult:

        if value is None:
            return RuleResult(passed=True)

        if re.fullmatch(r"\d{10}", value):
            return RuleResult(passed=True)

        return RuleResult(
            passed=False,
            message="Phone must contain exactly 10 digits.",
            error_code="DQ101",
        )
