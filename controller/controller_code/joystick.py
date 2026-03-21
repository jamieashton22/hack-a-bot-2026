
# WRAPPER CLASS FOR JOYSTICKS


from machine import Pin, ADC
from utime import sleep

class Joystick:
    def __init__(self, x_pin, y_pin, button_pin, deadzone = 5000):

        # store raw input
        self.x = ADC(Pin(x_pin))
        self.y = ADC(Pin(y_pin))

        self.button = Pin(button_pin, Pin.IN, Pin.PULL_UP)

        self.deadzone = deadzone

        # calibrate centre value
        self.center_x = self.x.read_u16()
        self.center_y = self.y.read_u16()

    # function to read values
    def read(self):
        return self.x.read_u16(), self.y.read_u16()
    
    # function to check if button pressed
    def pressed(self):
        return not self.button.value() 
    
    # function to get direction

    def direction(self):
        x,y = self.read()

        dx = x - self.center_x
        dy = y - self.center_y

        dir_x = ""
        dir_y = ""

        if dx < -self.deadzone:
            dir_x = "LEFT"
        elif dx > self.deadzone:
            dir_x = "RIGHT"

        if dy < -self.deadzone:
            dir_y = "DOWN"
        elif dy > self.deadzone:
            dir_y = "UP"

        if dir_x and dir_y:
            return dir_y + "_" + dir_x
        
        return dir_x or dir_y or "CENTER"

        


