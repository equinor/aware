# Sensu Dashboard

The purpose of this dashboard is to have it be more alarming and visual compared to e.g. Uchiwa. You would typically set this dashboard up on a team-monitor and in the case of an event, get everyones attention, and then inspect further in another dashboard with more features.

## Demo

In the case of events:
![alt text](events.png)
The background change color to the most severe event.

When there are no events:
![alt text](noevents.png)

## Usage

The easiest way to test and/or use this dashboard is with Docker. Edit docker-compose.yaml to configure the following settings:

* REFRESH_INTERVAL
How often the html page should reload and poll the API.
* SENSU_API
The full path to some Sensu API or multiple APIs in a comma separated list.

Start the application with docker-compose
```
docker-compose up -d
```

