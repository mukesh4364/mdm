from identity_resolution.interfaces import MatchingRule
from identity_resolution.models import MatchEvidence
from identity_resolution.registry import MatchingRegistry


@MatchingRegistry.register("email")
class EmailMatcher(MatchingRule):

    def match(
        self,
        left,
        right,
        config,
    ) -> MatchEvidence:

        email1 = left.email
        email2 = right.email

        if not email1 or not email2:

            return MatchEvidence(
                rule="email",
                matched=False,
                score=0,
                confidence=0,
                reason="Email missing."
            )

        matched = email1.lower() == email2.lower()

        return MatchEvidence(

            rule="email",

            matched=matched,

            score=config["weight"] if matched else 0,

            confidence=100 if matched else 0,

            reason="Email matched"
            if matched
            else "Email mismatch",

        )
