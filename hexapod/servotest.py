from pca9685 import PCA9685Driver
from servo import Servo
import time

driver = PCA9685Driver(
    i2c_periph_addr=0x40,
    i2c_channel=0,
    scl_pin=1,
    sda_pin=0,
    i2c_freq=400000
)

driver.set_pwm_frequency(50)

servo0 = Servo(driver, 0)
servo1 = Servo(driver, 1)
servo2 = Servo(driver, 2)

while True:
    servo0.set_angle(90)
    servo1.set_angle(90)
    servo2.set_angle(90)
    time.sleep(2)

    servo0.set_angle(70)
    servo1.set_angle(200)
    servo2.set_angle(110)
    time.sleep(2)