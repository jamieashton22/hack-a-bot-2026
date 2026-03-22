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
servo1 = Servo(driver, 1)
servo2 = Servo(driver, 2)
while True:
    servo.move_to_angle(20)
    servo1.move_to_angle(90)
    servo2.move_to_angle(90)
    time.sleep(2)
    servo.move_to_angle(90)
    servo1.move_to_angle(90)
    servo2.move_to_angle(90)
    time.sleep(2)