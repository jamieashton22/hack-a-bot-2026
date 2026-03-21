from machine import Pin, I2C
import ssd1306
import time

i2c = I2C(0, scl=Pin(1), sda=Pin(0))
display = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

def up_arrow(x, y):
    display.fill(0)

    # id: 0 line 135
    display.line(x - 8, y, x + 8, y, 1)
    # id: 1 line 136
    display.line(x - 8, y, x, y - 13, 1)
    # id: 2 line 137
    display.line(x, y - 13, x + 8, y, 1)
    # id: 3 fillRect 138
    display.fill_rect(x - 3, y - 7, 7, 7, 1)
    # id: 4 fillRect 139
    display.fill_rect(x + 3, y - 4, 3, 4, 1)
    # id: 5 fillRect 140
    display.fill_rect(x - 5, y - 4, 3, 4, 1)
    # id: 6 fillRect 141
    display.fill_rect(x - 1, y - 9, 3, 2, 1)
    # id: 7 fillRect 142
    display.fill_rect(x - 1, y - 10, 3, 1, 1)
    # id: 8 fillRect 143
    display.fill_rect(x, y - 12, 1, 3, 1)
    # id: 9 fillRect 144
    display.fill_rect(x + 2, y - 8, 1, 2, 1)
    # id: 10 fillRect 145
    display.fill_rect(x + 4, y - 5, 1, 1, 1)
    # id: 11 fillRect 146
    display.fill_rect(x + 5, y - 2, 2, 2, 1)
    # id: 12 fillRect 147
    display.fill_rect(x - 3, y - 5, 1, 1, 1)
    # id: 13 fillRect 148
    display.fill_rect(x - 4, y - 5, 1, 2, 1)
    # id: 14 fillRect 149
    display.fill_rect(x - 2, y - 8, 1, 1, 1)
    # id: 15 fillRect 150
    display.fill_rect(x - 6, y - 2, 1, 2, 1)
    # id: 16 fillRect 151
    display.fill_rect(x, y, 1, 27, 1)
    # id: 17 fillRect 152
    display.fill_rect(x - 2, y + 1, 5, 26, 1)

    display.show()

def down_arrow(x, y):
    display.fill(0)

    # id: 0 line 135
    display.line(x - 8, y, x + 8, y, 1)
    # id: 1 line 136
    display.line(x + 8, y, x, y + 13, 1)
    # id: 2 line 137
    display.line(x, y + 13, x - 8, y, 1)
    # id: 3 fillRect 138
    display.fill_rect(x - 3, y + 1, 7, 7, 1)
    # id: 4 fillRect 139
    display.fill_rect(x + 3, y + 1, 3, 4, 1)
    # id: 5 fillRect 140
    display.fill_rect(x - 5, y + 1, 3, 4, 1)
    # id: 6 fillRect 141
    display.fill_rect(x - 1, y + 8, 3, 2, 1)
    # id: 7 fillRect 142
    display.fill_rect(x - 1, y + 10, 3, 1, 1)
    # id: 8 fillRect 143
    display.fill_rect(x, y + 10, 1, 3, 1)
    # id: 9 fillRect 144
    display.fill_rect(x + 2, y + 7, 1, 2, 1)
    # id: 10 fillRect 145
    display.fill_rect(x + 4, y + 5, 1, 1, 1)
    # id: 11 fillRect 146
    display.fill_rect(x + 5, y + 1, 2, 2, 1)
    # id: 12 fillRect 147
    display.fill_rect(x - 3, y + 5, 1, 1, 1)
    # id: 13 fillRect 148
    display.fill_rect(x - 4, y + 4, 1, 2, 1)
    # id: 14 fillRect 149
    display.fill_rect(x - 2, y + 8, 1, 1, 1)
    # id: 15 fillRect 150
    display.fill_rect(x - 6, y + 1, 1, 4, 1)
    # id: 16 fillRect 151
    display.fill_rect(x, y - 27, 1, 27, 1)
    # id: 17 fillRect 152
    display.fill_rect(x - 2, y - 26, 5, 26, 1)

    display.show()

