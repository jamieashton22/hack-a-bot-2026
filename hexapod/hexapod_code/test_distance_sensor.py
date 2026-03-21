from distance_sensor import distance_sensor
import time

sensor = distance_sensor(trig_pin=19, echo_pin=18)

print("Starting distance test...")

while True:

    # # Bypass get_distance_cm and check raw pulse
    # duration = sensor.send_pulse()
    # print("Raw duration:", duration)


    dist = sensor.get_distance_cm()

    if dist == -1:
        print("Out of range")
    else:
        print("Distance:", dist, "cm")

    time.sleep(0.2)