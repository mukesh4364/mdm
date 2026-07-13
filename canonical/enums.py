from enum import Enum


class SourceType(str, Enum):
    CRM = "CRM"
    CLAIMS = "CLAIMS"
    MOBILE = "MOBILE"
    EMPLOYER = "EMPLOYER"


class ValidationStatus(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    WARNING = "WARNING"


class PipelineStatus(str, Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    RUNNING = "RUNNING"


class MatchStatus(str, Enum):
    MATCH = "MATCH"
    POSSIBLE_MATCH = "POSSIBLE_MATCH"
    NO_MATCH = "NO_MATCH"
