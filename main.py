from Board import *
from Pieces import *
from ChessGUI import *
import time

#ADD COMMENTS BUDDY

def main():
    win = ChessGUI()

    # Making white pieces
    w_rook1 = Rook("w", 1, 1)
    w_rook2 = Rook("w", 8, 1)
    w_knight1 = Knight("w", 2, 1)
    w_knight2 = Knight("w", 7, 1)
    w_bishop1 = Bishop("w", 3, 1)
    w_bishop2 = Bishop("w", 6, 1)
    w_queen = Queen("w", 4, 1)
    w_king = King("w", 5, 1)

    w_pieces = [w_rook1, w_knight1, w_bishop1, w_queen, w_king, w_bishop2,
                w_knight2, w_rook2]

    for i in range(8):
        pawn = Pawn("w", i + 1, 2)
        w_pieces.append(pawn)

    # Making black pieces
    b_rook1 = Rook("b", 1, 8)
    b_rook2 = Rook("b", 8, 8)
    b_knight1 = Knight("b", 2, 8)
    b_knight2 = Knight("b", 7, 8)
    b_bishop1 = Bishop("b", 3, 8)
    b_bishop2 = Bishop("b", 6, 8)
    b_queen = Queen("b", 4, 8)
    b_king = King("b", 5, 8)

    b_pieces = [b_rook1, b_knight1, b_bishop1, b_queen, b_king, b_bishop2,
                b_knight2, b_rook2]

    for i in range(8):
        pawn = Pawn("b", i + 1, 7)
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

    # Drawing everything
    win.draw_inst("Welcome to Chess!")
    win.draw_rest()
    win.draw_squares(board)

    for w_piece in w_pieces:
        win.draw_piece(w_piece)

    for b_piece in b_pieces:
        win.draw_piece(b_piece)

    # Actual gameplay
    turn = 'w'
    while True:
        if turn == 'w':
            w_time1 = time.strftime("%H:%M:%S")
            win.set_inst("It is white's move")
        else:
            b_time1 = time.strftime("%H:%M:%S")
            win.set_inst("It is black's move")
            
        while True:
            pt1 = win.getMouse()
            
            if win.check_quit(pt1):
                win.close()
                return
            
            elif pt1.getX() >= 550 and pt1.getX() <= 1350:
                if pt1.getY() >= 45 and pt1.getY() <= 845:
                    sqr = win.find_square(pt1, board)
                    i = board.interrogate(sqr.getX(), sqr.getY())

                    if i and i.color == turn:
                        moves = i.legal_moves(board)
                        win.change_sqr_color(moves, "yellow3", "yellow2")

                        if len(moves) == 0:
                            continue

                        break

        while True:
            pt2 = win.getMouse()

            if win.check_quit(pt1):
                win.close()
                return
            
            elif pt2.getX() >= 550 and pt2.getX() <= 1350:
                if pt2.getY() >= 45 and pt2.getY() <= 845:
                    f = win.find_square(pt2, board)

                    if f in moves:
                        win.undraw_piece(i)
                        i.move(f.getX(), f.getY(), board)
                        if board.check_promote() != False:
                            ox = board.check_promote().getX()
                            oy = board.check_promote().getY()
                            prompt_piece = win.ask_promote(i)
                            board.promote(prompt_piece)
                            i = board.interrogate(ox, oy)
                        win.draw_piece(i)
                        win.change_sqr_color(moves, "PaleGreen4",
                                             "light goldenrod yellow")
                        
                        win.set_inst(str(i) + " moved to " + str(f.inst_str()))

                        cont = False    
                        break

                    else:
                        win.change_sqr_color(moves, "PaleGreen4",
                                             "light goldenrod yellow")
                        cont = True
                        break

        if cont == True:
            continue

        while True:
            pt3 = win.getMouse()
            
            if win.check_clock(pt3):
                time2 = time.strftime("%H:%M:%S")
                if turn == 'w':
                    win.switch_clock()
                    win.update_clock('w', w_time1, time2)
                else:
                    win.switch_clock()
                    win.update_clock('b', b_time1, time2)
                break

            elif win.check_quit(pt3):
                win.close()
                return
        
        if turn == 'b':
            print(board.checkmate())
            turn = 'w'
        elif turn == 'w':
            print(board.checkmate())
            turn = 'b'
        


main()
