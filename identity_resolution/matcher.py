from identity_resolution.registry import MatchingRegistry


class Matcher:
    """
    Executes all configured matching rules
    for the given entity.
    """

    def __init__(self, config):

        self.config = config

    def match(
        self,
        entity_type: str,
        left,
        right,
    ):

        evidences = []

        entity_config = self.config.get(entity_type)

        if entity_config is None:

            raise ValueError(
                f"No configuration found for entity '{entity_type}'"
            )

        rules = entity_config.get(
            "matching_rules",
            [],
        )

        for rule_config in rules:

            matcher = MatchingRegistry.get(
                rule_config["type"]
            )

            evidence = matcher.match(
                left,
                right,
                rule_config,
            )

            evidences.append(evidence)

        return evidences
