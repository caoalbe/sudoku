# Albert Cao

from tkinter import *
import copy
from Sudoku_Board import Sudoku_Board
import examples

typeface = ("Verdana", 16)  # Constant


def draw(gui: Tk):

    for r in range(9):
        for c in range(9):
            target = game.get_board(r + 1, c + 1)
            if target == 0:
                # Create an Input Space
                Entry(gui, width=2, justify="center", font=(typeface[0], typeface[1])).grid(row=r, column=c)
            else:
                # Create a Label
                Label(gui, width=2, height=1, text=target, font=(typeface[0], typeface[1])).grid(row=r, column=c)

    # Create Check Moves Button
    def check_board():
        # Temp is board with all of the player selections
        temp = Sudoku_Board()
        for r in range(9):
            for c in range(9):
                target = find_widget(r, c)
                if isinstance(target, Entry):
                    # Target is <Entry>
                    input = target.get()
                    if input == "":
                        # Input is a blank space
                        input = 0
                    else:
                        input = int(input)
                    temp.set_board(r+1, c+1, input)
                else:
                    # Target is <Label>
                    temp.set_board(r+1, c+1, int(target.cget("text")))

        output_window = Tk()
        output_window.title("Result")

        if temp == solved:
            # Game has been solved by player.  Make these create a new window
            message_text = "Good Job!\nThis is Solved!"
        else:
            message_text = "Not Quite Right.\nKeep working on this Puzzle!"
        Label(output_window, text=message_text, font=(typeface[0], typeface[1])).pack()
        output_window.mainloop()

    check = Button(gui, text="Check Answers", command=check_board)
    check.grid(row=9, columnspan=3, sticky=W)

    # Scrapped this Function
    # # Create Show Steps Button
    # show_steps = IntVar()  # 0 indicates False; 1 indicates True
    # steps = Checkbutton(gui, text="Show Steps", variable=show_steps)
    # steps.grid(row=9, column=4, columnspan=3, sticky=E)

    # Create Solve Board Button
    def solution():
        # Clear Previous Screen
        for widget in gui.grid_slaves():
            widget.grid_forget()
        game.solve_game(True)
        # if not game.solve_game(show_steps == 1):
            # Game is Unsolvable
            # print("No Solution Exists")
        # nonlocal game = solved:
        draw(gui)

    solve = Button(gui, text="Solution", command=solution)
    solve.grid(row=9, column=6, columnspan=3, sticky=E)

    # Create Window
    gui.mainloop()


def find_widget(x: int, y: int):  # Literally dont know what instance to return but I know its not None
    # for widget in gui.grid_slaves():
    #     if int(widget.grid_info()["row"]) == x and int(widget.grid_info()["col"]) == y:
    #         return widget
    return gui.grid_slaves(row=x, column=y)[0]

if __name__ == '__main__':
    game = examples.random_example()

    solved = copy.deepcopy(game)
    solved.solve_game(False)

    gui = Tk()
    gui.title("Sudoku")
    draw(gui)

    # p1 = Process(target=draw(gui))
    # p1.start()
    # p2 = Process(target=solved.solve_game(False))
    # p2.start()
    # p2.join()
    # p1.join()
