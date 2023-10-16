import tkinter as tk
import tkinter.font as font
from tkinter import ttk

def gretting_window():

    def greet():
        if user_name.get() == 'Bob':
            print("We don't like you Bob...")
        else:
            print(f"Hello {user_name.get() or 'World'}!")
            
    # creating the main window
    root = tk.Tk()
    root.title("Greeter")

    user_name = tk.StringVar()

    input_frame = ttk.Frame(root, padding=(20,10,20,0))                     #padding goes clockwise starting with the left side. Left, top, right, bottom
    input_frame.pack(fill="both") 

    name_label = ttk.Label(input_frame, text="Name: ")
    name_label.pack(side="left", padx=(0, 10))
    name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
    name_entry.pack(side='left')
    name_entry.focus()

    buttons = ttk.Frame(root, padding=(20,10,20,0))
    buttons.pack(fill="both")
    
    greet_button = ttk.Button(buttons, text='Greet', command=greet)
    greet_button.pack(side='left', fill="x", expand=True)

    quit_button = ttk.Button(buttons, text='Quit', command=root.destroy)
    quit_button.pack(side='left', fill="x", expand=True)
    
    return root.mainloop()