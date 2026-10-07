import json
import socket
import time
from pathlib import Path

from PIL import Image

FIXTURES_DIR = Path(__file__).parent / "fixtures"
IMAGE_DIR = Path(__file__).parent / "fixtures" / "images"


# ==========================
# RGB888 -> RGB565
# ==========================

def rgb888_to_rgb565(red, green, blue):
    return (
        ((red & 0xF8) << 8)
        | ((green & 0xFC) << 3)
        | (blue >> 3)
    )

# ==========================
# Bild in RGB565 umwandeln
# ==========================

def convert_to_rgb565(image_path, width, height):
    image = Image.open(image_path)

    image = image.convert("RGB")
    image = image.resize(
        (width, height),
        Image.Resampling.LANCZOS
    )

    rgb565_data = bytearray()

    for red, green, blue in image.getdata():
        pixel = rgb888_to_rgb565(red, green, blue)

        # ESP32 ist Little-Endian.
        rgb565_data.extend(pixel.to_bytes(2, "little"))

    return bytes(rgb565_data)


def load_image(filename, width, height):
    file_path = IMAGE_DIR / filename

    return convert_to_rgb565(
        file_path,
        width,
        height
    )


def load_json_fixture(filename):
    file_path = FIXTURES_DIR / filename

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
