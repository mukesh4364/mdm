from abc import ABC, abstractmethod


class Standardizer(ABC):

    @abstractmethod
    def standardize(self, value):
        """Return the standardized value."""
        raise NotImplementedError
