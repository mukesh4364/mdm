from typing import Type

from identity_resolution.interfaces import MatchingRule


class MatchingRegistry:
    """
    Global registry for all matching rules.
    """

    _registry: dict[str, Type[MatchingRule]] = {}

    @classmethod
    def register(cls, name: str):
        """
        Decorator used by matching rules.
        """

        def decorator(rule_class):

            cls._registry[name] = rule_class

            return rule_class

        return decorator

    @classmethod
    def get(cls, name: str) -> MatchingRule:

        if name not in cls._registry:

            raise ValueError(
                f"Unknown matching rule: {name}"
            )

        return cls._registry[name]()

    @classmethod
    def available_rules(cls):

        return list(cls._registry.keys())
