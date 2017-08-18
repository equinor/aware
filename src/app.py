#!/usr/bin/env python3

from flask import Flask, render_template, url_for
import requests
import json
import os
import re

sensu_api = os.getenv('SENSU_API', "")
debug = os.getenv('DEBUG', False)
sensu_apis = sensu_api.split(",")
refresh_interval = os.getenv('REFRESH_INTERVAL', 15)

app = Flask(__name__)

if not sensu_api:
    print("SENSU_API unset. Aborting")
    sys.exit()

@app.route('/', methods=['GET'])
def index():

    i = 0
    events = {}
    for api in sensu_apis:
        api_failed = False
        try:
            response = requests.get(api)
            if response.ok:
                data = response.json()
                for event in data:
                    events[i] = {}
                    events[i]['client_name'] = event['client']['name']
                    events[i]['check_name'] = event['check']['name']
                    if event['check']['status'] == 2:
                        events[i]['status'] = "critical"
                    elif event['check']['status'] == 1:
                        events[i]['status'] = "warning"
                    elif event['check']['status'] > 2:
                        events[i]['status'] = "unknown"
                    else:
                        events[i]['status'] = "ok"
                    events[i]['output'] = event['check']['output']
                    if event['silenced']:
                        events[i]['silenced'] = "Yes"
                    else:
                        events[i]['silenced'] = "No"
                    events[i]['silenced_by'] = event['silenced_by']
                    i = i + 1
            else:
                api_failed = True
        except requests.exceptions.RequestException:
            api_failed = True
        if api_failed:
            events[i] = {}
            events[i]['client_name'] = api.split('/')[2]
            events[i]['check_name'] = 'Sensu API'
            events[i]['status'] = "critical"
            events[i]['output'] = "Unable to connect to Sensu API: %s" % api
            events[i]['silenced'] = 'N/A'
            events[i]['silenced_by'] = 'N/A'
            i = i + 1
        for event in events:
            if events[event]['status'] == "critical" and events[event].silenced != "Yes":
                background_color_class = "background_critical"
                break
            elif events[event]['status'] == "warning" and events[event].silenced != "Yes":
                background_color_class = "background_warning"
                break
            elif events[event]['status'] == "unknown" and events[event].silenced != "Yes":
                background_color_class = "background_unknown"
                break
            else:
                background_color_class = "background_ok"
                break
    return render_template('index.html',
                           events=events,
                           refresh_interval=refresh_interval,
                           sensu_apis=sensu_apis,
                           background_color_class=background_color_class)


if __name__ == '__main__':
    app.debug = debug
    app.run(host="0.0.0.0", port=5000)
