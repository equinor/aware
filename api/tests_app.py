import json
import unittest
from unittest.mock import patch

from app import events
from config import Config


class TestApp(unittest.TestCase):
    @patch("app.Config")
    @patch("monitors.sensu.requests.get")
    @patch("monitors.prometheus.requests.get")
    def test_events(self, prometheus_get, sensu_get, mock_config):
        mock_config.sensu_api = "sensu"
        mock_config.prometheus_api = "prometheus"
        sensu_get.return_value.json.return_value = json.loads(Config.sensu_mock_data)
        prometheus_get.return_value.json.return_value = json.loads(Config.mockdata2)
        result = events()
        print(123)
