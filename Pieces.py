from Board import *
import copy

class Piece():
    def __init__(self, color, x: int, y: int):
        self.color = color
        self.x = x
        self.y = y
        self.img_file = ""
        
    def legal_move(self, dx, dy, board, care_check = True):
        m = board.get_square(self.x+dx, self.y+dy)
        if m:
            piece = m.get_piece()
            if piece != None:
                if piece.get_color() != self.color:
                    if care_check: # make sure when we call legal_moves from checkcheck we don't get into recursive loop
                        p = self.move(m.getX(), m.getY(), board) # executing move 
                        check = board.checkcheck()
                        self.undo_move(p, board) # undoing move so board state is not changed
                        if check != False:
                            if self.color in check:
                                return None, True
                    return m, False
                else:
                    return None, False
            else:
                if care_check:
                    p = self.move(m.getX(), m.getY(), board)
                    check = board.checkcheck()
                    self.undo_move(p, board)
                    if check != False:
                        if self.color in check:
                            return None, True
                return m, True
        else:
            return None, False

    def get_color(self):
        return self.color
 
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setPos(self, x, y):
        self.x = x
        self.y = y
    
    def getIMG_file(self):
        return self.img_file

    def setIMG_obj(self, img_obj):
        self.img_obj = img_obj

    def getIMG_obj(self):
        return self.img_obj
    
    def move(self, x, y, board):
        board.get_square(self.x, self.y).clear() # clearing previous piece location
        self.prev_x = self.x
        self.prev_y = self.y
        self.x = x # updating coords
        self.y = y
        return board.get_square(x, y).set_piece(self)
    
    def undo_move(self, piece, board): # takes piece as input to restore possible previous captured piece
        board.get_square(self.x, self.y).clear()
        if isinstance(piece, Piece):
            board.get_square(self.x, self.y).set_piece(piece)
        self.x = self.prev_x
        self.y = self.prev_y
        board.get_square(self.x, self.y).set_piece(self) # moving piece back
    
class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

        if color == "b":
            self.img_file = "bP.png"
        else:
            self.img_file = "wP.png"
    
    def __str__(self):
        "string representation for nogui main"
        return self.color + 'P'

    def legal_moves(self, board, check = True):
        moves = []
        
        if self.color == "b":
            p = board.interrogate(self.x, self.y - 1)
            if p == None:
                square = board.get_square(self.x, self.y - 1)
                moves.append(square)
                
                if self.y == 7:
                    p = board.interrogate(self.x, self.y - 2)
                    if p == None:
                        square = board.get_square(self.x, self.y - 2)
                        moves.append(square)
            
            p = board.interrogate(self.x + 1, self.y - 1)       
            if isinstance(p, Piece):
                if p.get_color() == "w":
                    square = board.get_square(self.x + 1, self.y - 1)
                    moves.append(square)
            
            p = board.interrogate(self.x - 1, self.y - 1) 
            if isinstance(p, Piece):
                if p.get_color() == "w":
                    square = board.get_square(self.x - 1, self.y - 1)
                    moves.append(square)

        else:
            p = board.interrogate(self.x, self.y + 1)
            if p == None:
                square = board.get_square(self.x, self.y + 1)
                moves.append(square)
                
                if self.y == 2:
                    p = board.interrogate(self.x, self.y + 2)
                    if p == None:
                        square = board.get_square(self.x, self.y + 2)
                        moves.append(square)
            
            p = board.interrogate(self.x + 1, self.y + 1)       
            if isinstance(p, Piece):
                if p.get_color() == "b":
                    square = board.get_square(self.x + 1, self.y + 1)
                    moves.append(square)
            
            p = board.interrogate(self.x - 1, self.y + 1) 
            if isinstance(p, Piece):
                if p.get_color() == "b":
                    square = board.get_square(self.x - 1, self.y + 1)
                    moves.append(square)
        if check:
            rem = []
            for move in moves:
                p = self.move(move.getX(), move.getY(), board)
                c = board.checkcheck()
                self.undo_move(p, board)
                if c != False:
                    if self.color in c:
                        rem.append(move)
            for m in rem:
                moves.remove(m)
        return moves

class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

        if color == "b":
            self.img_file = "bB.png"
        else:
            self.img_file = "wB.png"
    
    def __str__(self):
        "string representation for nogui main"
        return self.color + 'B'

    def legal_moves(self, board, check = True):
        moves = []
        i = 0
        while True:
            i += 1
            move, active = super().legal_move(i, i, board, check) # increment i, i for diagnal pattern of bishop (right, up)
            if move != None:
                moves.append(move)
            if active == False: # break loop if piece gets in way
                break
        i = 0
        while True:
            i += 1
            move, active = super().legal_move(-i, i, board, check) # increment -i, i for diagnal pattern of bishop (left, up)
            if move != None:
                moves.append(move)
            if active == False:
                break
        i = 0
        while True:
            i += 1
            move, active = super().legal_move(i, -i, board, check) # increment i, -i for diagnal pattern of bishop (right, down)
            if move != None:
                moves.append(move)
            if active == False:
                break
        i = 0
        while True:
            i += 1
            move, active = super().legal_move(-i, -i, board, check) # increment -i, -i for diagnal pattern of bishop (left, down)
            if move != None:
                moves.append(move)
            if active == False:
                break
        return moves

