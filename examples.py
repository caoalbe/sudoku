# Albert Cao

from Sudoku_Board import Sudoku_Board
from random import sample


def random_example():
    funcs = [example1, example2, example3, example4]
    chosen_function = sample(funcs, 1)[0]
    game = chosen_function()
    return game


def example1():
    game = Sudoku_Board()

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


def example2():
    # Easy Puzzle
    game = Sudoku_Board()

    game.set_board(1, 1, 6)
    game.set_board(1, 3, 2)
    game.set_board(1, 4, 4)
    game.set_board(1, 5, 1)
    game.set_board(1, 9, 8)

    game.set_board(2, 2, 1)
    game.set_board(2, 3, 5)
    game.set_board(2, 4, 7)
    game.set_board(2, 6, 3)
    game.set_board(2, 9, 9)

    game.set_board(3, 1, 7)
    game.set_board(3, 2, 3)
    game.set_board(3, 3, 4)
    game.set_board(3, 6, 8)
    game.set_board(3, 8, 6)

    game.set_board(4, 1, 5)
    game.set_board(4, 3, 3)
    game.set_board(4, 4, 2)
    game.set_board(4, 6, 4)

    game.set_board(5, 3, 8)
    game.set_board(5, 5, 9)
    game.set_board(5, 9, 5)

    game.set_board(6, 3, 6)
    game.set_board(6, 5, 5)
    game.set_board(6, 6, 7)
    game.set_board(6, 8, 3)

    game.set_board(7, 2, 5)
    game.set_board(7, 5, 7)
    game.set_board(7, 7, 4)
    game.set_board(7, 9, 9)

    game.set_board(8, 1, 4)
    game.set_board(8, 3, 9)
    game.set_board(8, 7, 2)
    game.set_board(8, 8, 5)

    game.set_board(9, 2, 8)
    game.set_board(9, 3, 7)
    game.set_board(9, 7, 6)
    game.set_board(9, 9, 3)

    return game


def example3():
    game = Sudoku_Board()

    game.set_board(1, 2, 8)
    game.set_board(1, 3, 5)
    game.set_board(1, 5, 9)
    game.set_board(1, 6, 2)
    game.set_board(1, 7, 7)

    game.set_board(2, 5, 8)

    game.set_board(3, 1, 3)
    game.set_board(3, 6, 6)
    game.set_board(3, 8, 2)

    game.set_board(4, 1, 4)
    game.set_board(4, 2, 9)
    game.set_board(4, 4, 8)
    game.set_board(4, 8, 5)

    game.set_board(5, 1, 2)
    game.set_board(5, 2, 1)
    game.set_board(5, 4, 7)
    game.set_board(5, 8, 9)
    game.set_board(5, 9, 6)

    game.set_board(6, 4, 1)
    game.set_board(6, 5, 6)

    game.set_board(7, 1, 6)
    game.set_board(7, 2, 4)
    game.set_board(7, 3, 9)
    game.set_board(7, 8, 3)

    game.set_board(8, 2, 3)
    game.set_board(8, 3, 1)
    game.set_board(8, 7, 6)

    game.set_board(9, 1, 8)
    game.set_board(9, 3, 7)
    game.set_board(9, 6, 1)

    return game


def example4():
    game = Sudoku_Board()

    game.set_board(1, 1, 5)
    game.set_board(1, 9, 9)

    game.set_board(2, 3, 9)
    game.set_board(2, 4, 3)

    game.set_board(3, 2, 2)
    game.set_board(3, 3, 7)
    game.set_board(3, 7, 1)

    game.set_board(4, 1, 4)
    game.set_board(4, 4, 5)
    game.set_board(4, 7, 3)
    game.set_board(4, 9, 8)

    game.set_board(5, 2, 1)
    game.set_board(5, 6, 6)
    game.set_board(5, 8, 5)
    game.set_board(5, 9, 7)

    game.set_board(6, 3, 3)
    game.set_board(6, 7, 9)

    game.set_board(7, 1, 9)
    game.set_board(7, 5, 4)
    game.set_board(7, 6, 5)
    game.set_board(7, 9, 3)

    game.set_board(8, 1, 1)
    game.set_board(8, 5, 7)

    game.set_board(9, 7, 6)
    game.set_board(9, 9, 5)

    return game


def example5():
    # Expert Puzzle, Takes the longest to solve
    game = Sudoku_Board()

    game.set_board(1, 1, 5)
    game.set_board(1, 2, 7)
    game.set_board(1, 3, 1)
    game.set_board(1, 4, 4)
    game.set_board(1, 8, 3)

    game.set_board(2, 1, 8)
    game.set_board(2, 3, 2)
    game.set_board(2, 4, 7)
    game.set_board(2, 6, 3)
    game.set_board(2, 7, 1)
    game.set_board(2, 8, 9)

    game.set_board(3, 1, 9)
    game.set_board(3, 2, 6)
    game.set_board(3, 6, 8)

    game.set_board(4, 2, 2)
    game.set_board(4, 5, 3)
    game.set_board(4, 6, 1)

    game.set_board(5, 4, 6)
    game.set_board(5, 5, 4)
    game.set_board(5, 9, 7)

    game.set_board(6, 3, 5)
    game.set_board(6, 5, 2)

    game.set_board(7, 6, 2)
    game.set_board(7, 8, 7)

    game.set_board(8, 1, 6)
    game.set_board(8, 3, 7)
    game.set_board(8, 6, 5)
    game.set_board(8, 9, 9)

    game.set_board(9, 3, 9)
    game.set_board(9, 9, 1)

    return game


def blank():
    game = Sudoku_Board()
    return game
