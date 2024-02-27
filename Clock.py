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
                
            self.txt1 = Text(Point(323, y + i * 46 + b), "––")
            self.txt1.setSize(36)
            self.txt1.setStyle("bold")

            self.txt2 = Text(Point(367, y + i * 46 + b), "––")
            self.txt2.setSize(36)
            self.txt2.setStyle("bold")

            self.txt3 = Text(Point(323, y + 35 + i * 46 + b), "––")
            self.txt3.setSize(36)
            self.txt3.setStyle("bold")

            self.txt4 = Text(Point(367, y + 35 + i * 46 + b), "––")
            self.txt4.setSize(36)
            self.txt4.setStyle("bold")

            self.txt5 = Text(Point(300, y + 15 + i * 46 + b), "l")
            self.txt5.setSize(36)
            self.txt5.setStyle("bold")

            self.txt6 = Text(Point(345, y + 15 + i * 46 + b), "l")
            self.txt6.setSize(36)
            self.txt6.setStyle("bold")

            self.txt7 = Text(Point(390, y + 15 + i * 46 + b), "l")
            self.txt7.setSize(36)
            self.txt7.setStyle("bold")

            self.txt1.draw(win)
            self.txt2.draw(win)
            self.txt3.draw(win)
            self.txt4.draw(win)
            self.txt5.draw(win)
            self.txt6.draw(win)
            self.txt7.draw(win)
            
            if int(digit) == 0:
                self.txt6.setTextColor("grey50")
                
            if int(digit) == 1:
                self.txt1.setTextColor("grey50")
                self.txt2.setTextColor("grey50")
                self.txt5.setTextColor("grey50")
                self.txt6.setTextColor("grey50")
                self.txt7.setTextColor("grey50")

            if int(digit) == 2:
                self.txt1.setTextColor("grey50")
                self.txt4.setTextColor("grey50")

            if int(digit) == 3:
                self.txt1.setTextColor("grey50")
                self.txt2.setTextColor("grey50")

            if int(digit) == 4:
                self.txt2.setTextColor("grey50")
                self.txt5.setTextColor("grey50")
                self.txt7.setTextColor("grey50")

            if int(digit) == 5:
                self.txt2.setTextColor("grey50")
                self.txt3.setTextColor("grey50")

            if int(digit) == 6:
                self.txt3.setTextColor("grey50")

            if int(digit) == 7:
                self.txt1.setTextColor("grey50")
                self.txt2.setTextColor("grey50")
                self.txt6.setTextColor("grey50")
                self.txt7.setTextColor("grey50")

            if int(digit) == 8:
                pass

            if int(digit) == 9:
                self.txt2.setTextColor("grey50")
                self.txt7.setTextColor("grey50")

            i += 1

        self.colon = Text(Point(345, y + 98), ".   .")
        self.colon.setSize(36)
        self.colon.setStyle("bold")
        self.colon.draw(win)

    def set_time(self, time):
        self.time = time

    def get_time(self):
        self.time = int(self.time[0:2]) * 60 + int(self.time[2:4])
        return self.time

    def undraw(self):
        self.txt1.undraw()
        self.txt2.undraw()
        self.txt3.undraw()
        self.txt4.undraw()
        self.txt5.undraw()
        self.txt6.undraw()
        self.txt7.undraw()
        self.colon.undraw()
