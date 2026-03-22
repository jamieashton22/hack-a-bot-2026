
# WRAPPER CLASS FOR JOYSTICKS


from machine import Pin, ADC
from utime import sleep

class Joystick:
    def __init__(self, x_pin, y_pin, button_pin, deadzone = 5000, side = "LEFT"):

        # store raw input
        self.x = ADC(Pin(x_pin)) if x_pin is not None else None
        self.y = ADC(Pin(y_pin))

        self.button = Pin(button_pin, Pin.IN, Pin.PULL_UP)

        self.deadzone = deadzone

        self.side = side

        # calibrate centre value
        self.center_x = self.x.read_u16() if self.x is not None else 0
        self.center_y = self.y.read_u16()

    # function to read values
    def read(self):

        x = self.x.read_u16() if self.x is not None else 0
        return x, self.y.read_u16()
    
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
            dir_x = "L"
        elif dx > self.deadzone:
            dir_x = "R"

        if dy < -self.deadzone:
            if self.side == "LEFT":
                dir_y = "B"
            else:
                dir_y = "D"
        elif dy > self.deadzone:
            if self.side == "LEFT":
                dir_y = "F"
            else:
                dir_y = "U"

        if dir_x and dir_y:
            return dir_y + "_" + dir_x
        
        return dir_x or dir_y or "S"



