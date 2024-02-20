#clock class
from graphics import *

class Clock:
    def __init__(self, side):
        self.side = side

    def draw(self, win, time):
        self.time = time

        digit1 = time[0]
        digit2 = time[1]
        digit3 = time[2]
        digit4 = time[3]

        digits = [digit1, digit2, digit3, digit4]

        if self.side == 'w':
            y = 245
        else:
            y = 465

        b = 0
        i = 0
        for digit in digits:
            if i == 2:
                b = 8
                
            txt1 = Text(Point(323, y + i * 46 + b), "––")
            txt1.setSize(36)
            txt1.setStyle("bold")

            txt2 = Text(Point(367, y + i * 46 + b), "––")
            txt2.setSize(36)
            txt2.setStyle("bold")

            txt3 = Text(Point(323, y + 35 + i * 46 + b), "––")
            txt3.setSize(36)
            txt3.setStyle("bold")

            txt4 = Text(Point(367, y + 35 + i * 46 + b), "––")
            txt4.setSize(36)
            txt4.setStyle("bold")

            txt5 = Text(Point(300, y + 15 + i * 46 + b), "l")
            txt5.setSize(36)
            txt5.setStyle("bold")

            txt6 = Text(Point(345, y + 15 + i * 46 + b), "l")
            txt6.setSize(36)
            txt6.setStyle("bold")

            txt7 = Text(Point(390, y + 15 + i * 46 + b), "l")
            txt7.setSize(36)
            txt7.setStyle("bold")

            txt1.draw(win)
            txt2.draw(win)
            txt3.draw(win)
            txt4.draw(win)
            txt5.draw(win)
            txt6.draw(win)
            txt7.draw(win)
            
            if int(digit) == 0:
                txt6.setTextColor("grey50")
                
            if int(digit) == 1:
                txt1.setTextColor("grey50")
                txt2.setTextColor("grey50")
                txt5.setTextColor("grey50")
                txt6.setTextColor("grey50")
                txt7.setTextColor("grey50")

            if int(digit) == 2:
                txt1.setTextColor("grey50")
                txt4.setTextColor("grey50")

            if int(digit) == 3:
                txt1.setTextColor("grey50")
                txt2.setTextColor("grey50")

            if int(digit) == 4:
                txt2.setTextColor("grey50")
                txt5.setTextColor("grey50")
                txt7.setTextColor("grey50")

            if int(digit) == 5:
                txt2.setTextColor("grey50")
                txt3.setTextColor("grey50")

            if int(digit) == 6:
                txt3.setTextColor("grey50")

            if int(digit) == 7:
                txt1.setTextColor("grey50")
                txt2.setTextColor("grey50")
                txt6.setTextColor("grey50")
                txt7.setTextColor("grey50")

            if int(digit) == 8:
                pass

            if int(digit) == 9:
                txt2.setTextColor("grey50")
                txt7.setTextColor("grey50")

            i += 1

        colon = Text(Point(345, y + 98), ".   .")
        colon.setSize(36)
        colon.setStyle("bold")
        colon.draw(win)

    def set_time(self, time):
        self.time = time

    def get_time(self):
        return self.time
