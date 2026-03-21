
# Distance sensor wrapper class
# has 2 pins trig and echo 

# Echo: pin 18
# Trig resistors then GP pin, 19

from machine import Pin
import time

class distance_sensor:

    def __init__(self, trig_pin, echo_pin, timeout_us =30000):
        self.trig = Pin(trig_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN)

        self.timeout = timeout_us

        self.trig.value(0)
        time.sleep(0.1)

    def send_pulse(self):

        # Send 10µs pulse
        self.trig.value(0)
        time.sleep_us(2)
        self.trig.value(1)
        time.sleep_us(10)
        self.trig.value(0)

        # Wait for echo start
        start = time.ticks_us()
        while self.echo.value() == 0:
            if time.ticks_diff(time.ticks_us(), start) > self.timeout:
                return None
        start_time = time.ticks_us()

        # Wait for echo end
        while self.echo.value() == 1:
            if time.ticks_diff(time.ticks_us(), start_time) > self.timeout:
                return None
        end_time = time.ticks_us()

        # Calculate duration
        return time.ticks_diff(end_time, start_time)
    
    def get_distance_cm(self):

        duration = self.send_pulse()

        if duration is None:
            return None
        
        distance = (duration * 0.0343) / 2
        return distance
    
    # readings averaged over 5 samples
    def get_distance_cm_avg(self, samples=5):
            
            readings = []

            for _ in range(samples):
                d = self.get_distance_cm()
                if d is not None:
                    readings.append(d)

            return sum(readings) / len(readings) if readings else None