import re

import requests

from config import Config

regex = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')


def strip_ansi_escape(text: str) -> str:
    new_text = regex.sub('', text)
    return new_text


def get_container_logs(instance: str) -> [str]:
    parameters = {
        "query": f"{{instance=\"{instance}\"}}",
        "limit": 20,
        "direction": "backward"
    }
    try:
        request = requests.get(url=Config.loki_api, params=parameters)
        # request = requests.get(url=Config.loki_api, params=parameters, auth=HTTPBasicAuth('sdpteam', Config.loki_passwd))
        data = request.json()
    except Exception as e:
        print(f'Fatal: Could not GET loki API {Config.loki_api}. Error: {e}')
        return ["ERROR: Failed to fetch logs..."]

    if result := data["data"]["result"]:
        return [
            strip_ansi_escape(line[1])
            for line in result[0]["values"]
        ]
    else:
        return [f"No logs for instance {instance} within the time frame..."]
