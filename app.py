#!/usr/bin/env python3

from flask import Flask, render_template, url_for
import requests
import json

url = 'http://<some_url_to_sensu_api>:4567/events'


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    response = requests.get(url)
    if response.ok:
        data = response.json()
#        with open('result.json', 'w') as datafile:
#            json.dump(data, datafile, sort_keys=True, indent=4)
        events = {}
        for event in data:
            id = event['id']
            events[id] = {}
            events[id]['client_name'] = event['client']['name']
            events[id]['check_name'] = event['check']['name']
            events[id]['status'] = event['check']['status']
            events[id]['silenced'] = event['silenced']
            events[id]['silenced_by'] = event['silenced_by']
        return render_template('index.html', events=events)
    else:
        response.raise_for_status()

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
