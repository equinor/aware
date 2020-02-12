import json
from typing import List, Dict

import requests

from utils import get_path
from config import Config

def convert_severity(state) -> str:
    if state == "0":
        return "ok"
    elif state == "2":
        return "warning"
    elif state == "1":
        return "critical"
    else:
        return "none"

def get_sensu_events() -> List[Dict]:
    headers = {"AUTHENTICATION": f"Key {Config.sensu_key}"}
    try:
        request = (requests.get(url=Config.sensu_api, headers=headers))
        data = request.json()
    except Exception as e:
        print(f"Fatal: Could not GET Sensu API {Config.prometheus_api}. Error: {e}")

    data = json.loads(Config.sensu_mock_data)

    not_passing_status = [check for check in data if check["check"]["state"] != "passing"]

    events = [{
        'alertname': get_path(event, "check", 'metadata', 'name'),
        'namespace': get_path(event, "entity", "metadata", "name"),
        'severity': convert_severity(get_path(event, "check", "state")),
        'message': get_path(event, "check", "output"),
        'triggered': int(get_path(event, "check", "issued")),
        "source": "Sensu"
    } for event in not_passing_status]

    return events
