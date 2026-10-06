import os

from dotenv import load_dotenv


load_dotenv()


ESP32_HOST = os.getenv("ESP32_HOST")
ESP32_PORT = int(os.getenv("ESP32_PORT", "8080"))
ESP32_TIMEOUT = int(os.getenv("ESP32_TIMEOUT", "3"))