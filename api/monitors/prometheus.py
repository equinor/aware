import requests

from config import Config
from utils import dead_mans_switch, get_path, local_to_epoch_time, truncate_string

ignore_alert_list = Config.ignore_alert_list


def get_prometheus_events():
    try:
        request = (requests.get(url=Config.prometheus_api))
        data = request.json()
    except Exception as e:
        print(f'Fatal: Could not GET prometheus API {Config.prometheus_api}. Error: {e}')
        return dead_mans_switch("Prometheus events", Config.prometheus_api, e)

    # data = json.loads(Config.mock_data)

    filtered = [alert for alert in data['data']['alerts']
                if alert['labels']['alertname'] not in ignore_alert_list]

    events = [{
        'alertname': get_path(event, 'labels', 'alertname'),
        'namespace': get_path(event, 'labels', 'namespace'),
        'severity': get_path(event, 'labels', 'severity'),
        'message': truncate_string(get_path(event, 'annotations', 'message')),
        'triggered': local_to_epoch_time(event['activeAt']),
        "source": "SDP-AKS"
    } for event in filtered]

    return events
