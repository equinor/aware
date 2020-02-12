import requests
from datetime import datetime

from utils import get_path
from config import Config
import json

ignore_alert_list = Config.ignore_alert_list

def local_to_epoch_time(local_string) -> int:
    local_string = local_string.split(".", 1)[0]
    utc_dt = datetime.strptime(local_string, '%Y-%m-%dT%H:%M:%S')
    timestamp = (utc_dt - datetime(1970, 1, 1)).total_seconds()
    return int(timestamp)

def get_prometheus_events():
    try:
        request = (requests.get(url=Config.prometheus_api))
        data = request.json()
    except Exception as e:
        print(
            f'Fatal: Could not GET prometheus API {Config.prometheus_api}. Error: {e}')

    data = json.loads(Config.mock_data)

    filtered = [alert for alert in data['data']['alerts']
                if alert['labels']['alertname'] not in ignore_alert_list
                or alert['labels']['alertname'] != "Watchdog"]

    events = [{
        'alertname': get_path(event, 'labels', 'alertname'),
        'namespace': get_path(event, 'labels', 'namespace'),
        'severity': get_path(event, 'labels', 'severity'),
        'message': get_path(event, 'annotations', 'message'),
        'triggered': local_to_epoch_time(event['activeAt']),
        "source": "SDP-AKS"
    } for event in filtered]

    return events
