
from machine import Pin
from utime import sleep
from joystick import Joystick
import time

# Create joystick instance (update pins if needed)
js = Joystick(x_pin=27, y_pin=26, button_pin=22)

pin = Pin("LED", Pin.OUT)

print("Joystick test starting...")

while True:
    direction = js.direction()
    pressed = js.pressed()

    print("Direction:", direction, "| Button:", pressed)

    time.sleep(0.2)

