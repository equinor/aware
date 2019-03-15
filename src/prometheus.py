import requests

from config import Config

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


def get_prometheus_events():
    try:
        request = (requests.get(url=Config.prometheus_api))
    except Exception as e:
        print(f'Could not GET prometheus API {Config.prometheus_api}. Error: {e}')
    data = request.json()
    # data = json.loads(Config.mock_data)
    filtered = [alert for alert in data['data']['alerts'] if alert['labels']['alertname'] not in ignore_alert_list]

    events = [{
        'client_name': get_path(event, 'labels', 'alertname'),
        'check_name': get_path(event, 'labels', 'namespace'),
        'status': get_path(event, 'labels', 'severity'),
        'output': get_path(event, 'annotations', 'message'),
        'silenced': event['activeAt'].split('.')[0],
    } for event in filtered]

    most_sever_alert = 'ok'
    for event in events:
        severity = event['status']
        if most_sever_alert == 'ok':
            most_sever_alert = severity
        elif most_sever_alert == 'warning' and severity == 'critical':
            most_sever_alert = severity

    return {'most_sever': most_sever_alert, 'events': events}
