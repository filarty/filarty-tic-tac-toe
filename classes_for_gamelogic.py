import tkinter as tk

figure = "X" # Переменная для переключение фигуры


class Game:
    winning = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (1, 4, 7), (0, 3, 6), (2, 5, 8), (0, 4, 8), (2, 4, 6)] #выигрышные варианты
    move = 0 # счет хода
    array = ["0", "1", "2",    #список для размещения фигур
             "3", "4", "5",
             "6", "7", "8"]
    finish_combinations = None  # выиграшная комбинация

    @classmethod
    def check_combo(cls):   # данный метод служит для проверки выигрыша и заносит выигрышную комбинацию
        cls.move += 1
        if cls.move > 8:
            print("Ничья!")
        for a, b, c in Game.winning:
            if cls.array[a] == cls.array[b] and cls.array[b] == cls.array[c] and (
                    cls.array[a] == "X" or cls.array[a] == "O"):
                if cls.array[a] == "X":
                    print("X WIN!")
                    Game.finish_combinations = (a, b, c)
                elif cls.array[a] == "O":
                    print("O WIN!")
                    Game.finish_combinations = (a, b, c)
        print(Game.finish_combinations)


class Button(tk.Button):
    __id = 0                    # id для отслеживания номера кнопки
                                # класс создания tk кнопки
    def __init__(self, root):
        super().__init__()
        self.root = root         # поверхность для отрисовки кнопки
        self.button_id = Button.__id
        self.button = tk.Button(command=self.add_figure)   # создать экземпляр класса на основе кнопки TK
        Button.__id += 1

    def place(self, row, column):                 # расположить кнопку(колонка, строка)
        self.button.grid(row=row, column=column, stick="wens")

    def add_figure(self):   # добавить фигуру при нажатии кнопки мыши
        global figure
        if not self.button["text"]:             # если в ячейке где щелкает курсор нет фигуры, тогда разместить
            self.button["text"] = figure
            Game.array[self.button_id] = figure # присвоить игровому списку фигуру по идендификатору
            Game.check_combo()   # проверить выигрыш
            figure = "O" if figure == "X" else "X"  # поменять фигуру если ход был свершен
        else:
            print("Занято!")
            return 0

    def color(self):
        self.button["bg"] = "red"  # перекраска кнопки в красный
