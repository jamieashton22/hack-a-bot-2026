# Stan
# OLED output for when an object is detected

from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont

# Setup display (I2C address 0x3C)
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, width=128, height=64)

# Draw shapes
with canvas(device) as draw:
    # id: 0 - text at (0, 0)
    draw.text((0,  0),  "OBJECT DETECTED", fill="white")
    # id: 1 - text at (6, 8)
    draw.text((6,  8),  "OBJECT DETECTED", fill="white")
    # id: 2 - text at (12, 16)
    draw.text((12, 16), "OBJECT DETECTED", fill="white")
    # id: 3 - text at (18, 24)
    draw.text((18, 24), "OBJECT DETECTED", fill="white")
    # id: 4 - text at (24, 32)
    draw.text((24, 32), "OBJECT DETECTED", fill="white")
    # id: 5 - text at (30, 40)
    draw.text((30, 40), "OBJECT DETECTED", fill="white")
    # id: 6 - text at (36, 48)
    draw.text((36, 48), "OBJECT DETECTED", fill="white")
    # id: 7 - text at (42, 56)
    draw.text((42, 56), "OBJECT DETECTED", fill="white")

# Keep display on
input("Press Enter to exit...")