import tkinter as tk


class Game:
    winning = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (1, 4, 7), (0, 3, 6), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    figure = "X"
    move = 0
    array = ["0", "1", "2",
             "3", "4", "5",
             "6", "7", "8"]

    @classmethod
    def check_combo(cls):
        cls.move += 1
        if cls.move > 8:
            print("Ничья!")
        for a, b, c in Game.winning:
            if cls.array[a] == cls.array[b] and cls.array[b] == cls.array[c] and (
                    cls.array[a] == "X" or cls.array[a] == "O"):
                if cls.array[a] == "X":
                    print("X WIN!")
                elif cls.array[a] == "O":
                    print("O WIN!")
        cls.figure = "O" if cls.figure == "X" else "X"


class Button(tk.Button):
    __id = 0

    def __init__(self, root):
        super().__init__()
        self.root = root
        self.button_id = Button.__id
        self.button = tk.Button(command=self.click)
        Button.__id += 1

    def place(self, row, column):
        self.button.grid(row=row, column=column, stick="wens")

    def click(self):
        self.button["text"] = Game().figure
        Game().array[self.button_id] = Game().figure
        Game.check_combo()
