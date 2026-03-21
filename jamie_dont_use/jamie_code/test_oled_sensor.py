from OLED import OLEDDisplay
from distance_sensor import distance_sensor
import time

oled = OLEDDisplay()
sensor = distance_sensor(trig_pin=19, echo_pin=18)

while True:

    distance = sensor.get_distance_cm_filtered()
    # oled.show_distance(distance)
    # time.sleep(0.2)

    # oled.clear

    oled.main_operation(distance)
    time.sleep(0.2)

    