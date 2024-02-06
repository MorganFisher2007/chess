from Board import *

class Piece():
    def __init__(self, color, x: int, y: int):
        self.color = color
        self.x = x
        self.y = y
        
    def legal_move(self, dx, dy, board):
        move = board.get_square(self.x+dx, self.y+dy)
        if move:
            piece = move.get_piece()
            if piece != None:
                if piece.get_color() != self.color:
                    return move, False
                else:
                    return None, False
            else:
                return move, True
        else:
            return None, False
    
    '''def __del__(self):
        pass'''

    def get_color(self):
        return self.color
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def move(self, x, y, board):
        board.get_square(self.x, self.y).clear()
        self.x == x
        self.y == y
        board.get_square(x, y).set_piece(self)
    
class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
    
    def __str__(self):
        return self.color + 'P'

    def legal_moves(self, board):
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
    
    def __str__(self):
        return self.color + 'B'

    def legal_moves(self, board):
        moves = []
        i = 0
        while True:
            i += 1
            move, active = super().legal_move(i, i, board)
            if move != None:
                moves.append(move)
            if active == False:
                break
        i = 0
        while True:
            i += 1
            move, active = super().legal_move(-i, i, board)
            if move != None:
                moves.append(move)
            if active == False:
                break
        i = 0
        while True:
            i += 1
            move, active = super().legal_move(i, -i, board)
            if move != None:
                moves.append(move)
            if active == False:
                break
        i = 0
        while True:
            i += 1
            move, active = super().legal_move(-i, -i, board)
            if move != None:
                moves.append(move)
            if active == False:
                break
        return moves

class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
    
    def __str__(self):
        return self.color + 'R'

    def legal_moves(self, board):
        moves = []
        i = 0
        while True:
            i += 1
            move, active = super().legal_move(0, i, board)
            if move != None:
                moves.append(move)
            if active == False:
                break
        i = 0
        while True:
            i += 1
            move, active = super().legal_move(0, -i, board)
            if move != None:
                moves.append(move)
            if active == False:
                break
        i = 0
        while True:
            i += 1
            move, active = super().legal_move(i, 0, board)
            if move != None:
                moves.append(move)
            if active == False:
                break
        i = 0
        while True:
            i += 1
            move, active = super().legal_move(-i, 0, board)
            if move != None:
                moves.append(move)
            if active == False:
                break
        return moves

class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
    
    def __str__(self):
        return self.color + 'K'

    def legal_moves(self, board):
        moves = []
        moves.append(super().legal_move(1, 2, board)[0])
        moves.append(super().legal_move(-1, 2, board)[0])   
        moves.append(super().legal_move(-1, -2, board)[0])      
        moves.append(super().legal_move(1, -2, board)[0])
        moves.append(super().legal_move(2, 1, board)[0])
        moves.append(super().legal_move(-2, 1, board)[0])   
        moves.append(super().legal_move(-2, -1, board)[0])      
        moves.append(super().legal_move(2, -1, board)[0])
        moves = [move for move in moves if move != None]
        return moves

class Queen(Rook, Bishop):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
    
    def __str__(self):
        return self.color + 'Q'

    def legal_moves(self, board):
        moves = []
        moves.append(super().legal_move(1, 2, board))
            
        return moves

class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
    
    def __str__(self):
        return self.color + 'K'

    def legal_moves(self, board):
        moves = []
        return moves
