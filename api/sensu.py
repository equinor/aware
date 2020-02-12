import requests
from config import Config


def get_sensu_events():
    request = (requests.get(url=Config.sensu_api))