class IdentityResolutionError(Exception):
    """Base exception for Identity Resolution."""
    pass


class ConfigurationError(IdentityResolutionError):
    """Raised when identity resolution configuration is invalid."""
    pass
