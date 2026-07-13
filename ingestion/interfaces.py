from abc import ABC, abstractmethod
from canonical import CustomerRecord


class SourceConnector(ABC):
    """
    Abstract base class for all ingestion connectors.
    Because every connector—CSV, JSON, API, Database, Kafka—must implement the same contract.
    """

    @abstractmethod
    def read(self) -> list[CustomerRecord]:
        """Read data from the source and return canonical customer records."""
        raise NotImplementedError
