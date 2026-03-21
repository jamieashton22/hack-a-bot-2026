# Stan
# OLED output for when an object is detected
from machine import Pin, I2C
import ssd1306


# Setup display (I2C address 0x3C)
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000) # Adjust pins to match your wiring
display = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

bObj_Detected = True

if bObj_Detected == True:
    display.fill(0)  # Clear display
    # id: 0 - text at (0, 0)
    display.text("OBJECT DETECTED", 0, 0)
    # id: 1 - text at (6, 8)
    display.text("OBJECT DETECTED", 6, 8)
    # id: 2 - text at (12, 16)
    display.text("OBJECT DETECTED", 12, 16)
    # id: 3 - text at (18, 24)
    display.text("OBJECT DETECTED", 18, 24)
    # id: 4 - text at (24, 32)
    display.text("OBJECT DETECTED", 24, 32)
    # id: 5 - text at (30, 40)
    display.text("OBJECT DETECTED", 30, 40)
    # id: 6 - text at (36, 48)
    display.text("OBJECT DETECTED", 36, 48)
    # id: 7 - text at (42, 56)
    display.text("OBJECT DETECTED", 42, 56)
    display.show()  # Push to display

else:
    display.fill(0)  # Clear display
    # id: 0 - text at (52, 28)
    display.text("IDLE", 52, 28)
    display.show()  # Push to display