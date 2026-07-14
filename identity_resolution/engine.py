from identity_resolution.matcher import Matcher
from identity_resolution.scorer import MatchScorer
from identity_resolution.decision import DecisionEngine
from identity_resolution.registry import MatchingRegistry
from identity_resolution.models import IdentityMatchResult
from identity_resolution.exceptions import ConfigurationError

# Import all rules so they register themselves
import identity_resolution.rules


class IdentityResolutionEngine:
    """
    Orchestrates the complete Identity Resolution workflow.
    """

    def __init__(self, config: dict):

        self.config = config

        # Validate configuration before creating components
        self._validate_configuration()

        self.matcher = Matcher(config)
        self.scorer = MatchScorer()
        self.decision_engine = DecisionEngine(config)

    def _validate_configuration(self):
        """
        Validate all configured entities and matching rules.

        This ensures the application fails during startup
        instead of failing at runtime.
        """

        available_rules = set(
            MatchingRegistry.available_rules()
        )

        for entity_name, entity_config in self.config.items():

            matching_rules = entity_config.get(
                "matching_rules",
                [],
            )

            for rule in matching_rules:

                rule_name = rule["type"]

                if rule_name not in available_rules:

                    raise ConfigurationError(
                        f"Entity '{entity_name}' uses "
                        f"unknown matching rule '{rule_name}'.\n\n"
                        f"Available rules: "
                        f"{sorted(available_rules)}"
                    )

    def resolve(
        self,
        entity_type: str,
        left,
        right,
    ):

        evidences = self.matcher.match(
            entity_type=entity_type,
            left=left,
            right=right,
        )

        total_score = self.scorer.score(
            evidences
        )

        decision = self.decision_engine.decide(
            entity_type=entity_type,
            score=total_score,
        )

        return IdentityMatchResult(
            decision=decision,
            total_score=total_score,
            evidence=evidences,
        )
