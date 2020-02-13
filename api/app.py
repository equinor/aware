import time

from config import Config
from flask import Flask, jsonify
from prometheus import get_prometheus_events
from sensu import get_sensu_events


app = Flask(__name__)


@app.route('/api/events', methods=['GET'])
def events():
    events = []

    if Config.sensu_api:
        events += get_sensu_events()

    if Config.prometheus_api:
        events += get_prometheus_events()

    sorted_events = sorted(events, key=lambda event: event['triggered'], reverse=True)

    [e.update({"triggered": time.strftime("%a, %d %H:%M" ,time.localtime(e["triggered"]))}) for e in sorted_events]

    return jsonify(sorted_events)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=Config.flask_debug)
