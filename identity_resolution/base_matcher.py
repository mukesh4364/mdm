from abc import ABC, abstractmethod

from identity_resolution.models import MatchEvidence


class BaseMatchingRule(ABC):

    @abstractmethod
    def match(self, left, right, config):
        pass

    def build_result(
        self,
        rule,
        similarity,
        threshold,
        weight,
    ):

        matched = similarity >= threshold

        return MatchEvidence(
            rule=rule,
            matched=matched,
            score=weight if matched else 0,
            confidence=round(similarity, 2),
            reason=f"Similarity={similarity:.2f}%"
        )
