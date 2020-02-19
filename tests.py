# Tests for Files

import unittest
import SudokuGame

if __name__ == '__main__':
    unittest


# ==================================================== Sudoku_Board ====================================================

class TestSudokuBoard(unittest.TestCase):

    def test_init(self) -> None:
        # Test for <__init__>
        game = SudokuGame.Sudoku_Board()
        assert game._board[0][0] == "_"  # e1
        assert game._board[8][8] == "_"  # e2
        assert game._board[2][2] == "_"  # e3
        assert game._board[3][3] == "_"  # e4

    def test_string(self) -> None:
        # Test for <__str__>
        game1 = SudokuGame.Sudoku_Board()

        game2 = SudokuGame.Sudoku_Board()
        game2._board[1][1] = 3
        assert str(game1) != str(game2)

        game2._board[1][1] = "_"
        assert str(game1) == str(game2)

    def test_get_board(self) -> None:
        # Test for <get_board>
        game = SudokuGame.Sudoku_Board()
        assert game.get_board(3, 3) == "_"

        game._board[2][2] = 7
        assert game.get_board(3, 3) == 7

    def test_set_board(self) -> None:
        # Test for <set_board>
        game = SudokuGame.Sudoku_Board()
        game.set_board(4, 6, 99)
        assert game._board[4 - 1][6 - 1] == 99

        game.set_board(4, 6, 8)
        assert game._board[4 - 1][6 - 1] == 8

    def test_check_valid(self) -> None:
        # Test for <_check_valid>
        game = SudokuGame.Sudoku_Board()
        # Should return false since there are multiple empty spaces
        assert not game._check_valid(3, 3)

        game.set_board(3, 3, 8)
        game.set_board(3, 4, 8)
        assert not game._check_valid(3, 3)
        assert not game._check_valid(3, 4)

        game.set_board(5, 5, 8)
        assert game._check_valid(5, 5)

        game.set_board(5, 6, 7)
        assert game._check_valid(5, 5)
        assert game._check_valid(5, 6)

        game.set_board(6, 7, 7)
        assert game._check_valid(5, 6)
        assert game._check_valid(6, 7)


# ================================================== Helper Functions ==================================================


class TestHelperFunctions(unittest.TestCase):

    def test_get_sector(self) -> None:
        # Test for <_get_sector>
        assert SudokuGame._get_sector(1, 1) == [0, 0]
        assert SudokuGame._get_sector(4, 4) == [1, 1]
        assert SudokuGame._get_sector(2, 5) == [0, 1]
        assert SudokuGame._get_sector(9, 9) == [2, 2]
