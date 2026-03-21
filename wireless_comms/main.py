# Set to "SENDER" or "RECEIVER"
MODE = "SENDER"   # <-- change to "RECEIVER" for the other Pico

from Radio import Transmitter, Receiver
from machine import Pin
import utime

# Fixed 5-byte address for testing
ADDRESS = b"team6"

pin = Pin("LED", Pin.OUT)

if MODE.upper() == "SENDER":
    tx = Transmitter(tx_address=ADDRESS)
    print("Running as SENDER for 60 seconds")

    counter = 0
    start = utime.ticks_ms()
    duration = 60000   # 60 seconds

    while utime.ticks_diff(utime.ticks_ms(), start) < duration:
        message = f"Hello {counter}"
        success = tx.send_with_retry(message)
        print(f"Sent: {message} -> {success}")

        counter += 1
        pin.toggle()
        utime.sleep(1)

    print("Sender finished after 60 seconds")


# elif MODE.upper() == "RECEIVER":
#     rx = Receiver(rx_address=ADDRESS)
#     print("Running as RECEIVER. Press Ctrl+C to stop.")

#     try:
#         while True:
#             msg = rx.receive()
#             if msg:
#                 print("Received:", msg)
#             utime.sleep(0.05)
#     except KeyboardInterrupt:
#         print("Receiver stopped.")

# else:
#     raise ValueError("MODE must be either 'SENDER' or 'RECEIVER'")

