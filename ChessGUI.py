from graphics import *
from Pieces import *
from Button import Button

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
        quit_button = Button(Point(100, 825), 90, 40, "Quit", "tomato")
        quit_button.setSize(15)
        quit_button.activate()
        quit_button.draw(self.win)

        clock_base = Rectangle(Point(100, 195), Point(440, 695))
        clock_base.setWidth(0)
        clock_base.setFill("sienna4")
        clock_base.draw(self.win)

        click1 = Rectangle(Point(120, 215), Point(230, 445))
        click1.setFill("grey12")
        click1.setWidth(0)
        click1.draw(self.win)

        lin1 = Line(Point(120, 445), Point(229, 445))
        lin1.setWidth(3)
        lin1.draw(self.win)

        click2 = Rectangle(Point(120, 445), Point(230, 675))
        click2.setFill("grey20")
        click2.setWidth(0)
        click2.draw(self.win)

        screen = Rectangle(Point(260, 225), Point(410, 665))
        screen.setWidth(0)
        screen.setFill("cornsilk4")
        screen.draw(self.win)

        for i in range(4):
            txt1 = Text(Point(335, 245 + i * 50), "–– ––")
            txt1.setSize(36)

            txt2 = Text(Point(290, 259 + i * 50), "l")
            txt2.setSize(36)

            txt3 = Text(Point(335, 280 + i * 50), "–– ––")
            txt3.setSize(36)

            txt4 = Text(Point(380, 259 + i * 50), "l")
            txt4.setSize(36)

            if i == 0:
                txt1.setTextColor("grey50")
                txt2.setTextColor("grey50")
                txt4.setTextColor("grey50")
            
            txt1.draw(self.win)
            txt2.draw(self.win)
            txt3.draw(self.win)
            txt4.draw(self.win)

        colon = Text(Point(335, 345), ".  .")
        colon.setSize(36)
        colon.draw(self.win)
        
        lin2 = Line(Point(280, 444), Point(390, 444))
        lin2.setWidth(2)
        lin2.draw(self.win)
        
        for i in range(4):
            txt5 = Text(Point(335, 465 + i * 50), "–– ––")
            txt5.setSize(36)

            txt6 = Text(Point(290, 479 + i * 50), "l")
            txt6.setSize(36)

            txt7 = Text(Point(335, 500 + i * 50), "–– ––")
            txt7.setSize(36)

            txt8 = Text(Point(380, 479 + i * 50), "l")
            txt8.setSize(36)

            if i == 0:
                txt5.setTextColor("grey50")
                txt6.setTextColor("grey50")
                txt8.setTextColor("grey50")
            
            txt5.draw(self.win)
            txt6.draw(self.win)
            txt7.draw(self.win)
            txt8.draw(self.win)

        colon = Text(Point(335, 565), ".  .")
        colon.setSize(36)
        colon.draw(self.win)

    def getMouse(self):
        return self.win.getMouse()

    def check_square(self, pt, board):
        for square in board.state:
            x = square.getX() * 100 + 500
            y = square.getY() * 100 - 5
            
            if pt.getX() > (x - 50) and pt.getX() < (x + 50):
                if pt.getY() > (y - 50) and pt.getY() < (y + 50):    
                    return square

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
                
