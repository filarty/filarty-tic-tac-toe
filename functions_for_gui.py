
import classes_for_gamelogic


def initialization(root):
    root.title("Крестики-нолики")
    root.geometry("500x500")
    root.resizable(width=False, height=False)


def created_buttons(root):
    b1 = classes_for_gamelogic.Button(root)
    b2 = classes_for_gamelogic.Button(root)
    b3 = classes_for_gamelogic.Button(root)
    b4 = classes_for_gamelogic.Button(root)
    b5 = classes_for_gamelogic.Button(root)
    b6 = classes_for_gamelogic.Button(root)
    b7 = classes_for_gamelogic.Button(root)
    b8 = classes_for_gamelogic.Button(root)
    b9 = classes_for_gamelogic.Button(root)
    return [b1, b2, b3, b4, b5, b6, b7, b8, b9]


def config_grid_buttons(array):
    row = 0
    column = 0
    for i in array:
        i.place(row=row, column=column)
        column += 1
        if column == 3:
            column = 0
            row += 1


def grid_column_config(root):
    root.grid_columnconfigure(0, minsize=166)
    root.grid_columnconfigure(1, minsize=166)
    root.grid_columnconfigure(2, minsize=166)
    root.grid_rowconfigure(0, minsize=170)
    root.rowconfigure(1, minsize=166)
    root.rowconfigure(2, minsize=166)
