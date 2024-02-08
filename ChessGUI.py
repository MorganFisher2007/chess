from graphics import *
from Pieces import *
#from screeninfo import get_monitors

class ChessGUI:
    def __init__(self):
        #for m in get_monitors():
            #self.width = m.width
            #self.height = m.height
        self.win = GraphWin("Chess", 1470, 890)
        self.win.setCoords(0, 0, 1470 - 1, 890 - 1)
        self.win.setBackground("grey16")


    def draw_piece(self, piece):
        x = piece.getX() * 100 + 500
        y = piece.getY() * 100 - 5
        IMG_file = piece.getIMG_file()

        IMG = Image(Point(x, y), IMG_file)
        IMG.draw(self.win)

    def draw_squares(self):
        y = -5
        for j in range(1, 9):
            y += 100
            x = 500
            for i in range(1, 9):
                x += 100
                sqr = Rectangle(Point(x - 50, y - 50), Point(x + 50, y + 50))
                sqr.setWidth(0)
                if i % 2 == 0:
                    if j % 2 == 0:
                        sqr.setFill("PaleGreen4")
                    else:
                        sqr.setFill("light goldenrod yellow")
                else:
                    if j % 2 == 0:
                        sqr.setFill("light goldenrod yellow")
                    else:
                        sqr.setFill("PaleGreen4")
                        
                sqr.draw(self.win)