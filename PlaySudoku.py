
import examples
from tkinter import *

if __name__ == '__main__':
    game = examples.create_example1()

    root = Tk()

    # label_1 = Label(root, text="TOP TEXT")
    # label_2 = Label(root, text="BOTTOM TEXT")

    # entry_1 = Entry(root)
    # entry_2 = Entry(root)

    # label_1.grid(row=0, sticky=E)
    # label_2.grid(row=1, sticky=E)

    # entry_1.grid(row=0, column=1)
    # entry_2.grid(row=1, column=1)

    # Create all Labels and Entries
    for r in range(9):
        for c in range(9):
            target = game.get_board(r+1, c+1)
            if target == 0:
                # Create an Entry
                Entry(root, width=3, justify=CENTER).grid(row=r, column=c)
            else:
                # Create a Label
                Label(root, text=target).grid(row=r, column=c)

    # Create Check Moves Button
    def testing():
        print("nice")

    check = Button(root, text="Check Answers", command=testing)
    check.grid(row=9, columnspan=7, sticky=W)

    root.mainloop()
