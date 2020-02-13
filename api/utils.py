import time
from datetime import datetime
from typing import List, Dict


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


def dead_mans_switch(name, url, error) -> List[Dict]:
    return [{
            'alertname': f"Fetch {name} failed",
            'namespace': "Aware",
            'severity': "critical",
            'message': f"Failed to fetch data from {url}. {error}",
            'triggered': time.time(),
            "source": "Aware-API"
        }]


def local_to_epoch_time(local_string) -> int:
    local_string = local_string.split(".", 1)[0]
    utc_dt = datetime.strptime(local_string, '%Y-%m-%dT%H:%M:%S')
    timestamp = (utc_dt - datetime(1970, 1, 1)).total_seconds()
    return int(timestamp)

def truncate_string(string, length = 120) -> str:
    if not string:
        return ""
    return (string[:length] + '...') if len(string) > length else string