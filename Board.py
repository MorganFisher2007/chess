from Pieces import *
import copy

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
    
    def inst_str(self):
        letters = ["a", "b", "c", "c", "e", "f", "g", "h"]
        return letters[self.x - 1] + str(self.y)

    def set_piece(self, piece):
        out = self.piece
        self.piece = piece
        return out

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
        for j in range(1, 9):
            for i in range(1, 9):
                self.state.append(Square(i, j))
    
    def __str__(self):
        "string representation for nogui main"
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
        
    def interrogate(self, x, y): # directly returns piece from coords, bypassing having to access the square
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
        out = []
        for square in self.state:
            piece = square.get_piece()
            if piece == None:
                continue
            if str(piece) == 'wK':
                wKing = self.get_square(piece.getX(), piece.getY())
            elif str(piece) == 'bK':
                bKing = self.get_square(piece.getX(), piece.getY())
        for square in self.state:
            piece = square.get_piece()
            if piece == None:
                continue
            if piece.color == 'w': # loop through all pieces of given color
                for move in piece.legal_moves(self, False): # if the piece can capture king on next move, it is check
                    if move == bKing:
                        out += 'b'
            else:
                for move in piece.legal_moves(self, False):
                    if move == wKing:
                        out += 'w'
        if out == []:
            return False
        else:
            return out

    def checkmate(self):
        p = []
        cc = self.checkcheck()
        for square in self.state:
            piece = square.get_piece()
            if isinstance(piece, Piece):
                p.append(piece)
        if cc == False:
            return False
        if 'w' in cc: # king must be in check for checkmate
            for piece in p:
                if piece.color == 'w':
                    for m in piece.legal_moves(self): # if no moves are possible, it is checkmate
                        p = piece.move(m.getX(), m.getY(), self)
                        c = self.checkcheck()
                        piece.undo_move(p, self)
                        if c == False:
                            return False
                        if 'w' not in c:
                            return False
            return True
        
        elif 'b' in cc:
            for piece in p:
                if piece.color == 'b':
                    for m in piece.legal_moves(self):
                        p = piece.move(m.getX(), m.getY(), self)
                        c = self.checkcheck()
                        piece.undo_move(p, self)
                        if c == False:
                            return False
                        if 'b' not in c:
                            return False
            return True
        return False
    
    def check_promote(self): # checks if a pawn is on the 8th or 1st rank, and if so returns the piece to be promoted
        for square in self.state:
            piece = square.get_piece()
            if type(piece) == Pawn:
                if piece.getY() in [1, 8]:
                    return piece
        return False
    
    def promote(self, Piece): # replaces pawn with chosen piece
        piece = self.check_promote()
        x = piece.getX()
        y = piece.getY()
        color = piece.get_color()
        square = self.get_square(x, y)
        square.clear()
        square.set_piece(Piece(color, x, y))
