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
        del self.piece
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
        for j in range(1, 9):
            for i in range(1, 9):
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
            if piece.color == 'w':
                for move in piece.legal_moves(self):
                    if move == bKing:
                        return 'b'
            else:
                for move in piece.legal_moves(self):
                    if move == wKing:
                        return 'w'
        return False

    def checkmate(self):
        for square in self.state:
            piece = square.get_piece()
            if str(piece) == 'wK':
                wKing = piece
            elif str(piece) == 'bK':
                bKing = piece
        if self.checkcheck() == 'w':
            for move in wKing.legal_moves():
                tboard = self
                tking = tboard.interrogate(wKing.getX(), wKing.getY())
                tking.move(move)
                if tboard.checkcheck() == False:
                    return False
            return True
        
        elif self.checkcheck() == 'b':
            for move in bKing.legal_moves():
                tboard = self
                tking = tboard.interrogate(bKing.getX(), bKing.getY())
                tking.move(move)
                if tboard.checkcheck() == False:
                    return False
            return True
        return False

    def check_promote(self):
            for square in self.state():
                piece = square.get_piece()
                if type(piece) == Pawn:
                    if piece.getY in [1, 8]:
                        return piece
            return False
