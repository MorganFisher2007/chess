from graphics import *
from Pieces import *
from Button import Button
from Clock import Clock

class ChessGUI:
    def __init__(self):
        self.win = GraphWin("Chess", 1470, 890, autoflush = False)
        self.win.setCoords(0, 0, 1470 - 1, 890 - 1)
        self.win.setBackground("grey16")

        # list of drawn stuff (so I can undraw later)
        self.drawn_list = []

    def draw_piece(self, piece):
        "draws given piece"
        x = piece.getX() * 100 + 498
        y = piece.getY() * 100 - 5
        IMG_file = piece.getIMG_file()

        IMG = Image(Point(x, y), IMG_file)
        piece.setIMG_obj(IMG)
        IMG.draw(self.win)
        self.drawn_list.append(IMG)

    def undraw_piece(self, piece):
        "undraws given piece"
        IMG = piece.getIMG_obj()
        IMG.undraw()
        self.drawn_list.remove(IMG)

    def draw_squares(self, board):
        "draw squares"
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
            self.drawn_list.append(sqr)
    
    def draw_rest(self):
        "draws clock, board letters/numbers, buttons"
        letters = ["a", "b", "c", "c", "e", "f", "g", "h"]

        for i in range(1, 9):
            txt = Text(Point(1370, i * 100 - 5), str(i))
            txt.setTextColor("white")
            txt.draw(self.win)
            self.drawn_list.append(txt)

        i = 0
        for letter in letters:
            i += 1
            txt = Text(Point(i * 100 + 500, 860), letter)
            txt.setTextColor("white")
            txt.draw(self.win)
            self.drawn_list.append(txt)
        
        self.quit_button = Button(Point(100, 825), 90, 40, "Quit", "tomato")
        self.quit_button.setSize(15)
        self.quit_button.activate()
        self.quit_button.draw(self.win)
        self.drawn_list.append(self.quit_button)

        self.start_button = Button(Point(450, 825), 90, 40, "Start", "LightBlue1")
        self.start_button.setSize(15)
        self.start_button.activate()
        self.start_button.draw(self.win)
        self.drawn_list.append(self.start_button)

        self.rect1 = Rectangle(Point(100, 195), Point(250, 695))
        self.rect1.setWidth(0)
        self.rect1.setFill("sienna")
        self.rect1.draw(self.win)
        self.drawn_list.append(self.rect1)

        self.rect2 = Rectangle(Point(250, 195), Point(440, 695))
        self.rect2.setWidth(0)
        self.rect2.setFill("sienna4")
        self.rect2.draw(self.win)
        self.drawn_list.append(self.rect2)

        self.click1 = Button(Point(175, 330), 110, 230, "", "grey20")
        self.click1.activate()
        self.click1.draw(self.win)
        self.drawn_list.append(self.click1)

        self.lin1 = Line(Point(120, 445), Point(229, 445))
        self.lin1.setWidth(3)
        self.lin1.draw(self.win)
        self.drawn_list.append(self.lin1)

        self.click2 = Button(Point(175, 560), 110, 230, "", "grey12")
        self.click2.activate()
        self.click2.draw(self.win)
        self.drawn_list.append(self.click2)

        self.screen = Rectangle(Point(280, 225), Point(410, 665))
        self.screen.setWidth(0)
        self.screen.setFill("cornsilk4")
        self.screen.draw(self.win)
        self.drawn_list.append(self.screen)

        self.clock1 = Clock('w')
        self.clock1.draw(self.win, "1000")
        self.drawn_list.append(self.clock1)

        self.clock2 = Clock('b')
        self.clock2.draw(self.win, "1000")
        self.drawn_list.append(self.clock2)

        self.lin2 = Line(Point(290, 444), Point(400, 444))
        self.lin2.setWidth(2)
        self.lin2.draw(self.win)
        self.drawn_list.append(self.lin2)

    def draw_inst(self, text):
        "draw instructions"
        self.inst = Text(Point(270, 115), text)
        self.inst.setTextColor("white")
        self.inst.setSize(20)
        self.inst.draw(self.win)
        self.drawn_list.append(self.inst)

    def set_inst(self, text):
        self.inst.setText(text)

    def getMouse(self):
        return self.win.getMouse()

    def find_square(self, pt, board):
        "returns square that matches the point clicked"
        for square in board.state:
            x = square.getX() * 100 + 500
            y = square.getY() * 100 - 5
            
            if pt.getX() > (x - 50) and pt.getX() < (x + 50):
                if pt.getY() > (y - 50) and pt.getY() < (y + 50):    
                    return square

    def check_quit(self, pt):
        return self.quit_button.clicked(pt)

    def check_start(self, pt):
        return self.start_button.clicked(pt)

    def change_start(self, activate, text="Play Again"):
        "changes text of start button"
        if activate:
            self.start_button.activate()
        else:
            self.start_button.deactivate()

        self.start_button.setLabel(text)

    def check_clock(self, pt):
        "checks if clock has been clicked"
        if self.click1.clicked(pt) or self.click2.clicked(pt):
            return True

    def switch_clock(self):
        "changes clock button colors"
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
        "updates clock given two timestamps
        if side == 'w':
            # converts given time stamp into seconds
            sec1 = int(time1[0:2]) * 3600 + int(time1[3:5]) * 60 + int(time1[6:8])
            sec2 = int(time2[0:2]) * 3600 + int(time2[3:5]) * 60 + int(time2[6:8])
            
            sec_time = int(self.clock1.get_time()) - (sec2 - sec1)
            
            if sec_time > 0:
                # converting sec_time into string of four numbers in minute-second
                # form
                mins = sec_time // 60
                secs = sec_time % 60
                time = str(mins) + str(secs)
                time = "0" * abs(len(time) - 4) + time
                
                self.clock1.draw(self.win, time)
                self.clock1.set_time(str(time))
                
                # time is still going so the game isn't done and there is no
                # winner
                return False, None

            else:
                time = "0000"
                
                self.clock1.draw(self.win, time)
                self.clock1.set_time(str(time))
                
                # time ran out so the game is done and there's a winner
                return True, "b"

        elif side == 'b':
            sec1 = int(time1[0:2]) * 3600 + int(time1[3:5]) * 60 + int(time1[6:8])
            sec2 = int(time2[0:2]) * 3600 + int(time2[3:5]) * 60 + int(time2[6:8])
            
            sec_time = int(self.clock2.get_time()) - (sec2 - sec1)

            if sec_time > 0:
                mins = sec_time // 60
                secs = sec_time % 60
                time = str(mins) + str(secs)
                time = "0" * abs(len(time) - 4) + time
                
                self.clock2.draw(self.win, time)
                self.clock2.set_time(str(time))

                return False, None

            else:
                time = "0000"
                
                self.clock2.draw(self.win, time)
                self.clock2.set_time(str(time))
                
                return True, "w"

    def change_sqr_color(self, squares, color1, color2):
        "changes color of square"
        # used to go back and forth between being lit up and normal
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

            # undrawing/redrawing piece (if there is one) so square doesn't
            # cover it
            p = square.get_piece()
            if p != None:
                self.undraw_piece(p)
                self.draw_piece(p)

    def ask_promote(self, piece):
        "creates prompt menu and returns promote piece"
        # checks where on the board the menu has to be
        x = piece.getX() * 100 + 498
        if piece.getY() == 1:
            y = 100
        else:
            y = 800
        
        prompt = Rectangle(Point(x - 140, y), Point(x + 140, y))
        prompt.draw(self.win)

        # creating image buttons
        Nbutton = Button(Point(x - 105, y), 70, 70, "", "white")
        Bbutton = Button(Point(x - 35, y), 70, 70, "", "white")
        Rbutton = Button(Point(x + 35, y), 70, 70, "", "white")
        Qbutton = Button(Point(x + 105, y), 70, 70, "", "white")

        if piece.get_color() == "w":
            Nbutton.setIMG("wN.png")
            Bbutton.setIMG("wB.png")
            Rbutton.setIMG("wR.png")
            Qbutton.setIMG("wQ.png")
        else:
            Nbutton.setIMG("bN.png")
            Bbutton.setIMG("bB.png")
            Rbutton.setIMG("bR.png")
            Qbutton.setIMG("bQ.png")

        Nbutton.draw(self.win)
        Nbutton.activate()
        Bbutton.draw(self.win)
        Bbutton.activate()
        Rbutton.draw(self.win)
        Rbutton.activate()
        Qbutton.draw(self.win)
        Qbutton.activate()

        # gets click and sets the chosen piece equal to the class
        while True:
            pt = self.win.getMouse()

            if Nbutton.clicked(pt):
                p = Knight
                break
            elif Bbutton.clicked(pt):
                p = Bishop
                break
            elif Rbutton.clicked(pt):
                p = Rook
                break
            elif Qbutton.clicked(pt):
                p = Queen
                break

        Nbutton.undraw()
        Bbutton.undraw()
        Rbutton.undraw()
        Qbutton.undraw()
        prompt.undraw()

        return p

    def undraw_all(self):
        "undraws everything in GUI"
        for item in self.drawn_list:
            item.undraw()

    def close(self):
        self.win.close()
