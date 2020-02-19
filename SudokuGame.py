
class Sudoku_Board:

    """
    A Sudoku Board

    ===Attributes===
    board: the 9x9 board with values
    """
    # Attribute Types
    _board: [[str]] # [row][column]

    def __init__(self) -> None:
        # Initialize all blank spaces to "_"
        self._board = [[], [], [], [], [], [], [], [], []]
        for row in range(len(self._board)):
            self._board[row] = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

    def __str__(self) -> str:
        # Print the Board
        output = ""
        for row in range(len(self._board)):

            # Add Horizontal Bar
            if row == 3 or row == 6:
                for dummy in range(17):
                    output += "-"
                output += "\n"

            for col in range(len(self._board[row])):
                # Add Value
                output += str(self._board[row][col])
                if ((col + 1) % 3):
                    output += " "
                # Add Vertical Bar
                if col == 2 or col == 5:
                    output += "|"
            # Add New Line at end of Row
            output += "\n"
        return output

    def set_board(self, row: int, col: int, value: int) -> None:
        # Set's a value for the board
        self._board[row - 1][col - 1] = value # Care for indexing at 0

    def _check_valid(self, row: int, col: int) -> bool:
        # Returns true if a value on <row>, <col> does not violate the rules of Sudoku (row, col, squares)

        target = self._board[row - 1][col - 1]

        # Check Rows and Columns
        for i in range(9):
            # Iterate through a row, but skip the target square
            if (i != col-1) and (target == self._board[row-1][i]):
                return False

            # Iterate through a column, but skip the target square
            if (i != row-1) and (target == self._board[i][col-1]):
                return False

        # Check Squares-Sectors


        return True


def main():
    game = Sudoku_Board()
    game.set_board(4, 4, 8)
    print(game._check_valid(4,4))  # True
    game.set_board(5, 5, 8)
    print(game._check_valid(4, 4))  # True
    print(game._check_valid(5, 5))  # True
    game.set_board(4,5,8)
    print(game._check_valid(4, 4))  # False
    print(game._check_valid(5, 5))  # False
    print(game._check_valid(4, 5))  # False




if __name__ == "__main__":
    main()
