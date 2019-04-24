from datetime import datetime
import requests
from config import Config
# import json

ignore_alert_list = Config.ignore_alert_list


def get_path(event, first_key, *keys):
    value = event.get(first_key, {})
    if keys is None:
        return value
    for key in keys:
        if key in value:
            value = value.get(key, {})
        else:
            return None
    return value


def find_most_sever_event(events):
    events = [event for event in events if event['alertname'] != 'Watchdog']
    most_sever_alert = 'ok'
    for event in events:
        severity = event['severity']
        if most_sever_alert == 'ok':
            most_sever_alert = severity
        elif most_sever_alert == 'none' and (severity == 'warning' or severity == 'critical'):
            most_sever_alert = severity
        elif most_sever_alert == 'warning' and severity == 'critical':
            most_sever_alert = severity
    return most_sever_alert


def get_prometheus_events():
    try:
        request = (requests.get(url=Config.prometheus_api))
        data = request.json()
    except Exception as e:
        print(f'Fatal: Could not GET prometheus API {Config.prometheus_api}. Error: {e}')

    # data = json.loads(Config.mockdata2)

    filtered = [alert for alert in data['data']['alerts'] if alert['labels']['alertname'] not in ignore_alert_list]

    events = [{
        'alertname': get_path(event, 'labels', 'alertname'),
        'namespace': get_path(event, 'labels', 'namespace'),
        'severity': get_path(event, 'labels', 'severity'),
        'message': get_path(event, 'annotations', 'message'),
        'triggered': event['activeAt'].replace('Z', '').split('.')[0],
    } for event in filtered]

    sorted_events = sorted(events,
                           key=lambda event: datetime.strptime(event['triggered'], '%Y-%m-%dT%H:%M:%S').timestamp(),
                           reverse=True)

    return {'most_sever': find_most_sever_event(events), 'events': sorted_events}
