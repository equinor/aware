from typing import Dict, List

import requests

from config import Config
from utils import dead_mans_switch


def get_exported_events(url) -> List[Dict]:
    headers = {"AUTHORIZATION": f"Key {Config.export_secret}"}
    try:
        request = (requests.get(url=url, headers=headers))
        if request.status_code == 404:
            msg = "ERROR: External url returned 404 status"
            print(msg)
            return dead_mans_switch("Imports", url, msg)
        data = request.json()
        return data
    except Exception as e:
        print(f"Fatal: Could not GET the from the external url {url}. Error: {e}")
        return dead_mans_switch("Imports", url, e)
