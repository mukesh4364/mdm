
'''
This gives us meaningful, domain-specific errors instead of generic exceptions.
'''
class IngestionError(Exception):
    """Base exception for ingestion."""


class InvalidSchemaError(IngestionError):
    """Raised when source schema is invalid."""


class SourceNotFoundError(IngestionError):
    """Raised when the configured source is unavailable."""
