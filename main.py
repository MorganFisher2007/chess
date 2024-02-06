from Board import *
from Pieces import *

def main():
    w_rook1 = Rook("w", 1, 1)
    w_rook2 = Rook("w", 8, 1)
    w_knight1 = Knight("w", 2, 1)
    w_knight2 = Knight("w", 7, 1)
    w_bishop1 = Bishop("w", 3, 1)
    w_bishop2 = Bishop("w", 6, 1)
    w_queen = Queen("w", 4, 1)
    w_king = King("w", 5, 1)

    w_pieces = [w_rook1, w_knight1, w_bishop1, w_queen, w_king, w_bishop2, w_knight2, w_rook2]

    for i in range(8):
        pawn = Pawn("w", i, 2)
        w_pieces.append(pawn)

    b_rook1 = Rook("b", 1, 8)
    b_rook2 = Rook("b", 8, 8)
    b_knight1 = Knight("b", 2, 8)
    b_knight2 = Knight("b", 7, 8)
    b_bishop1 = Bishop("b", 3, 8)
    b_bishop2 = Bishop("b", 6, 8)
    b_queen = Queen("b", 4, 8)
    b_king = King("b", 5, 8)

    b_pieces = [b_rook1, b_knight1, b_bishop1, b_queen, b_king, b_bishop2, b_knight2, b_rook2]

    for i in range(8):
        pawn = Pawn("b", i, 2)
        b_pieces.append(pawn)


    board = Board()
    for i in range(8):
        square = board.get_square(i + 1, 2)
        square.set_piece(w_pieces[8+i])
    
    for i in range(8):
        square = board.get_square(i + 1, 1)
        square.set_piece(w_pieces[i])

    for i in range(8):
        square = board.get_square(i + 1, 8)
        square.set_piece(b_pieces[i])
    
    for i in range(8):
        square = board.get_square(i + 1, 7)
        square.set_piece(b_pieces[8+i])

    turn = 'b'
    print(board)
    while True:
        if turn == 'b':
            turn = 'w'
        elif turn == 'w':
            turn = 'b'
        m = input('enter move \n')
        i = board.interrogate(int(m[0]), int(m[1]))
        f = board.get_square(int(m[2]), int(m[3]))
        if i and f and i.color == turn:
            moves = i.legal_moves(board)
            if moves != None:
                if f in moves:
                    i.move(f.getX(), f.getY(), board)
                    print(board)
                    continue
        print(board)
        print('illegal move, motherfucker!')


main()