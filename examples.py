import SudokuGame


def create_example1():
    game = SudokuGame.Sudoku_Board()

    game.set_board(1, 2, 8)
    game.set_board(1, 5, 7)
    game.set_board(1, 7, 3)
    game.set_board(1, 9, 5)

    game.set_board(2, 1, 2)
    game.set_board(2, 2, 5)
    game.set_board(2, 3, 7)
    game.set_board(2, 6, 8)
    game.set_board(2, 8, 9)
    game.set_board(2, 9, 6)

    game.set_board(3, 6, 5)
    game.set_board(3, 8, 7)

    game.set_board(4, 1, 4)
    game.set_board(4, 3, 9)
    game.set_board(4, 4, 3)
    game.set_board(4, 5, 6)

    game.set_board(5, 2, 6)
    game.set_board(5, 3, 1)
    game.set_board(5, 8, 4)

    game.set_board(6, 1, 3)
    game.set_board(6, 2, 7)
    game.set_board(6, 3, 8)
    game.set_board(6, 5, 1)
    game.set_board(6, 8, 2)

    game.set_board(7, 2, 3)
    game.set_board(7, 6, 1)
    game.set_board(7, 7, 9)
    game.set_board(7, 9, 4)

    game.set_board(8, 1, 7)
    game.set_board(8, 3, 5)
    game.set_board(8, 7, 1)
    game.set_board(8, 8, 8)
    game.set_board(8, 9, 2)

    game.set_board(9, 3, 6)
    game.set_board(9, 4, 4)
    game.set_board(9, 5, 8)
    game.set_board(9, 6, 2)
    game.set_board(9, 7, 5)

    return game


def create_example2():
    # This is a complete board
    game = SudokuGame.Sudoku_Board()

    game.set_board(1, 1, 5)
    game.set_board(1, 2, 3)
    game.set_board(1, 3, 4)
    game.set_board(1, 4, 6)
    game.set_board(1, 5, 7)
    game.set_board(1, 6, 8)
    game.set_board(1, 7, 9)
    game.set_board(1, 8, 1)
    game.set_board(1, 9, 2)

    game.set_board(2, 1, 6)
    game.set_board(2, 2, 7)
    game.set_board(2, 3, 2)
    game.set_board(2, 4, 1)
    game.set_board(2, 5, 9)
    game.set_board(2, 6, 5)
    game.set_board(2, 7, 3)
    game.set_board(2, 8, 4)
    game.set_board(2, 9, 8)

    game.set_board(3, 1, 1)
    game.set_board(3, 2, 9)
    game.set_board(3, 3, 8)
    game.set_board(3, 4, 3)
    game.set_board(3, 5, 4)
    game.set_board(3, 6, 2)
    game.set_board(3, 7, 5)
    game.set_board(3, 8, 6)
    game.set_board(3, 9, 7)

    game.set_board(4, 1, 8)
    game.set_board(4, 2, 5)
    game.set_board(4, 3, 9)
    game.set_board(4, 4, 7)
    game.set_board(4, 5, 6)
    game.set_board(4, 6, 1)
    game.set_board(4, 7, 4)
    game.set_board(4, 8, 2)
    game.set_board(4, 9, 3)

    game.set_board(5, 1, 4)
    game.set_board(5, 2, 2)
    game.set_board(5, 3, 6)
    game.set_board(5, 4, 8)
    game.set_board(5, 5, 5)
    game.set_board(5, 6, 3)
    game.set_board(5, 7, 7)
    game.set_board(5, 8, 9)
    game.set_board(5, 9, 1)

    game.set_board(6, 1, 7)
    game.set_board(6, 2, 1)
    game.set_board(6, 3, 3)
    game.set_board(6, 4, 9)
    game.set_board(6, 5, 2)
    game.set_board(6, 6, 4)
    game.set_board(6, 7, 8)
    game.set_board(6, 8, 5)
    game.set_board(6, 9, 6)

    game.set_board(7, 1, 9)
    game.set_board(7, 2, 6)
    game.set_board(7, 3, 1)
    game.set_board(7, 4, 5)
    game.set_board(7, 5, 3)
    game.set_board(7, 6, 7)
    game.set_board(7, 7, 2)
    game.set_board(7, 8, 8)
    game.set_board(7, 9, 4)

    # game.set_board(8, 1, 2)
    # game.set_board(8, 2, 8)
    # game.set_board(8, 3, 7)
    # game.set_board(8, 4, 4)
    # game.set_board(8, 5, 1)
    # game.set_board(8, 6, 9)
    # game.set_board(8, 7, 6)
    # game.set_board(8, 8, 3)
    # game.set_board(8, 9, 5)

    # game.set_board(9, 1, 3)
    # game.set_board(9, 2, 4)
    # game.set_board(9, 3, 5)
    # game.set_board(9, 4, 2)
    # game.set_board(9, 5, 8)
    # game.set_board(9, 6, 6)
    # game.set_board(9, 7, 1)
    # game.set_board(9, 8, 7)
    # game.set_board(9, 9, 9)

    return game
