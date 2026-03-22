from OLED import OLEDDisplay
from distance_sensor import distance_sensor
import time
from joystick import Joystick

oled = OLEDDisplay()
sensor = distance_sensor(trig_pin=19, echo_pin=18)
js = js = Joystick(x_pin=26, y_pin=27, button_pin=22)



while True:

    distance = sensor.get_distance_cm_filtered()
    direction = js.direction()

    oled.main_operation(direction,distance)
    time.sleep(0.2)

    