import tkinter as tk

root = tk.Tk()
root.title("Крестики-нолики")
root.geometry("500x500")
root.resizable(width=False, height=False)

b1 = tk.Button(root, text="hello")
b2 = tk.Button(root, text="hello")
b3 = tk.Button(root, text="hello")
b4 = tk.Button(root, text="hello")
b5 = tk.Button(root, text="hello")
b6 = tk.Button(root, text="hello")
b7 = tk.Button(root, text="hello")
b8 = tk.Button(root, text="hello")
b9 = tk.Button(root, text="hello")


b1.grid(row=0, column=0, stick="wens")
b2.grid(row=0, column=1, stick="wens")
b3.grid(row=0, column=2, stick="wens")
b4.grid(row=1, column=0, stick="wens")
b5.grid(row=1, column=1, stick="wens")
b6.grid(row=1, column=2, stick="wens")
b7.grid(row=2, column=0, stick="wens")
b8.grid(row=2, column=1, stick="wens")
b9.grid(row=2, column=2, stick="wens")

root.grid_columnconfigure(0, minsize=166)
root.grid_columnconfigure(1, minsize=166)
root.grid_columnconfigure(2, minsize=166)
root.grid_rowconfigure(0, minsize=170)
root.rowconfigure(1, minsize=166)
root.rowconfigure(2, minsize=166)

tk.mainloop()
