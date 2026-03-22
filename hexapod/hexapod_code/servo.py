class Servo:
    def __init__(self, driver, channel, min_us=1000, max_us=2000,
                 angle_range=180, offset_deg=0):
        self.driver = driver
        self.channel = channel
        self.min_us = min_us
        self.max_us = max_us
        self.angle_range = angle_range
        self.offset_deg = offset_deg
        self.current_angle = 90

    def set_angle(self, angle):
        angle = max(0, min(self.angle_range, angle))

        # convert angle -> pulse width
        pulse_us = self.min_us + (self.max_us - self.min_us) * (angle / self.angle_range)

        # convert us -> ms because driver expects ms
        pulse_ms = pulse_us / 1000.0

        # send to driver
        self.driver.set_pwm_dc_ontime(self.channel, pulse_ms)
        
    def move_to_angle(self, target_angle):
        self.set_angle(target_angle)

    def center(self):
        self.set_angle(self.angle_range / 2)

    def off(self):
        self.driver.set_pwm_dc_percent(self.channel, 0)
        
from machine import Pin, PWM

class GPIOServo:
    def __init__(self, pin_num, min_us=500, max_us=2500, angle_range=180, freq=50):
        self.pwm = PWM(Pin(pin_num))
        self.pwm.freq(freq)

        self.min_us = min_us
        self.max_us = max_us
        self.angle_range = angle_range
        self.current_angle = 90

    def move_to_angle(self, angle):
        angle = max(0, min(self.angle_range, angle))
        self.current_angle = angle

        pulse_us = self.min_us + (self.max_us - self.min_us) * (angle / self.angle_range)

        # Pico PWM uses duty_u16
        period_us = 20000  # 50 Hz = 20 ms
        duty = int((pulse_us / period_us) * 65535)
        self.pwm.duty_u16(duty)

    def off(self):
        self.pwm.duty_u16(0)        

import time

class ContinuousServo(Servo):
    def __init__(self, driver, channel, neutral_us=1500, span_us=400,
                 angle_range=180, offset_deg=0, deadband_deg=3,
                 deg_per_sec_cw=250, deg_per_sec_ccw=250,
                 drive_angle_cw=120, drive_angle_ccw=60):
        super().__init__(
            driver=driver,
            channel=channel,
            min_us=neutral_us - span_us,
            max_us=neutral_us + span_us,
            angle_range=angle_range,
            offset_deg=offset_deg
        )
        self.neutral_us = neutral_us
        self.span_us = span_us
        self.deadband_deg = deadband_deg

        self.deg_per_sec_cw = deg_per_sec_cw
        self.deg_per_sec_ccw = deg_per_sec_ccw

        self.drive_angle_cw = drive_angle_cw
        self.drive_angle_ccw = drive_angle_ccw

        self.current_angle = 90   # software estimate only

    def set_angle(self, angle):
        angle = max(0, min(self.angle_range, angle))
        self.current_angle = angle

        adjusted = angle + self.offset_deg
        adjusted = max(0, min(self.angle_range, adjusted))

        center = self.angle_range / 2
        delta = adjusted - center

        if abs(delta) <= self.deadband_deg:
            pulse_us = self.neutral_us
        else:
            norm = delta / center
            pulse_us = self.neutral_us + norm * self.span_us

        self.driver.set_pwm_dc_ontime(self.channel, pulse_us / 1000.0)

    def stop(self):
        self.driver.set_pwm_dc_ontime(self.channel, self.neutral_us / 1000.0)

    def move_to_angle(self, target_angle):
        """
        Open-loop estimate only.
        """
        target_angle = max(0, min(self.angle_range, target_angle))
        error = target_angle - self.current_angle

        if abs(error) < 1:
            self.stop()
            return

        if error > 0:
            run_time = error / self.deg_per_sec_cw
            self.set_angle(self.drive_angle_cw)
        else:
            run_time = (-error) / self.deg_per_sec_ccw
            self.set_angle(self.drive_angle_ccw)

        time.sleep(run_time)
        self.stop()
        self.current_angle = target_angle