from identity_resolution.base_matcher import BaseMatchingRule
from identity_resolution.registry import MatchingRegistry
from identity_resolution.similarity import Similarity
from identity_resolution.exceptions import ConfigurationError


@MatchingRegistry.register("fuzzy_name")
class FuzzyNameMatcher(BaseMatchingRule):

    def match(self, left, right, config):

        threshold = config.get("threshold")

        if threshold is None:
            raise ConfigurationError(
                "'fuzzy_name' matcher requires 'threshold'.\n"
                "Example:\n"
                "- type: fuzzy_name\n"
                "  weight: 20\n"
                "  threshold: 85"
            )

        weight = config.get("weight", 0)

        similarity = Similarity.ratio(
            left.full_name,
            right.full_name,
        )

        return self.build_result(
            rule="fuzzy_name",
            similarity=similarity,
            threshold=threshold,
            weight=weight,
        )
