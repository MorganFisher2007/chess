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
        
    def copy_state(self):
        new_state = []
        for j in range(1, 9):
            for i in range(1, 9):
                sqr = Square(i, j)
                new_state.append(sqr)
                p = self.get_square(i, j).get_piece()
                if p != None:
                    if type(p) == Pawn:
                        ghostp = Pawn(p.color, p.getX(), p.getY())
                    elif type(p) == Rook:
                        ghostp = Rook(p.color, p.getX(), p.getY())
                    elif type(p) == Bishop:
                        ghostp = Bishop(p.color, p.getX(), p.getY())
                    elif type(p) == Knight:
                        ghostp = Knight(p.color, p.getX(), p.getY())
                    elif type(p) == Queen:
                        ghostp = Pawn(p.color, p.getX(), p.getY())
                    elif type(p) == King:
                        ghostp = King(p.color, p.getX(), p.getY())
                
                if ghostp != None:
                    sqr.set_piece(ghostp)
        
        return new_state

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
                for move in piece.legal_moves(self, check = False):
                    if move == bKing:
                        return 'b'
            else:
                for move in piece.legal_moves(self, check = False):
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
                tboard = Board()
                tboard.state = self.copy_state()
                tboard.remove_images()
                tking = tboard.interrogate(wKing.getX(), wKing.getY())
                tking.move(move)
                if tboard.checkcheck() == False:
                    return False
            return True
        
        elif self.checkcheck() == 'b':
            for move in bKing.legal_moves():
                tboard = Board()
                tboard.state = self.copy_state()
                tboard.remove_images()
                tking = tboard.interrogate(bKing.getX(), bKing.getY())
                tking.move(move)
                if tboard.checkcheck() == False:
                    return False
            return True
        return False
    
    def check_promote(self):
        for square in self.state:
            piece = square.get_piece()
            if type(piece) == Pawn:
                if piece.getY() in [1, 8]:
                    return piece
        return False
    
    def promote(self, Piece):
        piece = self.check_promote()
        x = piece.getX()
        y = piece.getY()
        color = piece.get_color()
        square = self.get_square(x, y)
        square.clear()
        square.set_piece(Piece(color, x, y))
    
    def lead_check(self, piece, move):
        old_state = self.state
        piece.move(move.getX(), move.getY(), self)
        out = self.checkcheck()
        self.state = old_state
        return out
    
    def remove_images(self):
        '''for square in self.state:
            piece = square.get_piece()
            piece.img_file = None
            piece.obj = None'''
        pass
