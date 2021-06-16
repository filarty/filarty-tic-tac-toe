import tkinter as tk
from PIL import ImageTk
def func():
    but["text"] = "Нажато!"


window = tk.Tk()
window.geometry("518x502")
window.resizable(width=False, height=False)
window.title("Hello")
id_button = 0
for j in range(3):
    for i in range(3):
        but = tk.Button(text=id_button, width=18, height=9, name=str(id_button), command=func).grid(row=j, column=i)
        id_button += 1
window.mainloop()