from data_quality.models import (
    RuleResult,
    ValidationError,
    ValidationResult,
)


class DataQualityEngine:
    """
    Executes configured data quality rules on a CustomerRecord.

    Responsibilities:
    1. Read validation rules from configuration.
    2. Execute rules using the RuleRegistry.
    3. Collect validation errors and warnings.
    4. Return ValidationResult.
    """

    def __init__(self, config: dict, registry):
        self.config = config
        self.registry = registry

    def validate(self, customer) -> ValidationResult:
        """
        Validate a single CustomerRecord.
        """

        errors: list[ValidationError] = []
        warnings: list[ValidationError] = []

        customer_rules = self.config.get("customer", {})
        print("customer rule")
        print(customer_rules)

        for field_name, field_config in customer_rules.items():

            value = getattr(customer, field_name, None)
            print(field_name)
            print(field_config)
            print(value)

            for rule_config in field_config.get("rules", []):

                rule_name = rule_config["type"]
                print(rule_name)

                rule = self.registry.get(rule_name)
                print(rule)

                rule_result: RuleResult = rule.validate(
                    field_name=field_name,
                    value=value,
                    config=rule_config,
                )
                print(rule_result)

                if rule_result.passed:
                    continue

                validation_error = ValidationError(
                    field=field_name,
                    rule=rule_name,
                    message=rule_config.get(
                        "message",
                        rule_result.message,
                    ),
                    severity=rule_config.get(
                        "severity",
                        rule_result.severity,
                    ),
                    error_code=rule_config.get(
                        "error_code",
                        rule_result.error_code,
                    ),
                )

                if validation_error.severity == "WARNING":
                    warnings.append(validation_error)
                else:
                    errors.append(validation_error)

        return ValidationResult(
            passed=len(errors) == 0,
            errors=errors,
            warnings=warnings,
        )
