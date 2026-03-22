from pca9685 import PCA9685Driver
from servo import Servo, ContinuousServo
import time

driver = PCA9685Driver(
    i2c_periph_addr=0x40,
    i2c_channel=0,
    scl_pin=1,
    sda_pin=0,
    i2c_freq=400000
)
driver.set_pwm_frequency(50)

servo = Servo(driver, 0)
servo1 = ContinuousServo(driver, 1)
servo.move_to_angle(90)