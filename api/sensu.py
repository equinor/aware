import json
from typing import List, Dict

import requests

from config import Config


def convert_severity(status) -> str:
    if status == 1:
        return "warning"
    elif status == 2:
        return "critical"
    else:
        return "none"


def get_sensu_events() -> List[Dict]:
    headers = {"AUTHORIZATION": f"Key {Config.sensu_key}"}
    try:
        request = (requests.get(url=Config.sensu_api, headers=headers))
        data = request.json()
    except Exception as e:
        print(f"Fatal: Could not GET Sensu API {Config.prometheus_api}. Error: {e}")
        return []

    #data = json.loads(Config.sensu_mock_data)

    not_passing_status = [check for check in data if check["check"]["state"] != "passing"]

    events = [{
        'alertname': event["check"]['metadata']['name'],
        'namespace': event["entity"]["metadata"]["name"],
        'severity': convert_severity(event["check"]["status"]),
        'message': event["check"]["output"],
        'triggered': int(event["check"]["issued"]),
        "source": "Sensu"
    } for event in not_passing_status]

    return events
