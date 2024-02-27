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
                    if care_check:
                        p = self.move(m.getX(), m.getY(), board)
                        check = board.checkcheck()
                        self.undo_move(p, board)
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
        board.get_square(self.x, self.y).clear()
        self.prev_x = self.x
        self.prev_y = self.y
        self.x = x
        self.y = y
        return board.get_square(x, y).set_piece(self)
    
    def undo_move(self, piece, board):
        board.get_square(self.x, self.y).clear()
        if isinstance(piece, Piece):
            board.get_square(self.x, self.y).set_piece(piece)
        self.x = self.prev_x
        self.y = self.prev_y
        board.get_square(self.x, self.y).set_piece(self)
    
class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

        if color == "b":
            self.img_file = "bP.png"
        else:
            self.img_file = "wP.png"
    
    def __str__(self):
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
        return self.color + 'B'

    def legal_moves(self, board, check = True):
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
        return moves

class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

        if color == "b":
            self.img_file = "bR.png"
        else:
            self.img_file = "wR.png"
    
    def __str__(self):
        return self.color + 'R'

    def legal_moves(self, board, check = True):
        moves = []
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
        '''if check == True:
            print(moves)'''
        return moves

class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

        if color == "b":
            self.img_file = "bN.png"
        else:
            self.img_file = "wN.png"
    
    def __str__(self):
        return self.color + 'N'

    def legal_moves(self, board, check = True):
        moves = []
        moves.append(super().legal_move(1, 2, board, check)[0])
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
        self.v = Rook(self.color, self.x, self.y)
        self.d = Bishop(self.color, self.x, self.y)

        if color == "b":
            self.img_file = "bQ.png"
        else:
            self.img_file = "wQ.png"
    
    def __str__(self):
        return self.color + 'Q'

    def legal_moves(self, board, check = True):
        self.v.setPos(self.x, self.y)
        self.d.setPos(self.x, self.y)
        out = self.v.legal_moves(board, check) + self.d.legal_moves(board, check)
        if check == True:
            print(out)
        return out

class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

        if color == "b":
            self.img_file = "bK.png"
        else:
            self.img_file = "wK.png"
    
    def __str__(self):
        return self.color + 'K'

    def legal_moves(self, board, check = True):
        moves = []
        moves.append(super().legal_move(1, 0, board, check)[0])
        moves.append(super().legal_move(1, 1, board, check)[0])
        moves.append(super().legal_move(1, -1, board, check)[0])
        moves.append(super().legal_move(-1, 0, board, check)[0])
        moves.append(super().legal_move(-1, 1, board, check)[0])
        moves.append(super().legal_move(-1, -1, board, check)[0])
        moves.append(super().legal_move(0, 1, board, check)[0])
        moves.append(super().legal_move(0, -1, board, check)[0])
        moves = [move for move in moves if move != None]
        return moves
