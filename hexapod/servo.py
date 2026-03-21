class Servo:
    def __init__(self, driver, channel, min_us=1000, max_us=2000, angle_range=180):
        """
        driver      : PCA9685Driver object
        channel     : 0 to 15
        min_us      : pulse width for 0 degrees (microseconds)
        max_us      : pulse width for max angle
        angle_range : usually 180
        """
        self.driver = driver
        self.channel = channel
        self.min_us = min_us
        self.max_us = max_us
        self.angle_range = angle_range

    def set_angle(self, angle):
        angle = max(0, min(self.angle_range, angle))

        # convert angle -> pulse width
        pulse_us = self.min_us + (self.max_us - self.min_us) * (angle / self.angle_range)

        # convert us -> ms because driver expects ms
        pulse_ms = pulse_us / 1000.0

        # send to driver
        self.driver.set_pwm_dc_ontime(self.channel, pulse_ms)

    def center(self):
        self.set_angle(self.angle_range / 2)

    def off(self):
        self.driver.set_pwm_dc_percent(self.channel, 0)