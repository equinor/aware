from datetime import datetime
from typing import Dict, List

import requests

from requests import Response

from api.models import Event, SeverityEnum, SourceEnum


def convert_severity(status: int, silenced: List[Dict]) -> str:
    if silenced:
        return "none"
    if status == 1:
        return "warning"
    elif status == 2:
        return "critical"
    else:
        return "none"


def get_websites_events(url_list_file: str) -> List[Event]:
    events = []
    for url in url_list_file.splitlines():
        if "http://" not in url and "https://" not in url:
            url = f"https://{url}"
        try:
            response = None
            response: Response = requests.get(url, timeout=5, )
        except (requests.exceptions.ConnectionError) as request_error:
            events.append(Event(alertname=url, namespace="HealthCheck", severity=SeverityEnum.critical,
                          message=request_error.__class__.__name__, triggered=datetime.now(), logs=str(request_error),
                          source=SourceEnum.url))
            continue

        if 201 >= response.status_code >= 200:
            print(f"URL '{url}' had a positive response")
            continue

        event = Event(alertname=url, namespace="HealthCheck", severity=SeverityEnum.unknown,
                      message=response.status_code, triggered=datetime.now(), logs=response.text,
                      source=SourceEnum.url)

        if 400 > response.status_code > 201:
            event.severity = SeverityEnum.warning

        if response.status_code > 400:
            event.severity = SeverityEnum.critical

        events.append(event)

    return events
