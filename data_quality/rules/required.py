from mdm.data_quality.interfaces import ValidationRule
from mdm.data_quality.models import RuleResult


class RequiredRule(ValidationRule):

    def validate(
        self,
        field_name,
        value,
        config,
    ) -> RuleResult:

        if value is None:
            return RuleResult(
                passed=False,
                message="Value is mandatory.",
                error_code="DQ001",
            )

        if isinstance(value, str) and value.strip() == "":
            return RuleResult(
                passed=False,
                message="Value is mandatory.",
                error_code="DQ001",
            )

        return RuleResult(passed=True)
