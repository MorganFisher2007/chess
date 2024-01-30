from Pieces import *

class Square():
    def __init__(self, x, y, piece = None):
        self.x = x
        self.y = y

    def set_piece(self, piece: Piece):
        self.piece = piece
    
    def clear(self):
        self.piece = None
        
    def get_piece(self):
        return self.piece

class Board():
    def __init__(self):
        self.state = []
        for i in range(1, 9):
            for j in range(1, 9):
                self.state.append(Square(i, j))
        
    def interrogate(self, x, y):
        if x > 8 or x < 1 or y < 1 or y > 8:
            return False
        else:
            for square in self.state:
                if square.x == x and square.y == y:
                    return square.get_piece()
    
    def get_square(self, x, y):
        if x > 8 or x < 1 or y < 1 or y > 8:
            return False
        else:
            for square in self.state:
                if square.x == x and square.y == y:
                    return square

