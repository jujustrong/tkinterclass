import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("600x400")
root.resizable(False,False)
root.title("Widget Examples")

text = tk.Text(root, height=8)
text.pack()



root.mainloop()