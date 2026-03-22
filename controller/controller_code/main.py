from Radio import Transmitter, Receiver
from joystick import Joystick
from OLED import OLEDDisplay
import utime
# Fixed 5-byte address for testing
ADDRESS = b"team6"

tx = Transmitter(tx_address=ADDRESS)
js_left = Joystick(x_pin=28, y_pin=26, button_pin=22)
js_right = Joystick(x_pin = None, y_pin = 27, button_pin=21, side= "RIGHT")
oled = OLEDDisplay()
prev_direction = None
prev_updown = None

while True:

    direction = js_left.direction()
    updown = js_right.direction()

    if direction != prev_direction:
        message = direction.encode()
        success = tx.send_with_retry(message)
        print(f"Sent: {message} -> {success}")
        prev_direction = direction
    utime.sleep(0.01)

    if updown != prev_updown:
        message = updown.encode()
        success = tx.send_with_retry(message)
        print(f"Sent: {message} -> {success}")
        prev_updown = updown
    utime.sleep(0.01)

    # TEMP HARDCODED DISTANCE
    # add: receiving distance from ultrasound sensor 

    distance = 14.5
    oled.main_operation(direction, distance)
    utime.sleep(0.2)
