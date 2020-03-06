# Albert Cao

from tkinter import *


class Sudoku_Board:
    """
    A Sudoku Board

    ===Attributes===
    board: the 9x9 board with values
    window: the GUI
    """
    # Attribute Types
    _board: [[int]]  # [row][column]
    _window: Tk()

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

    def draw(self, time: int) -> None:
        # <time> refers to how many milliseconds the window persists
        # 0 time indicates a forever window
        # Creates a window to view the sudoku board
        root = Tk()
        root.title("Sudoku")
        root.geometry("300x300")

        self._window = root  # Care this is a bodge;
        # code should reference <_window> instead of <root>

        if not time == 0:
            # 0 time indicates forever
            root.after(time, lambda: root.destroy())

        # Create all Labels and Entries
        for r in range(9):
            for c in range(9):
                target = self.get_board(r+1, c+1)
                if target == 0:
                    # Create an Entry
                    Entry(root, width=3, justify=CENTER).grid(row=r, column=c)
                else:
                    # Create a Label
                    Label(root, text=target).grid(row=r, column=c)

        # Create Check Moves Button
        def check_board():
            game.check_board()

        check = Button(root, text="Check Answers", command=check_board)
        check.grid(row=9, columnspan=6, sticky=W)

        # Create Solve Board Button
        def solution():
            root.destroy()
            self.solve_game(False)
            self.draw(0)

        solve = Button(root, text="Solution", command=solution)
        solve.grid(row=9, column=6, columnspan=3, sticky=E)

        root.mainloop()

    def update(self, row: int, col: int) -> None:
        # This edits an existing window instead
        # of drawing everything from scratch

        # In particular, it updates a specified space

        # Assuming self._window already has a tk instance

        updated = self.get_board(row, col)

        for widget in self._window.grid_slaves():
            if int(widget.grid_info()["row"]) + 1 == row \
                    and int(widget.grid_info()["column"]) + 1 == col:
                # update <widget>
                # kill <widget>
                widget.grid_forget()
                # draw updated widget in place
                if updated == 0:
                    # Empty Space, Create an Entry
                    Entry(self._window, width=3, justify=CENTER)\
                        .grid(row=r, column=c)
                else:
                    # Create a Label
                    Label(self._window, text=target).grid(row=r, column=c)

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

    def first_empty(self):
        # Return empty space on the board prioritizing
        # Higher Row and then a more left Column
        for r in range(9):
            for c in range(9):
                if self._board[r][c] == 0:
                    # Found Empty Space
                    return r+1, c+1
        # No Empty Spaces
        return None

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
                if self._board[r][c] == 0 or \
                        not self.check_valid(r+1, c+1):
                    # There is an empty-tile, game is not solved
                    # or
                    # There is a tile which breaks a sudoku rule
                    return False
        return True

    def solve_game(self, display: bool) -> bool:
        # Mutates the board to a solved state
        # If <display> is true, show the steps
        # Otherwise, just show the final state

        # Base Case
        # Game is Complete
        if self.check_board():
            return True

        # Recursive Case
        # Find an Empty Space to Try Solving
        (r, c) = self.first_empty()

        # Try Every Value 1-9 inclusive
        for v in range(1, 10):
            # Choose <v>
            self.set_board(r, c, v)
            # self.draw(200)
            self.update(r, c)
            # Verify
            if self.check_valid(r, c):
                # This choice of <v> in <r>, <c> might work
                if self.solve_game(display):
                    return True
            # Un-Choose <v>
            self.clear_slot(r, c)

        # The choice that led to this branch was bad,
        return False


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
