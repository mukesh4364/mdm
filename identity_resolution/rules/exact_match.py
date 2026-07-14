from identity_resolution.interfaces import MatchingRule
from identity_resolution.models import MatchEvidence
from identity_resolution.registry import MatchingRegistry
from identity_resolution.exceptions import ConfigurationError


@MatchingRegistry.register("exact")
class ExactFieldMatcher(MatchingRule):
    """
    Generic matcher for exact field comparison.
    """

    def match(
        self,
        left,
        right,
        config,
    ) -> MatchEvidence:

        field = config.get("field")

        if not field:
            raise ConfigurationError(
                "'exact' matcher requires a 'field' property.\n"
                "Example:\n"
                "- type: exact\n"
                "  field: customer_id\n"
                "  weight: 20"
            )

        left_value = getattr(left, field, None)
        right_value = getattr(right, field, None)

        if left_value is None or right_value is None:
            return MatchEvidence(
                rule=f"exact:{field}",
                matched=False,
                score=0,
                confidence=0,
                reason=f"{field} missing."
            )

        matched = left_value == right_value

        return MatchEvidence(
            rule=f"exact:{field}",
            matched=matched,
            score=config.get("weight", 0) if matched else 0,
            confidence=100 if matched else 0,
            reason=f"{field} matched" if matched else f"{field} mismatch",
        )
