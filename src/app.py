from config import Config
from flask import Flask, jsonify
from prometheus import get_prometheus_events

app = Flask(__name__)


@app.route('/api/prometheus', methods=['GET'])
def index():
    prometheus_object = get_prometheus_events()

    watchdog_alert = [alert for alert in prometheus_object['events'] if alert['alertname'] == 'Watchdog']
    prometheus_object['events'] = \
        [alert for alert in prometheus_object['events'] if not alert['alertname'] == 'Watchdog']

    if watchdog_alert:
        dead_mans_switch = False
    else:
        dead_mans_switch = True

    return jsonify(prometheus_object['events'])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=Config.flask_debug)
