from Board import *

state = 

class Piece():
    def __init__(self, color, x: int, y: int):
        self.color = color
        self.x = x
        self.y = y
        
    def legal_move(self, dx, dy, board: Board):
        move = board.get_square(self.x+dx, self.y+dy)
        if move:
            if type(move.get_piece) == Piece:
                if move.color != self.color:
                    return move
            else:
                return move
        else:
            return False
    
    def __del__():
        pass

    def get_color(self):
        return self.color
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def legal_moves(self, board: Board):
        moves = []
        
        if self.color == "b":
            if self.y == 7:
                if board.interrogate(self.x, self.y - 2) == Piece:
                    if not Piece.get_color() == "w":
                        square = board.get_square(self.x + 1, self.y - 2)
                        moves.append(square)
                    
            if board.interrogate(self.x + 1, self.y - 1) == Piece:
                if Piece.get_color() == "w":
                    square = board.get_square(self.x + 1, self.y - 1)
                    moves.append(square)

            if board.interrogate(self.x - 1, self.y - 1) == Piece:
                if Piece.get_color() == "w":
                    square = board.get_square(self.x - 1, self.y - 1)
                    moves.append(square)
                
            if board.interrogate(self.x, self.y - 1) != Piece:
                square = board.get_square(self.x, self.y - 1)
                moves.append(square)

        else:
            if self.y == 2:
                if board.interrogate(self.x, self.y + 2) == Piece:
                    if not Piece.get_color() == "w":
                        square = board.get_square(self.x + 1, self.y + 2)
                        moves.append(square)
                    
            if board.interrogate(self.x + 1, self.y + 1) == Piece:
                if Piece.get_color() == "w":
                    square = board.get_square(self.x + 1, self.y + 1)
                    moves.append(square)

            if board.interrogate(self.x - 1, self.y + 1) == Piece:
                if Piece.get_color() == "w":
                    square = board.get_square(self.x - 1, self.y + 1)
                    moves.append(square)
                
            if board.interrogate(self.x, self.y + 1) != Piece:
                square = board.get_square(self.x, self.y + 1)
                moves.append(square)

class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def legal_moves(self, board: Board):
        moves = []
        i = 0
        while True:
            i += 1
            move = super().legal_move(i, i)
            if move:
                moves.append(move)
                continue
            break
        i = 0
        while True:
            i += 1
            move = super().legal_move(i, -i)
            if move:
                moves.append(move)
                continue
            break
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
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

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
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def legal_moves(self, board: Board):
        moves = []
        moves.append(super().legal_move(1, 2))
        moves.append(super().legal_move(-1, 2))   
        moves.append(super().legal_move(-1, -2))      
        moves.append(super().legal_move(1, -2))
        moves.append(super().legal_move(2, 1))
        moves.append(super().legal_move(-2, 1))   
        moves.append(super().legal_move(-2, -1))      
        moves.append(super().legal_move(2, -1))        
        
        return moves

class Queen(Rook, Bishop):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def legal_moves():
        moves = []
        moves.append(super().legal_moves(1, 2))
            
        return moves

class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def legal_moves():
        

        return moves
