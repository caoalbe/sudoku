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