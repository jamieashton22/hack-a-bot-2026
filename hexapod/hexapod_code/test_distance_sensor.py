from distance_sensor import distance_sensor
import time

sensor = distance_sensor(trig_pin = 19, echo_pin = 18)

print("starting distance test")

while True:
    dist = sensor.get_distance_cm()

    if dist == -1:
        print("Out of range")
    else:
        print("Distance:", dist, "cm")

    time.sleep(0.2)