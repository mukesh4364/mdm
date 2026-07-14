from identity_resolution.models import MatchDecision


class DecisionEngine:

    def __init__(self, config):

        self.config = config

    def decide(
        self,
        entity_type: str,
        score: float,
    ):

        entity_config = self.config.get(entity_type)

        if entity_config is None:

            raise ValueError(
                f"No configuration found for entity '{entity_type}'"
            )

        decision = entity_config["decision"]

        if score >= decision["match_score"]:
            return MatchDecision.MATCH

        if score >= decision["possible_match_score"]:
            return MatchDecision.POSSIBLE_MATCH

        return MatchDecision.NO_MATCH
