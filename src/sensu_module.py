import os
import sys
import requests
from config import Config

sensu_apis = Config.sensu_apis

if not sensu_apis:
    print("SENSU_API unset. Aborting")
    sys.exit()

# TODO: Fix all of this
def get_sensu_events():
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
        unsilenced_critical_found = False
        unsilenced_warning_found = False
        unsilenced_unknown_found = False
        for event in events:
            if events[event]['status'] == "critical" and events[event]['silenced'] != "Yes":
                unsilenced_critical_found = True
            elif events[event]['status'] == "warning" and events[event]['silenced'] != "Yes":
                unsilenced_warning_found = True
            elif events[event]['status'] == "unknown" and events[event]['silenced'] != "Yes":
                unsilenced_unknown_found = True
        if unsilenced_critical_found:
            background_color_class = "background_critical"
        elif unsilenced_warning_found:
            background_color_class = "background_warning"
        elif unsilenced_unknown_found:
            background_color_class = "background_unknown"
        else:
            background_color_class = "background_ok"
