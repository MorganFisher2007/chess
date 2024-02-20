from graphics import *
from Pieces import *
from Button import Button
from Clock import Clock

#from screeninfo import get_monitors

class ChessGUI:
    def __init__(self):
        #for m in get_monitors():
            #self.width = m.width
            #self.height = m.height
        self.win = GraphWin("Chess", 1470, 890, autoflush = False)
        self.win.setCoords(0, 0, 1470 - 1, 890 - 1)
        self.win.setBackground("grey16")

    def draw_piece(self, piece):
        x = piece.getX() * 100 + 498
        y = piece.getY() * 100 - 5
        IMG_file = piece.getIMG_file()

        IMG = Image(Point(x, y), IMG_file)
        piece.setIMG_obj(IMG)
        IMG.draw(self.win)

    def undraw_piece(self, piece):
        IMG = piece.getIMG_obj()
        IMG.undraw()

    def draw_squares(self, board):
        for square in board.state:
            x = square.getX() * 100 + 500
            y = square.getY() * 100 - 5

            sqr = Rectangle(Point(x - 50, y - 50), Point(x + 50, y + 50))
            sqr.setWidth(0)
            
            if square.getX() % 2 == 0:
                if square.getY() % 2 == 0:
                    sqr.setFill("PaleGreen4")
                else:
                    sqr.setFill("light goldenrod yellow")
            else:
                if square.getY() % 2 == 0:
                    sqr.setFill("light goldenrod yellow")
                else:
                    sqr.setFill("PaleGreen4")
                        
            sqr.draw(self.win)
    
    def draw_rest(self):
        self.quit_button = Button(Point(100, 825), 90, 40, "Quit", "tomato")
        self.quit_button.setSize(15)
        self.quit_button.activate()
        self.quit_button.draw(self.win)

        rect1 = Rectangle(Point(100, 195), Point(250, 695))
        rect1.setWidth(0)
        rect1.setFill("sienna")
        rect1.draw(self.win)

        rect2 = Rectangle(Point(250, 195), Point(440, 695))
        rect2.setWidth(0)
        rect2.setFill("sienna4")
        rect2.draw(self.win)

        self.click1 = Button(Point(175, 330), 110, 230, "", "grey20")
        self.click1.activate()
        self.click1.draw(self.win)

        lin1 = Line(Point(120, 445), Point(229, 445))
        lin1.setWidth(3)
        lin1.draw(self.win)

        self.click2 = Button(Point(175, 560), 110, 230, "", "grey12")
        self.click2.activate()
        self.click2.draw(self.win)

        screen = Rectangle(Point(280, 225), Point(410, 665))
        screen.setWidth(0)
        screen.setFill("cornsilk4")
        screen.draw(self.win)

        self.clock1 = Clock('w')
        self.clock1.draw(self.win, "1000")

        self.clock2 = Clock('b')
        self.clock2.draw(self.win, "1000")

        lin2 = Line(Point(290, 444), Point(400, 444))
        lin2.setWidth(2)
        lin2.draw(self.win)

        #inst = 

    def getMouse(self):
        return self.win.getMouse()

    def find_square(self, pt, board):
        for square in board.state:
            x = square.getX() * 100 + 500
            y = square.getY() * 100 - 5
            
            if pt.getX() > (x - 50) and pt.getX() < (x + 50):
                if pt.getY() > (y - 50) and pt.getY() < (y + 50):    
                    return square

    def check_quit(self, pt):
        return self.quit_button.clicked(pt)

    def check_clock(self, pt):
        if self.click1.clicked(pt) or self.click2.clicked(pt):
            return True

    def switch_clock(self):
        if self.click1.getFill() == "grey12":
            self.click1.setFill("grey20")
        else:
            self.click1.setFill("grey12")

        if self.click2.getFill() == "grey12":
            self.click2.setFill("grey20")
        else:
            self.click2.setFill("grey12")

        self.click1.undraw()
        self.click2.undraw()
        self.click1.draw(self.win)
        self.click2.draw(self.win)
        self.click1.activate()
        self.click2.activate()

    def update_clock(self, side, time1, time2):
        if side == 'w':
            sec1 = int(time1[0:2]) * 3600 + int(time1[3:5]) * 60 + int(time1[6:8])
            sec2 = int(time2[0:2]) * 3600 + int(time2[3:5]) * 60 + int(time2[6:8])
            
            sec_time = int(self.clock1.get_time()) - (sec2 - sec1)
            
            print(int(self.clock2.get_time()))
            min = sec_time // 60
            sec = sec_time % 60
            time = str(min) + str(sec)
            time = "0" * abs(len(time) - 4) + time
            print(time)
            
            self.clock1.draw(self.win, time)
            self.clock1.set_time(sec_time)

        elif side == 'b':
            sec1 = int(time1[0:2]) * 3600 + int(time1[3:5]) * 60 + int(time1[6:8])
            sec2 = int(time2[0:2]) * 3600 + int(time2[3:5]) * 60 + int(time2[6:8])
            
            sec_time = int(self.clock2.get_time()) - (sec2 - sec1)
            print(int(self.clock2.get_time()))
            min = sec_time // 60
            sec = sec_time % 60
            time = str(min) + str(sec)
            time = "0" * abs(len(time) - 4) + time
            print(time)
            
            self.clock2.draw(self.win, time)
            self.clock2.set_time(sec_time)

    def change_sqr_color(self, squares, color1, color2):
        for square in squares:
            x = square.getX() * 100 + 500
            y = square.getY() * 100 - 5

            sqr = Rectangle(Point(x - 50, y - 50), Point(x + 50, y + 50))
            sqr.setWidth(0)
                
            if square.getX() % 2 == 0:
                if square.getY() % 2 == 0:
                    sqr.setFill(color1)
                else:
                    sqr.setFill(color2)
            else:
                if square.getY() % 2 == 0:
                    sqr.setFill(color2)
                else:
                    sqr.setFill(color1)
                    
            sqr.draw(self.win)

            p = square.get_piece()
            if p != None:
                self.undraw_piece(p)
                self.draw_piece(p)

    def close(self):
        self.win.close()
        
