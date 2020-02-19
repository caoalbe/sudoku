
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
            if row == 0 or row == 3 or row == 6:
                for dummy in range(19):
                    output += "-"
                output += "\n"

            for col in range(len(self._board[row])):
                # Add Vertical Bar
                if col == 0 or col == 3 or col == 6:
                    output += "|"

                # Add Value
                output += str(self._board[row][col])
                if ((col + 1) % 3):
                    output += " "
            # Add New Line and Vertical Bar at end of Row
            output += "|\n"

        # Add Horizontal Bar at Bottom of Board
        for dummy in range(19):
            output += "-"
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
    print(str(game))




if __name__ == "__main__":
    main()
