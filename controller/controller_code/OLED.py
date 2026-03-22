# OLED class 

# FIX: RIGHT IS UP 

from machine import Pin, I2C
import ssd1306

class OLEDDisplay:
    def __init__(self, sda_pin=0, scl_pin=1, width=128, height=64, addr=0x3C, i2c_id=0):
        i2c = I2C(i2c_id, scl=Pin(scl_pin), sda=Pin(sda_pin))
        self.display = ssd1306.SSD1306_I2C(width, height, i2c, addr=addr)
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0


    def clear(self):
        self.display.fill(0)
        self.display.show()

    def up_arrow(self, x, y):
        d = self.display
        d.fill(0)
        d.line(x - 8, y, x + 8, y, 1)
        d.line(x - 8, y, x, y - 13, 1)
        d.line(x, y - 13, x + 8, y, 1)
        d.fill_rect(x - 3, y - 7, 7, 7, 1)
        d.fill_rect(x + 3, y - 4, 3, 4, 1)
        d.fill_rect(x - 5, y - 4, 3, 4, 1)
        d.fill_rect(x - 1, y - 9, 3, 2, 1)
        d.fill_rect(x - 1, y - 10, 3, 1, 1)
        d.fill_rect(x, y - 12, 1, 3, 1)
        d.fill_rect(x + 2, y - 8, 1, 2, 1)
        d.fill_rect(x + 4, y - 5, 1, 1, 1)
        d.fill_rect(x + 5, y - 2, 2, 2, 1)
        d.fill_rect(x - 3, y - 5, 1, 1, 1)
        d.fill_rect(x - 4, y - 5, 1, 2, 1)
        d.fill_rect(x - 2, y - 8, 1, 1, 1)
        d.fill_rect(x - 6, y - 2, 1, 2, 1)
        d.fill_rect(x, y, 1, 27, 1)
        d.fill_rect(x - 2, y + 1, 5, 26, 1)
        d.show()

    def down_arrow(self, x, y):
        d = self.display
        d.fill(0)
        d.line(x - 8, y, x + 8, y, 1)
        d.line(x + 8, y, x, y + 13, 1)
        d.line(x, y + 13, x - 8, y, 1)
        d.fill_rect(x - 3, y + 1, 7, 7, 1)
        d.fill_rect(x + 3, y + 1, 3, 4, 1)
        d.fill_rect(x - 5, y + 1, 3, 4, 1)
        d.fill_rect(x - 1, y + 8, 3, 2, 1)
        d.fill_rect(x - 1, y + 10, 3, 1, 1)
        d.fill_rect(x, y + 10, 1, 3, 1)
        d.fill_rect(x + 2, y + 7, 1, 2, 1)
        d.fill_rect(x + 4, y + 5, 1, 1, 1)
        d.fill_rect(x + 5, y + 1, 2, 2, 1)
        d.fill_rect(x - 3, y + 5, 1, 1, 1)
        d.fill_rect(x - 4, y + 4, 1, 2, 1)
        d.fill_rect(x - 2, y + 8, 1, 1, 1)
        d.fill_rect(x - 6, y + 1, 1, 4, 1)
        d.fill_rect(x, y - 27, 1, 27, 1)
        d.fill_rect(x - 2, y - 26, 5, 26, 1)
        d.show()

    def left_arrow(self, x, y):
        d = self.display
        d.fill(0)
        d.line(x, y - 8, x, y + 8, 1)
        d.line(x, y + 8, x - 13, y, 1)
        d.line(x - 14, y, x - 14, y, 1)
        d.line(x - 13, y, x, y - 8, 1)
        d.fill_rect(x, y - 1, 26, 2, 1)
        d.fill_rect(x + 25, y - 1, 1, 1, 1)
        d.fill_rect(x + 1, y + 1, 25, 1, 1)
        d.fill_rect(x, y - 2, 26, 6, 1)
        d.fill_rect(x - 12, y, 13, 1, 1)
        d.fill_rect(x - 6, y - 4, 6, 4, 1)
        d.fill_rect(x - 7, y + 1, 7, 4, 1)
        d.fill_rect(x - 2, y + 1, 2, 1, 1)
        d.fill_rect(x - 5, y - 1, 1, 1, 1)
        d.fill_rect(x - 8, y - 2, 2, 2, 1)
        d.fill_rect(x - 8, y + 1, 2, 2, 1)
        d.fill_rect(x - 10, y + 1, 2, 1, 1)
        d.fill_rect(x - 10, y - 1, 2, 1, 1)
        d.fill_rect(x - 7, y - 3, 1, 1, 1)
        d.fill_rect(x - 4, y - 5, 4, 1, 1)
        d.fill_rect(x - 2, y - 6, 2, 1, 1)
        d.fill_rect(x - 4, y + 5, 4, 2, 1)
        d.fill_rect(x + 1, y - 3, 25, 3, 1)
        d.fill_rect(x + 25, y - 3, 8, 7, 1)
        d.fill_rect(x + 32, y + 3, 1, 1, 1)
        d.show()

    def right_arrow(self, x, y):
        d = self.display
        d.fill(0)
        d.line(x, y - 8, x, y + 8, 1)
        d.line(x, y + 8, x + 13, y, 1)
        d.line(x + 14, y, x + 14, y, 1)
        d.line(x + 13, y, x, y - 8, 1)
        d.fill_rect(x - 26, y - 1, 26, 2, 1)
        d.fill_rect(x - 26, y - 1, 1, 1, 1)
        d.fill_rect(x - 26, y + 1, 25, 1, 1)
        d.fill_rect(x - 26, y - 2, 26, 6, 1)
        d.fill_rect(x + 1, y, 13, 1, 1)
        d.fill_rect(x + 1, y - 4, 6, 4, 1)
        d.fill_rect(x + 1, y + 1, 7, 4, 1)
        d.fill_rect(x + 1, y + 1, 2, 1, 1)
        d.fill_rect(x + 5, y - 1, 1, 1, 1)
        d.fill_rect(x + 7, y - 2, 2, 2, 1)
        d.fill_rect(x + 7, y + 1, 2, 2, 1)
        d.fill_rect(x + 9, y + 1, 2, 1, 1)
        d.fill_rect(x + 9, y - 1, 2, 1, 1)
        d.fill_rect(x + 7, y - 3, 1, 1, 1)
        d.fill_rect(x + 1, y - 5, 4, 1, 1)
        d.fill_rect(x + 1, y - 6, 2, 1, 1)
        d.fill_rect(x + 1, y + 5, 4, 2, 1)
        d.fill_rect(x - 26, y - 3, 25, 3, 1)
        d.fill_rect(x - 33, y - 3, 8, 7, 1)
        d.fill_rect(x - 33, y + 3, 1, 1, 1)
        d.show()

    def progress_bar(self, x, label="OBJECT DETECTED"):
        d = self.display
        d.fill(0)
        d.text(label, 4, 0, 1)
        d.rect(15, 26, 97, 12, 1)
        d.fill_rect(16, 27, x - 16, 10, 1)
        d.show()

    def show_distance(self, distance_cm):
        d = self.display
        d.fill(0)
        
        if distance_cm is None:
            d.text("NO READING", 20, 28, 1)
        else:
            d.text("OBJECT DETECTED", 5, 6, 1)
            d.text(" Distance:", 20, 16, 1)
            d.text(str(round(distance_cm, 1)) + " cm", 30, 32, 1)
        
        d.show()

    def main_operation(self, mode, distance_cm):


        if  distance_cm > 30 or distance_cm < 5 or distance_cm == None:


            # UP ARROW
            if mode == "UP":
                self.x = 64
                y_min = 13
                y_max = 27

                if self.y <= 0 - y_max:
                    self.y = 64 + y_min
                
                self.up_arrow(self.x, self.y)
                self.y -= 16

            # DOWN ARROW 

            elif mode == "DOWN":
                self.x = 64
                y_min = 27
                y_max = 13

                if self.y >= 64 + y_min:
                    self.y = 0 - y_max

                self.down_arrow(self.x, self.y)
                self.y += 16

            # LEFT ARROW
            elif mode == "LEFT":
                self.y = 32
                x_min = 13
                x_max = 33

                if self.x <= 0 - x_max:
                    self.x = 128 + x_min
                
                self.left_arrow(self.x, self.y)
                self.x -= 20

            # RIGHT ARROW
            elif mode == "RIGHT":
                self.y = 32
                x_min = 33
                x_max = 14

                if self.x >= 128 + x_min:
                    self.x = 0 - x_max
                
                self.right_arrow(self.x,self.y)
                self.x += 20

            elif mode == "CENTER":
                self.display.text("NO OBJECT", 5, 6, 1)
                self.display.text("DETECTED", 20, 16, 1)


        else:
            self.show_distance(distance_cm)
