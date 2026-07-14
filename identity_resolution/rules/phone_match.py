from identity_resolution.interfaces import MatchingRule
from identity_resolution.models import MatchEvidence
from identity_resolution.registry import MatchingRegistry


@MatchingRegistry.register("phone")
class PhoneMatcher(MatchingRule):

    def match(
        self,
        left,
        right,
        config,
    ) -> MatchEvidence:

        phone1 = left.phone
        phone2 = right.phone

        if not phone1 or not phone2:

            return MatchEvidence(
                rule="phone",
                matched=False,
                score=0,
                confidence=0,
                reason="Phone missing."
            )

        matched = phone1 == phone2

        return MatchEvidence(

            rule="phone",

            matched=matched,

            score=config["weight"] if matched else 0,

            confidence=100 if matched else 0,

            reason="Phone matched"
            if matched
            else "Phone mismatch",

        )
