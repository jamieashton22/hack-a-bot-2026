# Set to "SENDER" or "RECEIVER"
MODE = "RECEIVER"   # <-- change to "RECEIVER" for the other Pico

from Radio import Transmitter, Receiver
import utime

# Fixed 5-byte address for testing
ADDRESS = b"team6"


if MODE.upper() == "SENDER":
    tx = Transmitter(tx_address=ADDRESS)
    print("Running as SENDER. Press Ctrl+C to stop.")
    
    counter = 0
    try:
        while True:
            message = f"Hello {counter}"
            success = tx.send_with_retry(message)
            print(f"Sent: {message} -> {success}")
            counter += 1
            utime.sleep(1)
    except KeyboardInterrupt:
        print("Sender stopped.")


elif MODE.upper() == "RECEIVER":
    rx = Receiver(rx_address=ADDRESS)
    print("Running as RECEIVER. Press Ctrl+C to stop.")

    try:
        while True:
            msg = rx.receive()
            if msg:
                print("Received:", msg)
            utime.sleep(0.05)
    except KeyboardInterrupt:
        print("Receiver stopped.")

else:
    raise ValueError("MODE must be either 'SENDER' or 'RECEIVER'")