def left_arrow(x, y):
    display.fill(0)

    # id: 0 line 153
    display.line(x, y - 8, x, y + 8, 1)
    # id: 1 line 154
    display.line(x, y + 8, x - 13, y, 1)
    # id: 2 line 155
    display.line(x - 14, y, x - 14, y, 1)
    # id: 3 line 156
    display.line(x - 13, y, x, y - 8, 1)
    # id: 4 fillRect 157
    display.fill_rect(x, y - 1, 26, 2, 1)
    # id: 5 fillRect 158
    display.fill_rect(x + 25, y - 1, 1, 1, 1)
    # id: 6 fillRect 159
    display.fill_rect(x + 1, y + 1, 25, 1, 1)
    # id: 7 fillRect 160
    display.fill_rect(x, y - 2, 26, 6, 1)
    # id: 8 fillRect 161
    display.fill_rect(x - 12, y, 13, 1, 1)
    # id: 9 fillRect 162
    display.fill_rect(x - 6, y - 4, 6, 4, 1)
    # id: 10 fillRect 163
    display.fill_rect(x - 7, y + 1, 7, 4, 1)
    # id: 11 fillRect 164
    display.fill_rect(x - 2, y + 1, 2, 1, 1)
    # id: 12 fillRect 165
    display.fill_rect(x - 5, y - 1, 1, 1, 1)
    # id: 13 fillRect 166
    display.fill_rect(x - 8, y - 2, 2, 2, 1)
    # id: 14 fillRect 167
    display.fill_rect(x - 8, y + 1, 2, 2, 1)
    # id: 15 fillRect 168
    display.fill_rect(x - 10, y + 1, 2, 1, 1)
    # id: 16 fillRect 169
    display.fill_rect(x - 10, y - 1, 2, 1, 1)
    # id: 17 fillRect 170
    display.fill_rect(x - 7, y - 3, 1, 1, 1)
    # id: 18 fillRect 171
    display.fill_rect(x - 4, y - 5, 4, 1, 1)
    # id: 19 fillRect 172
    display.fill_rect(x - 2, y - 6, 2, 1, 1)
    # id: 20 fillRect 173
    display.fill_rect(x - 4, y + 5, 4, 2, 1)
    # id: 21 fillRect 174
    display.fill_rect(x + 1, y - 3, 25, 3, 1)
    # id: 22 fillRect 175
    display.fill_rect(x + 25, y - 3, 8, 7, 1)
    # id: 23 fillRect 176
    display.fill_rect(x + 32, y + 3, 1, 1, 1)

    display.show()

def right_arrow(x, y):
    display.fill(0)

    # id: 0 line 153
    display.line(x, y - 8, x, y + 8, 1)
    # id: 1 line 154
    display.line(x, y + 8, x + 13, y, 1)
    # id: 2 line 155
    display.line(x + 14, y, x + 14, y, 1)
    # id: 3 line 156
    display.line(x + 13, y, x, y - 8, 1)
    # id: 4 fillRect 157
    display.fill_rect(x - 26, y - 1, 26, 2, 1)
    # id: 5 fillRect 158
    display.fill_rect(x - 26, y - 1, 1, 1, 1)
    # id: 6 fillRect 159
    display.fill_rect(x - 26, y + 1, 25, 1, 1)
    # id: 7 fillRect 160
    display.fill_rect(x - 26, y - 2, 26, 6, 1)
    # id: 8 fillRect 161
    display.fill_rect(x + 1, y, 13, 1, 1)
    # id: 9 fillRect 162
    display.fill_rect(x + 1, y - 4, 6, 4, 1)
    # id: 10 fillRect 163
    display.fill_rect(x + 1, y + 1, 7, 4, 1)
    # id: 11 fillRect 164
    display.fill_rect(x + 1, y + 1, 2, 1, 1)
    # id: 12 fillRect 165
    display.fill_rect(x + 5, y - 1, 1, 1, 1)
    # id: 13 fillRect 166
    display.fill_rect(x + 7, y - 2, 2, 2, 1)
    # id: 14 fillRect 167
    display.fill_rect(x + 7, y + 1, 2, 2, 1)
    # id: 15 fillRect 168
    display.fill_rect(x + 9, y + 1, 2, 1, 1)
    # id: 16 fillRect 169
    display.fill_rect(x + 9, y - 1, 2, 1, 1)
    # id: 17 fillRect 170
    display.fill_rect(x + 7, y - 3, 1, 1, 1)
    # id: 18 fillRect 171
    display.fill_rect(x + 1, y - 5, 4, 1, 1)
    # id: 19 fillRect 172
    display.fill_rect(x + 1, y - 6, 2, 1, 1)
    # id: 20 fillRect 173
    display.fill_rect(x + 1, y + 5, 4, 2, 1)
    # id: 21 fillRect 174
    display.fill_rect(x - 26, y - 3, 25, 3, 1)
    # id: 22 fillRect 175
    display.fill_rect(x - 33, y - 3, 8, 7, 1)
    # id: 23 fillRect 176
    display.fill_rect(x - 33, y + 3, 1, 1, 1)

    display.show()

y = 0
x = 0
while True:
    
    mode = 2
    # ====== up arrow ============
    if mode == 0:
        x = 64
        y_min = 13
        y_max = 27

        if y == 0 - y_max:
            y = 64 + y_min
        
        up_arrow(x, y)
        y -= 1

    # ====== down arrow ==========
    if mode == 1:
        x = 64
        y_min = 27
        y_max = 13

        if y == 64 + y_min:
            y = 0 - y_max
        
        down_arrow(x, y)
        y += 1

    # ====== left arrow ==========
    if mode == 2:
        y = 32
        x_min = 13
        x_max = 33

        if x == 0 - x_max:
            x = 128 + x_min
        
        left_arrow(x, y)
        x -= 1

    # ====== right arrow =========
    if mode == 3:
        y = 32
        x_min = 33
        x_max = 14

        if x == 128 + x_min:
            x = 0 - x_max
        
        right_arrow(x, y)
        x += 1

    # ====== Object Detected =====
    if mode == 4:
        x = 0
