from hexapod_code.hexapod import Leg
from hexapod_code.pca9685 import PCA9685Driver
from hexapod_code.servo import Servo, ContinuousServo
import time

driver = PCA9685Driver(
    i2c_periph_addr=0x40,
    i2c_channel=0,
    scl_pin=1,
    sda_pin=0,
    i2c_freq=400000
)    

servo1 = Servo(driver, 1)
servo0 = Servo(driver, 0)
servo2 = Servo(driver, 2)

leg1 = Leg(servo0, servo1, servo2,30,60,100)

servo0.move_to_angle(90)
servo1.move_to_angle(90)
servo2.move_to_angle(90)
time.sleep(2)
servo0.move_to_angle(110)
time.sleep(2)
servo0.move_to_angle(90)
time.sleep(2)

print("Moving foot")
while True:
    
    leg1.move_foot(90, -30, -20)
    # servo0.move_to_angle(90)
    # servo1.move_to_angle(79.7)
    # servo2.move_to_angle(63.1)
    time.sleep(2)
    leg1.move_foot(60, 30, -40)
    # servo0.move_to_angle(90)
    # servo1.move_to_angle(115.2)
    # servo2.move_to_angle(23.5)
    time.sleep(2)
