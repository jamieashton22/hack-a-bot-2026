from Radio import Transmitter, Receiver
from joystick import Joystick
import utime
# Fixed 5-byte address for testing
ADDRESS = b"team6"

tx = Transmitter(tx_address=ADDRESS)
js = Joystick(x_pin=28, y_pin=26, button_pin=22)
prev_direction = None
while True:
    direction = js.direction()
    if direction != prev_direction:
        message = direction.encode()
        success = tx.send_with_retry(message)
        print(f"Sent: {message} -> {success}")
        prev_direction = direction
    utime.sleep(0.01)