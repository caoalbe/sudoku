# Albert Cao

import SudokuGame
import examples
from tkinter import *

if __name__ == '__main__':
    game = examples.create_example1()
    # game = examples.create_example2()
    # game = examples.create_blank()

    game.draw(0)
