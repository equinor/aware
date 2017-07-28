#!/usr/bin/env python3

from flask import Flask, render_template, url_for
import requests
import json
import os

sensu_api = os.getenv('SENSU_API', "http://example.sensu-api.com:4567/events")
refresh_interval = os.getenv('REFRESH_INTERVAL', 15)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    response = requests.get(sensu_api)
    if response.ok:
        data = response.json()
        with open('result.json', 'w') as datafile:
            json.dump(data, datafile, sort_keys=True, indent=4)
        events = {}
        for event in data:
            id = event['id']
            events[id] = {}
            events[id]['client_name'] = event['client']['name']
            events[id]['check_name'] = event['check']['name']
            events[id]['status'] = event['check']['status']
            events[id]['output'] = event['check']['output']
            events[id]['silenced'] = event['silenced']
            events[id]['silenced_by'] = event['silenced_by']
        return render_template('index.html', events=events, refresh_interval=refresh_interval)
    else:
        response.raise_for_status()

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
