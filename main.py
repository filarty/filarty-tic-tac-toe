import functions_for_gui  # импорт функций для отрисовки
import classes_for_gamelogic as gl  # импорт классов для игры
import tkinter as tk

root = tk.Tk()  # создание главной поверхности


# функция перекраски кнопок в соответствии выигрышной комбинации и закончить игру
def Win():
    if gl.Game.finish_combinations:
        if gl.Game.finish_combinations == "Ничья":
            functions_for_gui.show_winning(root, "Ничья")
        else:
            for i in gl.Game.finish_combinations:
                array[i].color()
            functions_for_gui.show_winning(root, gl.Game.array[gl.Game.finish_combinations[0]])
            return 0
    root.after(1, Win)


array = functions_for_gui.created_buttons(root)  # функция создания экземпляров кнопки
functions_for_gui.config_grid_buttons(array)  # настройки сетки для кнопки
functions_for_gui.grid_column_config(root)  # настройка сетки для поверхности
functions_for_gui.initialization(root)  # инициализация(разрешения экрана и тд)

root.after(1, Win)  # вызвать функцию через 1мс

if __name__ == "__main__":
    root.mainloop()
