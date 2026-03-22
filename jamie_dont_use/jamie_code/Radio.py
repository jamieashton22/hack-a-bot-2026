from machine import Pin, SPI
from nrf24l01 import NRF24L01
import utime

class RadioBase:
    def __init__(self,
                 spi_id=0,
                 sck=6, mosi=7, miso=4,
                 csn_pin=14, ce_pin=17,
                 channel=46,
                 payload_size=16):

        self.spi = SPI(
            spi_id,
            baudrate=4000000,
            polarity=0,
            phase=0,
            sck=Pin(sck),
            mosi=Pin(mosi),
            miso=Pin(miso)
        )

        # Control pins
        self.csn = Pin(csn_pin, Pin.OUT)
        self.ce = Pin(ce_pin, Pin.OUT)

        # Create NRF object 
        self.nrf = NRF24L01(
            self.spi,
            self.csn,
            self.ce,
            channel=channel,
            payload_size=payload_size
        )

        self.payload_size = payload_size

    def set_channel(self, ch):
        self.nrf.set_channel(ch)

    def set_power(self, power, speed):
        self.nrf.set_power_speed(power, speed)



class Transmitter(RadioBase):
    def __init__(self, tx_address=b"1Node", **kwargs):
        super().__init__(**kwargs)

        if len(tx_address) != 5:
            raise ValueError("Address must be 5 bytes")

        self.tx_address = tx_address

        self.nrf.open_tx_pipe(self.tx_address)
        self.nrf.stop_listening()

    def send(self, data):
        if isinstance(data, str):
            data = data.encode()

        try:
            self.nrf.send(data)
            return True
        except OSError as e:
            print("Send failed:", e)
            return False

    def send_with_retry(self, data, retries=3, delay=0.1):
        for _ in range(retries):
            if self.send(data):
                return True
            utime.sleep(delay)
        return False



class Receiver(RadioBase):
    def __init__(self, rx_address=b"1Node", pipe_id=0, **kwargs):
        super().__init__(**kwargs)

        if len(rx_address) != 5:
            raise ValueError("Address must be 5 bytes")

        self.rx_address = rx_address
        self.pipe_id = pipe_id
        self.handlers = {}
        self.default_handler = None

        self.nrf.open_rx_pipe(self.pipe_id, self.rx_address)
        self.nrf.start_listening()

    def available(self):
        return self.nrf.any()

    def receive(self):
        if self.available():
            data = self.nrf.recv()
            data = data.rstrip(b"\x00")

            try:
                return data.decode()
            except:
                return data

        return None

    def add_handler(self, message, func):
        self.handlers[message] = func

    def set_default_handler(self, func):
        self.default_handler = func

    def dispatch(self, msg):
        try:
            if msg in self.handlers:
                self.handlers[msg]()
            elif self.default_handler is not None:
                self.default_handler(msg)
            else:
                print("No handler for:", msg)
        except Exception as e:
            print("Handler error for", msg, ":", e)

    def listen_once(self):
        msg = self.receive()
        if msg is not None:
            self.dispatch(msg)
            return msg
        return None

    def listen(self, delay=0.01):
        while True:
            self.listen_once()
            utime.sleep(delay)