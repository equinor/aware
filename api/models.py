from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class SeverityEnum(str, Enum):
    none = "none"
    unknown = "unknown"
    warning = "warning"
    critical = "critical"


class SourceEnum(str, Enum):
    prometheus = "prometheus"
    sensu = "sensu"
    url = "url"


class Event(BaseModel):
    alertname: str
    namespace: str
    severity: SeverityEnum
    message: str
    triggered: datetime
    logs: str
    source: SourceEnum
