import unittest

from src.config import ESP32_HOST, ESP32_PORT, ESP32_TIMEOUT
from src.esp32_client import ESP32Client


class TestPing(unittest.TestCase):

    def setUp(self):
        self.client = ESP32Client(
            ESP32_HOST,
            ESP32_PORT,
            ESP32_TIMEOUT
        )

    def test_ping(self):

        command = {
            "requestId": "test-ping-001",
            "type": "command",
            "command": "ping"
        }

        response = self.client.send_command(command)

        self.assertEqual(response["type"], "response")
        self.assertEqual(response["command"], "ping")
        self.assertTrue(response["success"])
        self.assertEqual(response["result"], "pong")
        self.assertEqual(
            response["requestId"],
            command["requestId"]
        )


if __name__ == "__main__":
    unittest.main()