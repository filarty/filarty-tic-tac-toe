import tkinter as tk
import classes

root = tk.Tk()
root.title("Крестики-нолики")
root.geometry("500x500")
root.resizable(width=False, height=False)


b1 = classes.Button(root)
b2 = classes.Button(root)
b3 = classes.Button(root)
b4 = classes.Button(root)
b5 = classes.Button(root)
b6 = classes.Button(root)
b7 = classes.Button(root)
b8 = classes.Button(root)
b9 = classes.Button(root)


b1.place(row=0, column=0)
b2.place(row=0, column=1)
b3.place(row=0, column=2)
b4.place(row=1, column=0)
b5.place(row=1, column=1)
b6.place(row=1, column=2)
b7.place(row=2, column=0)
b8.place(row=2, column=1)
b9.place(row=2, column=2)

root.grid_columnconfigure(0, minsize=166)
root.grid_columnconfigure(1, minsize=166)
root.grid_columnconfigure(2, minsize=166)
root.grid_rowconfigure(0, minsize=170)
root.rowconfigure(1, minsize=166)
root.rowconfigure(2, minsize=166)

if __name__ == "__main__":
    tk.mainloop()
