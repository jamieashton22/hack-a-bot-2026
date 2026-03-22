import utime
from hexapod import Hexapod, Leg
from pca9685 import PCA9685Driver
from servo import Servo, GPIOServo
from Radio import Receiver

ADDRESS = b"team6"

driver = PCA9685Driver(
    i2c_periph_addr=0x40,
    i2c_channel=0,
    scl_pin=1,
    sda_pin=0,
    i2c_freq=400000
)
driver.set_pwm_frequency(50)

legs = []

# First 5 legs use PCA9685 only
for i in range(5):
    is_left = (i >= 3)

    coxa_sign = -1 if is_left else 1
    femur_sign = 1
    tibia_sign = 1

    coxa_servo = Servo(driver, channel=i * 3)
    femur_servo = Servo(driver, channel=i * 3 + 1)
    tibia_servo = Servo(driver, channel=i * 3 + 2)

    leg = Leg(
        coxa_servo, femur_servo, tibia_servo,
        L1=30, L2=60, L3=100,
        home_x=50, home_y=0, home_z=-40,
        coxa_offset=90, femur_offset=90, tibia_offset=90,
        coxa_sign=coxa_sign,
        femur_sign=femur_sign,
        tibia_sign=tibia_sign,
        coxa_min=0, coxa_max=180,
        femur_min=0, femur_max=180,
        tibia_min=0, tibia_max=180
    )
    legs.append(leg)

# 6th leg
i = 5
is_left = True

coxa_sign = -1 if is_left else 1
femur_sign = 1
tibia_sign = 1

coxa_servo = Servo(driver, channel=15)
femur_servo = GPIOServo(pin_num=16) #change when we wire
tibia_servo = GPIOServo(pin_num=17)

leg = Leg(
    coxa_servo, femur_servo, tibia_servo,
    L1=30, L2=60, L3=100,
    home_x=50, home_y=0, home_z=-40,
    coxa_offset=90, femur_offset=90, tibia_offset=90,
    coxa_sign=coxa_sign,
    femur_sign=femur_sign,
    tibia_sign=tibia_sign,
    coxa_min=0, coxa_max=180,
    femur_min=0, femur_max=180,
    tibia_min=0, tibia_max=180
)
legs.append(leg)

hexapod = Hexapod(legs)
rx = Receiver(rx_address=ADDRESS)

current_cmd = "S"

def handle_forward(msg=None):
    global current_cmd
    current_cmd = "F"
    hexapod.clear_stop_request()

def handle_left(msg=None):
    global current_cmd
    current_cmd = "L"
    hexapod.clear_stop_request()
    
def handle_turn_right(msg=None):
    global current_cmd
    current_cmd = "R"
    hexapod.clear_stop_request()

def handle_stop(msg=None):
    global current_cmd
    current_cmd = "S"
    hexapod.request_stop()

def unknown_command(msg=None):
    print("Unknown command:", msg)

rx.add_handler("F", handle_forward)
rx.add_handler("S", handle_stop)
rx.add_handler("L", handle_left)
rx.add_handler("R", handle_turn_right)
rx.set_default_handler(unknown_command)

# Initial neutral pose once
for leg in legs:
    leg.set_joint_angles(0, 0, 0)
    utime.sleep_ms(300)

start = utime.ticks_ms()

while True:
    now = utime.ticks_diff(utime.ticks_ms(), start) / 1000.0

    rx.listen()

    if hexapod.stop_requested and not hexapod.is_standing:
        hexapod.update_stopping_gait(now)

    elif current_cmd == "F":
        hexapod.walk_forward(
            time_now=now,
            step_length=15,
            step_height=8,
            ground_z=-50,
            period=2.0
        )

    elif current_cmd == "L":
        hexapod.turn_left(
            time_now=now,
            turn_amount=1.0,
            step_height=8,
            ground_z=-50,
            period=2.0
        )
    
    elif current_cmd == "R":
        hexapod.turn_right(
            time_now=now,
            turn_amount=1.0,
            step_height=8,
            ground_z=-50,
            period=2.0
        )

    else:
        if not hexapod.stop_requested:
            hexapod.stand()

    utime.sleep_ms(20)