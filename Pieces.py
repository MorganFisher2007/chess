from Board import *

state = 

class Piece():
    def __init__(self, color, x: int, y: int):
        self.color = color
        self.x = x
        self.y = y
        
    def __del__():
        pass

    def get_color(self):
        return self.color
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
class Pawn(Piece):
    def __init__(self):
        super().__init__()

    def legal_moves(self, square_list):
        moves = []
        for square in square_list:
            dist_x = self.x - square.getX()
            dist_y = self.y - square.getY()
            if dist_x > 0 and dist_y > 0
            if abs(dist_x) == abs(dist_y):
            if square.getY() > self.y:
                piece_in_path = square.getPiece()
                if piece_in_path == None:
                    moves.append(square)
            
            if square.getY() == self.y: 
            if piece_in_path.get_color() != self.color:
                moves.append(square)

        return moves

class Bishop(Piece):
    def __init__(self):
        super().__init__()

    def legal_moves(self, board: Board):
        moves = []
        i = 0
        while True:
            i += 1
            nxt_x = self.x+i
            nxt_y = self.y+i
            if nxt_x > 8 or nxt_x < 1 or nxt_y > 8 or nxt_y < 1:
                break
            nxt = board.interrogate(nxt_x, nxt_y)
            if type(nxt) == Piece:
                if nxt.color != self.color:
                    # append move, but figure out capturing
                    square = board.get_square(nxt_x, nxt_y)
                    moves.append(square)
                break
            else:
                square = board.get_square(nxt_x, nxt_y)
                moves.append(square)
        i = 0
        while True:
            i += 1
            nxt_x = self.x+i
            nxt_y = self.y-i
            if nxt_x > 8 or nxt_x < 1 or nxt_y > 8 or nxt_y < 1:
                break
            nxt = board.interrogate(nxt_x, nxt_y)
            if type(nxt) == Piece:
                if nxt.color != self.color:
                    # append move, but figure out capturing
                    square = board.get_square(nxt_x, nxt_y)
                    moves.append(square)
                break
            else:
                square = board.get_square(nxt_x, nxt_y)
                moves.append(square)
        i = 0
        while True:
            i += 1
            nxt_x = self.x-i
            nxt_y = self.y+i
            if nxt_x > 8 or nxt_x < 1 or nxt_y > 8 or nxt_y < 1:
                break
            nxt = board.interrogate(nxt_x, nxt_y)
            if type(nxt) == Piece:
                if nxt.color != self.color:
                    # append move, but figure out capturing
                    square = board.get_square(nxt_x, nxt_y)
                    moves.append(square)
                break
            else:
                square = board.get_square(nxt_x, nxt_y)
                moves.append(square)
        i = 0
        while True:
            i += 1
            nxt_x = self.x-i
            nxt_y = self.y-i
            if nxt_x > 8 or nxt_x < 1 or nxt_y > 8 or nxt_y < 1:
                break
            nxt = board.interrogate(nxt_x, nxt_y)
            if type(nxt) == Piece:
                if nxt.color != self.color:
                    # append move, but figure out capturing
                    square = board.get_square(nxt_x, nxt_y)
                    moves.append(square)
                break
            else:
                square = board.get_square(nxt_x, nxt_y)
                moves.append(square)
            
        return moves

class Rook(Piece):
    def __init__(self):
        super().__init__()

    def legal_moves(self, board: Board):
        moves = []
        
        i = 0
        while True:
            i += 1
            nxtx = self.x + i
            if nxtx > 8:
                break
            nxt = board.interrogate(nxtx, self.y)
            if type(nxt) == Piece:
                if nxt.color != self.color:
                    # append move, but figure out capturing
                    square = board.get_square(nxtx, self.y)
                    moves.append(square)
                break
            else:
                square = board.get_square(nxtx, self.y)
                moves.append(square)
        i = 0
        while True:
            i += 1
            nxtx = self.x - i
            if self.x < 1:
                break
            nxt = board.interrogate(nxtx, self.y)
            if type(nxt) == Piece:
                if nxt.color != self.color:
                    # append move, but figure out capturing
                    square = board.get_square(nxtx, self.y)
                    moves.append(square)
                break
            else:
                square = board.get_square(nxtx, self.y)
                moves.append(square)
        i = 0
        while True:
            i += 1
            nxty = self.y + i
            if nxty > 8:
                break
            nxt = board.interrogate(self.x, nxty)
            if type(nxt) == Piece:
                if nxt.color != self.color:
                    # append move, but figure out capturing
                    square = board.get_square(self.x, nxty)
                    moves.append(square)
                break
            else:
                square = board.get_square(self.x, nxty)
                moves.append(square)
        i = 0
        while True:
            i += 1
            nxty = self.y - i
            if nxty < 1:
                break
            nxt = board.interrogate(self.x, nxty)
            if type(nxt) == Piece:
                if nxt.color != self.color:
                    # append move, but figure out capturing
                    square = board.get_square(self.x, nxty)
                    moves.append(square)
                break
            else:
                square = board.get_square(self.x, nxty)
                moves.append(square)
            
        return moves

class Knight(Piece):
    def __init__(self):
        super().__init__()

    def legal_moves(self, board: Board):
        moves = []
        for square in board.state: # we could also just go through each case without looping 64 times
            dist = ((self.x - square.getX())**2 + (self.y - square.getY())**2)**(1/2)
            if dist == (5)**(1/2):

                piece_in_path = square.getPiece()
                if piece_in_path == None:
                    moves.append(square)
                else:
                    if piece_in_path.get_color() != self.color:
                        moves.append(square)
                        
        return moves

class Queen(Rook, Bishop):
    def __init__(self):
        super().__init__()

    def legal_moves():
        super().legal_moves():

        return moves

class King(Piece):
    def __init__(self):
        super().__init__()

    def legal_moves():
        

        return moves
