from abc import ABC
from abc import abstractmethod

from identity_resolution.models import MatchEvidence


class MatchingRule(ABC):
    """
    Base interface for every matching algorithm.
    """

    @abstractmethod
    def match(
        self,
        left,
        right,
        config,
    ) -> MatchEvidence:
        """
        Compare two records.

        Returns MatchEvidence.
        """

        pass
