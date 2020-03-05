
class Sudoku_Board:
    """
    A Sudoku Board

    ===Attributes===
    board: the 9x9 board with values
    """
    # Attribute Types
    _board: [[int]]  # [row][column]

    def __init__(self) -> None:
        # Initialize all blank spaces to "_"
        self._board = [[], [], [], [], [], [], [], [], []]
        for row in range(9):
            for col in range(9):
                self._board[row].append(0)

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
                value = self._board[row][col]
                if value == 0:
                    output += "_"
                else:
                    output += str(value)
                if (col + 1) % 3:
                    output += " "
            # Add New Line and Vertical Bar at end of Row
            output += "|\n"

        # Add Horizontal Bar at Bottom of Board
        for dummy in range(19):
            output += "-"
        return output

    def get_board(self, row: int, col: int) -> int:
        # Returns the value for the board
        # Returns "_" for empty tiles
        # Use this function to get around indexing at 0
        return self._board[row - 1][col - 1]

    def set_board(self, row: int, col: int, value: int) -> None:
        # Set's a value for the board
        self._board[row - 1][col - 1] = value  # Care for indexing at 0

    def clear_slot(self, row: int, col: int) -> None:
        # Deletes a value for the board
        self._board[row - 1][col - 1] = 0

    def check_valid(self, row: int, col: int) -> bool:
        # Returns true if a value on <row>, <col> does not violate the rules of Sudoku (row, col, squares)

        target = self.get_board(row, col)

        # Check Rows and Columns
        for i in range(9):
            # Iterate through a row, but skip the target square
            if (i != col-1) and (target == self.get_board(row, i + 1)):
                return False

            # Iterate through a column, but skip the target square
            if (i != row-1) and (target == self.get_board(i + 1, col)):
                return False

        # Check Squares-Sectors
        sector = _get_sector(row, col)
        # Iterate through rows of sector
        for r in range(3):
            # Iterate through col of sector
            for c in range(3):
                if self.get_board(3 * sector[0] + r + 1, 3 * sector[1] + c + 1) == target and \
                        (row != 3 * sector[0] + r + 1) and (col != 3 * sector[1] + c + 1):
                    # Iterate through a box, but skip target square
                    return False

        return True

    def player_move(self, row: int, col: int, value: int) -> bool:
        # Returns true if a player move is immediately valid
        # Mutates board if it is valid, otherwise stays the same

        if not self.get_board(row, col) == 0:
            # Place already has a value
            return False

        self.set_board(row, col, value)
        if not self.check_valid(row, col):
            # This move breaks a rule of sudoku
            self.clear_slot(row, col)
            return False

        return True

    def check_board(self) -> bool:
        # Checks if a game has been solved

        # Iterate through every tile and checks if any violate sudoku rules
        for r in range(9):
            for c in range(9):
                if not self._board == 0 and not self.check_valid(r, c):
                    return False
        return True

    def solve_game(self) -> None:
        # Mutates the board a solved state

        pass


# Static Methods
def _get_sector(row: int, col: int) -> [[int], [int]]:
    # Returns which sector a value is in
    # First index is row, second index is col (0-2)

    output = list()

    output.append((row - 1) // 3)
    output.append((col - 1) // 3)

    return output


if __name__ == "__main__":
    main()
