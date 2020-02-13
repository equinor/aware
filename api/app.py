import time

from config import Config
from flask import Flask, jsonify, request, abort

from monitors.external import get_exported_events
from monitors.prometheus import get_prometheus_events
from monitors.sensu import get_sensu_events


app = Flask(__name__)

# Unprotected endpoint
@app.route('/api/events', methods=['GET'])
def events():
    events = []

    if Config.sensu_api:
        events += get_sensu_events()

    if Config.prometheus_api:
        events += get_prometheus_events()

    for external_url in Config.import_urls_list:
        events += get_exported_events(external_url)

    sorted_events = sorted(events, key=lambda event: event['triggered'], reverse=True)

    [e.update({"triggered": time.strftime("%a, %d %H:%M" ,time.localtime(e["triggered"]))}) for e in sorted_events]

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
        return events()

    return abort(403)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=Config.flask_debug)
