# tests/test_client.py

import json
import socket

class ESP32Client:

    def __init__(self, host, port, timeout=3):
        self.host = host
        self.port = port
        self.timeout = timeout

    def send_command(self, command):
        data = (json.dumps(command) + "\n").encode("utf-8")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(self.timeout)

            sock.connect((self.host, self.port))
            sock.sendall(data)

            response = sock.recv(4096)

        return json.loads(response.decode("utf-8"))