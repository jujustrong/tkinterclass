import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


root = tk.Tk()
root.geometry("900x500")
root.resizable(False, False)
root.title("Widget Examples")

# label = ttk.Label(root, text="Welcome to Parkle", padding=20)
# label.config(font=("Helvetica", 30))
# label.pack()

image = Image.open("/Users/jarmstrong/Desktop/Python Stuff/VSPYTHON/tkinterclass/Daco_1637362.png").resize((64,64))
photo = ImageTk.PhotoImage(image)
natlabel = ttk.Label(root, text="Welcome to Parkle!", image=photo, padding=5, compound="top")
natlabel.pack()

root.mainloop()