from Pieces import *

class Square():
    def __init__(self, x, y, piece = None):
        self.x = x
        self.y = y
        self.piece = piece
    
    def __str__(self):
        if self.piece != None:
            return str(self.piece)
        else:
            return ''

    def set_piece(self, piece):
        self.piece = piece
    
    def clear(self):
        self.piece = None
        
    def get_piece(self):
        return self.piece
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

class Board():
    def __init__(self):
        self.state = []
        for i in range(1, 9):
            for j in range(1, 9):
                self.state.append(Square(i, j))
    
    def __str__(self):
        out = ''
        squares = []
        for j in range(8):
            out += '\n'*2
            for i in range(1, 9):
                out += "\t"
                sqr = str(self.get_square(i, 8-j))
                if sqr == '':
                    out += "_"
                out += (str(self.get_square(i, 8-j)))
    
        return out
        
    def interrogate(self, x, y):
        if x > 8 or x < 1 or y < 1 or y > 8:
            return False
        else:
            for square in self.state:
                if square.getX() == x and square.getY() == y:
                    return square.get_piece()
    
    def get_square(self, x, y):
        if x > 8 or x < 1 or y < 1 or y > 8:
            return False
        else:
            for square in self.state:
                if square.getX() == x and square.getY() == y:
                    return square
    
    def checkcheck(self):
        for piece in self.state:
            if piece.color == 'w':
                if #blackking is in legal moves of each piece
            else:
