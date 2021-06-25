import functions_for_gui  # импорт функций для отрисовки
import classes_for_gamelogic as gl  # импорт классов для игры
import tkinter as tk

root = tk.Tk()  # создание главной поверхности
array = None

gl.x = tk.PhotoImage(file="image\klipartz.com.png")
gl.o = tk.PhotoImage(file="image\circle.png")


# функция перекраски кнопок в соответствии выигрышной комбинации и закончить игру
def Win():
    if gl.Game.finish_combinations:
        if gl.Game.finish_combinations == "Ничья":
            if functions_for_gui.show_winning(root, "Ничья") == "OK":
                functions_for_gui.remake()
                create()
        else:
            for i in gl.Game.finish_combinations:
                array[i].color()
            if functions_for_gui.show_winning(root, gl.Game.array[gl.Game.finish_combinations[0]]) == "OK":
                functions_for_gui.remake()
                create()
    root.after(1, Win)


def create():
    global array
    array = functions_for_gui.created_buttons(root)  # функция создания экземпляров кнопки
    functions_for_gui.config_grid_buttons(array)  # настройки сетки для кнопки
    functions_for_gui.grid_column_config(root)  # настройка сетки для поверхности
    functions_for_gui.initialization(root)  # инициализация(разрешения экрана и тд)


create()
root.after(10, Win)  # вызвать функцию через 1мс

if __name__ == "__main__":
    root.mainloop()
