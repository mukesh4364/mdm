from abc import ABC, abstractmethod

from mdm.data_quality.models import RuleResult


class ValidationRule(ABC):

    @abstractmethod
    def validate(
        self,
        field_name,
        value,
        config,
    ) -> RuleResult:
        pass
