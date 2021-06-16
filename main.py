class Game:
    """ Класс игры в крестики нолики
        атрибуты класса это выигрышные комбинации из тюплов(кортежей и в конструкторе класса игровое поле)
    """
    winning = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (1, 4, 7), (0, 3, 6), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    def __init__(self):
        self.array = ["0", "1", "2",
                      "3", "4", "5",
                      "6", "7", "8"]

    def show_grid(self):  # Нарисовать сетку
        print(f"{' | '.join(self.array[0:3])}\n{' | '.join(self.array[3:6])} \n{' | '.join(self.array[6:9])}")

    def move(self, figure):  # сделать ход, принимает X или O
        choice = int(input("Какая позиция?(0-8): "))
        if self.array[choice] == "X" or self.array[choice] == "O":
            return 1
        self.array[choice] = figure

    def check_winning(self):  # проверка комбинации с выигрышным тюплом
        for a, b, c in Game.winning:  # распаковка значений и их сравнение с игровыми клетками
            if self.array[a] == self.array[b] and self.array[b] == self.array[c] and (self.array[c] == "X"
                                                                                      or self.array[c] == "O"):
                return 1


game = Game()
figure = "X"
move = 0
while move < 7:
    game.show_grid()
    if game.move(figure):  # если метод вернет 1 то это означает что клетка занята
        print("Клетка занята!")
        continue
    if game.check_winning():  # если возвращает 1 то выиграла та фигура которая ходила на данный момент
        game.show_grid()
        print("Выиграли!", figure)
        break
    move += 1
    figure = "O" if figure == "X" else "X"  # если был ход X заменить на O  и наоборот
if move == 7:  # если осталось 2 клетки то это ничья
    game.show_grid()
    print("Ничья!")