class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

        if color == "b":
            self.img_file = "bR.png"
        else:
            self.img_file = "wR.png"
    
    def __str__(self):
        "string representation for nogui main"
        return self.color + 'R'

    def legal_moves(self, board, check = True):
        moves = []
        i = 0
        while True:
            i += 1
            move, active = super().legal_move(0, i, board, check) # increment 0, i for straight pattern of rook (no change, up)
            if move != None:
                moves.append(move)
            if active == False:
                break
        i = 0
        while True:
            i += 1
            move, active = super().legal_move(0, -i, board, check) # increment 0, -i for straight pattern of rook (no change, down)
            if move != None:
                moves.append(move)
            if active == False:
                break
        i = 0
        while True:
            i += 1
            move, active = super().legal_move(i, 0, board, check) # increment i, 0 for straight pattern of rook (right, no change)
            if move != None:
                moves.append(move)
            if active == False:
                break
        i = 0
        while True:
            i += 1
            move, active = super().legal_move(-i, 0, board, check) # increment -i, 0 for straight pattern of rook (left, no change)
            if move != None:
                moves.append(move)
            if active == False:
                break
        return moves

class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

        if color == "b":
            self.img_file = "bN.png"
        else:
            self.img_file = "wN.png"
    
    def __str__(self):
        "string representation for nogui main"
        return self.color + 'N'

    def legal_moves(self, board, check = True):
        moves = []
        moves.append(super().legal_move(1, 2, board, check)[0]) # checking each move case individually
        moves.append(super().legal_move(-1, 2, board, check)[0])   
        moves.append(super().legal_move(-1, -2, board, check)[0])      
        moves.append(super().legal_move(1, -2, board, check)[0])
        moves.append(super().legal_move(2, 1, board, check)[0])
        moves.append(super().legal_move(-2, 1, board, check)[0])   
        moves.append(super().legal_move(-2, -1, board, check)[0])      
        moves.append(super().legal_move(2, -1, board, check)[0])
        moves = [move for move in moves if move != None]
        return moves

class Queen(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

        if color == "b":
            self.img_file = "bQ.png"
        else:
            self.img_file = "wQ.png"
    
    def __str__(self):
        "string representation for nogui main"
        return self.color + 'Q'

    def legal_moves(self, board, check = True): # move logic is combination of bishop and rook
        moves = []
        i = 0
        while True:
            i += 1
            move, active = super().legal_move(i, i, board, check)
            if move != None:
                moves.append(move)
            if active == False:
                break
        i = 0
        while True:
            i += 1
            move, active = super().legal_move(-i, i, board, check)
            if move != None:
                moves.append(move)
            if active == False:
                break
        i = 0
        while True:
            i += 1
            move, active = super().legal_move(i, -i, board, check)
            if move != None:
                moves.append(move)
            if active == False:
                break
        i = 0
        while True:
            i += 1
            move, active = super().legal_move(-i, -i, board, check)
            if move != None:
                moves.append(move)
            if active == False:
                break

        i = 0
        while True:
            i += 1
            move, active = super().legal_move(0, i, board, check)
            if move != None:
                moves.append(move)
            if active == False:
                break
        i = 0
        while True:
            i += 1
            move, active = super().legal_move(0, -i, board, check)
            if move != None:
                moves.append(move)
            if active == False:
                break
        i = 0
        while True:
            i += 1
            move, active = super().legal_move(i, 0, board, check)
            if move != None:
                moves.append(move)
            if active == False:
                break
        i = 0
        while True:
            i += 1
            move, active = super().legal_move(-i, 0, board, check)
            if move != None:
                moves.append(move)
            if active == False:
                break
        return moves


class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

        if color == "b":
            self.img_file = "bK.png"
        else:
            self.img_file = "wK.png"
    
    def __str__(self):
        "string representation for nogui main"
        return self.color + 'K'

    def legal_moves(self, board, check = True):
        moves = []
        moves.append(super().legal_move(1, 0, board, check)[0]) # checking each case manually
        moves.append(super().legal_move(1, 1, board, check)[0])
        moves.append(super().legal_move(1, -1, board, check)[0])
        moves.append(super().legal_move(-1, 0, board, check)[0])
        moves.append(super().legal_move(-1, 1, board, check)[0])
        moves.append(super().legal_move(-1, -1, board, check)[0])
        moves.append(super().legal_move(0, 1, board, check)[0])
        moves.append(super().legal_move(0, -1, board, check)[0])
        moves = [move for move in moves if move != None]
        return moves
