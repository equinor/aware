import json
import time
from typing import Dict, List

from flask import abort, Flask, jsonify, request

from api.monitors.website_healthcheck import get_websites_events
from config import Config
from monitors.external import get_exported_events
from monitors.prometheus import get_prometheus_events
from monitors.sensu import get_sensu_events

app = Flask(__name__)


def get_raw_events() -> List[Dict]:
    events = []

    if Config.sensu_api:
        events += get_sensu_events()

    if Config.prometheus_api:
        events += get_prometheus_events()

    for external_url in Config.import_urls_list:
        events += get_exported_events(external_url)

    if Config.website_check_list:
        events += [e.dict() for e in get_websites_events(Config.website_check_list.splitlines())]

    return events


# Unprotected endpoint
@app.route('/api/events', methods=['GET'])
def events():
    events = get_raw_events()

    sorted_events = sorted(events, key=lambda event: event['triggered'], reverse=True)

    for e in sorted_events:
        if e["triggered"] == 0:
            e["triggered"] = "Never seen as 'OK'"
        else:
            e["triggered"] = time.strftime("%a, %d %H:%M", time.localtime(e["triggered"]))

    return jsonify(sorted_events)


# Protected endpoint
@app.route('/api/exports', methods=['GET'])
def exports():
    auth_header_value = request.headers.get("AUTHORIZATION")
    key = ""
    try:
        key = auth_header_value.split(" ")[1]
    except IndexError as error:
        print(f"Failed to get key from export request. ERROR: {error}")

    if key == Config.export_secret:
        events = get_raw_events()
        [event.update({"source": Config.deployment_name}) for event in events]
        return json.dumps(events)

    return abort(403)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=Config.flask_debug)
