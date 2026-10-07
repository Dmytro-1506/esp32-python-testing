import unittest
import time
import json

from src.config import ESP32_HOST, ESP32_PORT, ESP32_TIMEOUT
from src.esp32_client import ESP32Client
from tests.helpers import load_json_fixture, load_image


class TestCommands(unittest.TestCase):

    def setUp(self):
        time.sleep(0.5)
        
        self.client = ESP32Client(
            ESP32_HOST,
            ESP32_PORT,
            ESP32_TIMEOUT
        )
    
    def assert_success_response(self, response, command):

        self.assertEqual(
            response["type"],
            "response"
        )

        self.assertEqual(
            response["command"],
            command["command"]
        )

        self.assertTrue(
            response["success"],
            response
        )

        self.assertEqual(
            response["requestId"],
            command["requestId"]
        )

    def test_ping(self):

        command = load_json_fixture(
            "commands/ping.json"
        )

        response = self.client.send_command(command)

        self.assert_success_response(
            response,
            command
        )

    def test_get_user_answer(self):

        command = load_json_fixture(
            "commands/get_user_answer.json"
        )

        response = self.client.send_command(command, 10)

        self.assert_success_response(
            response,
            command
        )

        self.assertIn("result", response)

        self.assertIn("button", response["result"])

        self.assertIn(
            response["result"]["button"],
            [1, 2, 3]
        )
        
    def test_get_status(self):

        command = load_json_fixture(
            "commands/get_status.json"
        )

        response = self.client.send_command(command)

        self.assert_success_response(
            response,
            command
        )
    
    def test_set_led(self):

        command = load_json_fixture(
            "commands/set_led.json"
        )

        response = self.client.send_command(command)

        self.assert_success_response(
            response,
            command
        )
    
    def test_set_led_blink(self):

        command = load_json_fixture(
            "commands/set_led_blink.json"
        )

        response = self.client.send_command(command)

        self.assert_success_response(
            response,
            command
        )
    
    def test_set_led_pulse(self):

        command = load_json_fixture(
            "commands/set_led_pulse.json"
        )

        response = self.client.send_command(command)

        self.assert_success_response(
            response,
            command
        )
    
    def test_show_text(self):

        command = load_json_fixture(
            "commands/show_text.json"
        )

        response = self.client.send_command(command)

        self.assert_success_response(
            response,
            command
        )
    
    def test_show_image(self):

        command = load_json_fixture(
            "commands/show_image.json"
        )
        
        width = command["parameters"]["width"]
        height = command["parameters"]["height"]
        
        image_data = load_image("Stefan_Schwope.jpg", width, height)
        
        response = self.client.send_image_command(
            command,
            image_data
        )

        self.assert_success_response(
            response,
            command
        )
    
    def test_clear_display(self):

        command = load_json_fixture(
            "commands/clear_display.json"
        )

        response = self.client.send_command(command)

        self.assert_success_response(
            response,
            command
        )
    
    def test_clear_display_area(self):

        command = load_json_fixture(
            "commands/clear_display_area.json"
        )

        response = self.client.send_command(command)

        self.assert_success_response(
            response,
            command
        )
    
    def test_play_sound(self):

        command = load_json_fixture(
            "commands/play_sound.json"
        )

        response = self.client.send_command(command)

        self.assert_success_response(
            response,
            command
        )
    
    def test_stop_sound(self):

        command = load_json_fixture(
            "commands/stop_sound.json"
        )

        response = self.client.send_command(command)

        self.assert_success_response(
            response,
            command
        )
    
    def test_reset(self):

        command = load_json_fixture(
            "commands/reset.json"
        )

        response = self.client.send_command(command)

        self.assert_success_response(
            response,
            command
        )
    



if __name__ == "__main__":
    unittest.main()