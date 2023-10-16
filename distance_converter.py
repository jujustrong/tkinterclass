import tkinter as tk
import tkinter.font as font
from tkinter import ttk


def distance_converter():
    
    #create your container
    root = tk.Tk()
    root.title('Distance Converter')
    root.geometry("400x300")
    root.resizable(False, False)
    
    font.nametofont("TkDefaultFont").configure(size=13)
    
    distances = (
        'Foot', 'Kilometer', 'Centimeter', 'Meter', 'Millimeter', 'Mile', 
        'Yard', 'Inch', 'Micrometer', 'Nanometer'
        )
    
    answer = tk.StringVar()
    
    def calculate_distance(*args):
        try:
            if spin_box1.get() == "Meter" and spin_box2.get() == "Foot":
                set_num = float(convert_from.get())
                converted = set_num*3.28084
                answer.set(f"{converted:.3f}ft")
            elif spin_box1.get() == "Meter" and spin_box2.get() == "Kilometer":
                set_num = float(convert_from.get())
                converted = set_num/1000
                answer.set(f"{converted:.3f}km")
            elif spin_box1.get() == "Meter" and spin_box2.get() == "Centimeter":
                set_num = float(convert_from.get())
                converted = set_num*100
                answer.set(f"{converted:.3f}cm")
            elif spin_box1.get() == "Meter" and spin_box2.get() == "Meter":
                set_num = float(convert_from.get())
                converted = set_num*1
                answer.set(f"{converted:.3f}m")
            elif spin_box1.get() == "Meter" and spin_box2.get() == "Millimeter":
                set_num = float(convert_from.get())
                converted = set_num*1000
                answer.set(f"{converted:.3f}mm")
            elif spin_box1.get() == "Meter" and spin_box2.get() == "Mile":
                set_num = float(convert_from.get())
                converted = set_num/1609
                answer.set(f"{converted:.3f}mi")
            elif spin_box1.get() == "Meter" and spin_box2.get() == "Yard":
                set_num = float(convert_from.get())
                converted = set_num*1.094
                answer.set(f"{converted:.3f}yds")
            elif spin_box1.get() == "Meter" and spin_box2.get() == "Inch":
                set_num = float(convert_from.get())
                converted = set_num*39.37
                answer.set(f"{converted:.3f}in")
            elif spin_box1.get() == "Meter" and spin_box2.get() == "Micrometer":
                set_num = float(convert_from.get())
                converted = set_num*1e+6
                answer.set(f"{converted:.3f}μm")
            elif spin_box1.get() == "Meter" and spin_box2.get() == "Nanometer":
                set_num = float(convert_from.get())
                converted = set_num*1e+9
                answer.set(f"{converted:.3f}nm")
            elif spin_box1.get() == "Foot" and spin_box2.get() == "Foot":
                set_num = float(convert_from.get())
                converted = set_num*1
                answer.set(f"{converted:.3f}ft")
            elif spin_box1.get() == "Foot" and spin_box2.get() == "Kilometer":
                set_num = float(convert_from.get())
                converted = set_num/3281
                answer.set(f"{converted:.3f}km")
            elif spin_box1.get() == "Foot" and spin_box2.get() == "Centimeter":
                set_num = float(convert_from.get())
                converted = set_num*30.48
                answer.set(f"{converted:.3f}cm")
            elif spin_box1.get() == "Foot" and spin_box2.get() == "Meter":
                set_num = float(convert_from.get())
                converted = set_num/3.281
                answer.set(f"{converted:.3f}m")
            elif spin_box1.get() == "Foot" and spin_box2.get() == "Millimeter":
                set_num = float(convert_from.get())
                converted = set_num*304.8
                answer.set(f"{converted:.3f}mm")
            elif spin_box1.get() == "Foot" and spin_box2.get() == "Mile":
                set_num = float(convert_from.get())
                converted = set_num/5280
                answer.set(f"{converted:.3f}mi")
            elif spin_box1.get() == "Foot" and spin_box2.get() == "Yard":
                set_num = float(convert_from.get())
                converted = set_num/3
                answer.set(f"{converted:.3f}yds")
            elif spin_box1.get() == "Foot" and spin_box2.get() == "Inch":
                set_num = float(convert_from.get())
                converted = set_num*12
                answer.set(f"{converted:.3f}in")
            elif spin_box1.get() == "Foot" and spin_box2.get() == "Micrometer":
                set_num = float(convert_from.get())
                converted = set_num*304800
                answer.set(f"{converted:.3f}μm")
            elif spin_box1.get() == "Foot" and spin_box2.get() == "Nanometer":
                set_num = float(convert_from.get())
                converted = set_num*3.048e+8
                answer.set(f"{converted:.3f}nm")
            elif spin_box1.get() == "Kilometer" and spin_box2.get() == "Foot":
                set_num = float(convert_from.get())
                converted = set_num*3281
                answer.set(f"{converted:.3f}ft")
            elif spin_box1.get() == "Kilometer" and spin_box2.get() == "Kilometer":
                set_num = float(convert_from.get())
                converted = set_num*1
                answer.set(f"{converted:.3f}km")
            elif spin_box1.get() == "Kilometer" and spin_box2.get() == "Centimeter":
                set_num = float(convert_from.get())
                converted = set_num*100000
                answer.set(f"{converted:.3f}cm")
            elif spin_box1.get() == "Kilometer" and spin_box2.get() == "Meter":
                set_num = float(convert_from.get())
                converted = set_num*1000
                answer.set(f"{converted:.3f}m")
            elif spin_box1.get() == "Kilometer" and spin_box2.get() == "Millimeter":
                set_num = float(convert_from.get())
                converted = set_num*1e+6
                answer.set(f"{converted:.3f}mm")
            elif spin_box1.get() == "Kilometer" and spin_box2.get() == "Mile":
                set_num = float(convert_from.get())
                converted = set_num/1.609
                answer.set(f"{converted:.3f}mi")
            elif spin_box1.get() == "Kilometer" and spin_box2.get() == "Yard":
                set_num = float(convert_from.get())
                converted = set_num*1094
                answer.set(f"{converted:.3f}yds")
            elif spin_box1.get() == "Kilometer" and spin_box2.get() == "Inch":
                set_num = float(convert_from.get())
                converted = set_num*39370
                answer.set(f"{converted:.3f}in")
            elif spin_box1.get() == "Kilometer" and spin_box2.get() == "Micrometer":
                set_num = float(convert_from.get())
                converted = set_num*1e+9
                answer.set(f"{converted:.3f}μm")
            elif spin_box1.get() == "Kilometer" and spin_box2.get() == "Nanometer":
                set_num = float(convert_from.get())
                converted = set_num*1e+12
                answer.set(f"{converted:.3f}nm")
            elif spin_box1.get() == "Centimeter" and spin_box2.get() == "Foot":
                set_num = float(convert_from.get())
                converted = set_num*3281
                answer.set(f"{converted:.3f}ft")
            elif spin_box1.get() == "Centimeter" and spin_box2.get() == "Kilometer":
                set_num = float(convert_from.get())
                converted = set_num/30.48
                answer.set(f"{converted:.3f}km")
            elif spin_box1.get() == "Centimeter" and spin_box2.get() == "Centimeter":
                set_num = float(convert_from.get())
                converted = set_num*1
                answer.set(f"{converted:.3f}cm")
            elif spin_box1.get() == "Centimeter" and spin_box2.get() == "Meter":
                set_num = float(convert_from.get())
                converted = set_num/100
                answer.set(f"{converted:.3f}m")
            elif spin_box1.get() == "Centimeter" and spin_box2.get() == "Millimeter":
                set_num = float(convert_from.get())
                converted = set_num*10
                answer.set(f"{converted:.3f}mm")
            elif spin_box1.get() == "Centimeter" and spin_box2.get() == "Mile":
                set_num = float(convert_from.get())
                converted = set_num/160900
                answer.set(f"{converted:.3f}mi")
            elif spin_box1.get() == "Centimeter" and spin_box2.get() == "Yard":
                set_num = float(convert_from.get())
                converted = set_num/91.44
                answer.set(f"{converted:.3f}yds")
            elif spin_box1.get() == "Centimeter" and spin_box2.get() == "Inch":
                set_num = float(convert_from.get())
                converted = set_num/2.54
                answer.set(f"{converted:.3f}in")
            elif spin_box1.get() == "Centimeter" and spin_box2.get() == "Micrometer":
                set_num = float(convert_from.get())
                converted = set_num*10000
                answer.set(f"{converted:.3f}μm")
            elif spin_box1.get() == "Centimeter" and spin_box2.get() == "Nanometer":
                set_num = float(convert_from.get())
                converted = set_num*1e+7
                answer.set(f"{converted:.3f}nm")
            elif spin_box1.get() == "Millimeter" and spin_box2.get() == "Foot":
                set_num = float(convert_from.get())
                converted = set_num/304.8
                answer.set(f"{converted:.3f}ft")
            elif spin_box1.get() == "Millimeter" and spin_box2.get() == "Kilometer":
                set_num = float(convert_from.get())
                converted = set_num/1e+6
                answer.set(f"{converted:.3f}km")
            elif spin_box1.get() == "Millimeter" and spin_box2.get() == "Centimeter":
                set_num = float(convert_from.get())
                converted = set_num/10
                answer.set(f"{converted:.3f}cm")
            elif spin_box1.get() == "Millimeter" and spin_box2.get() == "Meter":
                set_num = float(convert_from.get())
                converted = set_num/1000
                answer.set(f"{converted:.3f}m")
            elif spin_box1.get() == "Millimeter" and spin_box2.get() == "Millimeter":
                set_num = float(convert_from.get())
                converted = set_num*1
                answer.set(f"{converted:.3f}mm")
            elif spin_box1.get() == "Millimeter" and spin_box2.get() == "Mile":
                set_num = float(convert_from.get())
                converted = set_num/1.609e+6
                answer.set(f"{converted:.3f}mi")
            elif spin_box1.get() == "Millimeter" and spin_box2.get() == "Yard":
                set_num = float(convert_from.get())
                converted = set_num/914.4
                answer.set(f"{converted:.3f}yds")
            elif spin_box1.get() == "Millimeter" and spin_box2.get() == "Inch":
                set_num = float(convert_from.get())
                converted = set_num/25.4
                answer.set(f"{converted:.3f}in")
            elif spin_box1.get() == "Millimeter" and spin_box2.get() == "Micrometer":
                set_num = float(convert_from.get())
                converted = set_num*1000
                answer.set(f"{converted:.3f}μm")
            elif spin_box1.get() == "Millimeter" and spin_box2.get() == "Nanometer":
                set_num = float(convert_from.get())
                converted = set_num*1e+6
                answer.set(f"{converted:.3f}nm")
            elif spin_box1.get() == "Mile" and spin_box2.get() == "Foot":
                set_num = float(convert_from.get())
                converted = set_num*5280
                answer.set(f"{converted:.3f}ft")
            elif spin_box1.get() == "Mile" and spin_box2.get() == "Kilometer":
                set_num = float(convert_from.get())
                converted = set_num*1.609
                answer.set(f"{converted:.3f}km")
            elif spin_box1.get() == "Mile" and spin_box2.get() == "Centimeter":
                set_num = float(convert_from.get())
                converted = set_num*160900
                answer.set(f"{converted:.3f}cm")
            elif spin_box1.get() == "Mile" and spin_box2.get() == "Meter":
                set_num = float(convert_from.get())
                converted = set_num*1609
                answer.set(f"{converted:.3f}m")
            elif spin_box1.get() == "Mile" and spin_box2.get() == "Millimeter":
                set_num = float(convert_from.get())
                converted = set_num*1.609e+6
                answer.set(f"{converted:.3f}mm")
            elif spin_box1.get() == "Mile" and spin_box2.get() == "Mile":
                set_num = float(convert_from.get())
                converted = set_num*1
                answer.set(f"{converted:.3f}mi")
            elif spin_box1.get() == "Mile" and spin_box2.get() == "Yard":
                set_num = float(convert_from.get())
                converted = set_num*1760
                answer.set(f"{converted:.3f}yds")
            elif spin_box1.get() == "Mile" and spin_box2.get() == "Inch":
                set_num = float(convert_from.get())
                converted = set_num*63360
                answer.set(f"{converted:.3f}in")
            elif spin_box1.get() == "Mile" and spin_box2.get() == "Micrometer":
                set_num = float(convert_from.get())
                converted = set_num*1.609e+9
                answer.set(f"{converted:.3f}μm")
            elif spin_box1.get() == "Mile" and spin_box2.get() == "Nanometer":
                set_num = float(convert_from.get())
                converted = set_num*1.609e+12
                answer.set(f"{converted:.3f}nm")
            elif spin_box1.get() == "Yard" and spin_box2.get() == "Foot":
                set_num = float(convert_from.get())
                converted = set_num*3
                answer.set(f"{converted:.3f}ft")
            elif spin_box1.get() == "Yard" and spin_box2.get() == "Kilometer":
                set_num = float(convert_from.get())
                converted = set_num/1094
                answer.set(f"{converted:.3f}km")
            elif spin_box1.get() == "Yard" and spin_box2.get() == "Centimeter":
                set_num = float(convert_from.get())
                converted = set_num*91.44
                answer.set(f"{converted:.3f}cm")
            elif spin_box1.get() == "Yard" and spin_box2.get() == "Meter":
                set_num = float(convert_from.get())
                converted = set_num/1.094
                answer.set(f"{converted:.3f}m")
            elif spin_box1.get() == "Yard" and spin_box2.get() == "Millimeter":
                set_num = float(convert_from.get())
                converted = set_num*914.4
                answer.set(f"{converted:.3f}mm")
            elif spin_box1.get() == "Yard" and spin_box2.get() == "Mile":
                set_num = float(convert_from.get())
                converted = set_num*1
                answer.set(f"{converted:.3f}mi")
            elif spin_box1.get() == "Yard" and spin_box2.get() == "Yard":
                set_num = float(convert_from.get())
                converted = set_num*1
                answer.set(f"{converted:.3f}yds")
            elif spin_box1.get() == "Yard" and spin_box2.get() == "Inch":
                set_num = float(convert_from.get())
                converted = set_num*63360
                answer.set(f"{converted:.3f}in")
            elif spin_box1.get() == "Yard" and spin_box2.get() == "Micrometer":
                set_num = float(convert_from.get())
                converted = set_num*1.609e+9
                answer.set(f"{converted:.3f}μm")
            elif spin_box1.get() == "Yard" and spin_box2.get() == "Nanometer":
                set_num = float(convert_from.get())
                converted = set_num*1.609e+12
                answer.set(f"{converted:.3f}nm")
            elif spin_box1.get() == "Inch" and spin_box2.get() == "Foot":
                set_num = float(convert_from.get())
                converted = set_num/12
                answer.set(f"{converted:.3f}ft")
            elif spin_box1.get() == "Inch" and spin_box2.get() == "Kilometer":
                set_num = float(convert_from.get())
                converted = set_num/39370
                answer.set(f"{converted:.3f}km")
            elif spin_box1.get() == "Inch" and spin_box2.get() == "Centimeter":
                set_num = float(convert_from.get())
                converted = set_num*2.54
                answer.set(f"{converted:.3f}cm")
            elif spin_box1.get() == "Inch" and spin_box2.get() == "Meter":
                set_num = float(convert_from.get())
                converted = set_num/39.37
                answer.set(f"{converted:.3f}m")
            elif spin_box1.get() == "Inch" and spin_box2.get() == "Millimeter":
                set_num = float(convert_from.get())
                converted = set_num*25.4
                answer.set(f"{converted:.3f}mm")
            elif spin_box1.get() == "Inch" and spin_box2.get() == "Mile":
                set_num = float(convert_from.get())
                converted = set_num/63360
                answer.set(f"{converted:.3f}mi")
            elif spin_box1.get() == "Inch" and spin_box2.get() == "Yard":
                set_num = float(convert_from.get())
                converted = set_num/36
                answer.set(f"{converted:.3f}yds")
            elif spin_box1.get() == "Inch" and spin_box2.get() == "Inch":
                set_num = float(convert_from.get())
                converted = set_num*1
                answer.set(f"{converted:.3f}in")
            elif spin_box1.get() == "Inch" and spin_box2.get() == "Micrometer":
                set_num = float(convert_from.get())
                converted = set_num*25400
                answer.set(f"{converted:.3f}μm")
            elif spin_box1.get() == "Inch" and spin_box2.get() == "Nanometer":
                set_num = float(convert_from.get())
                converted = set_num*2.54e+7
                answer.set(f"{converted:.3f}nm")
            elif spin_box1.get() == "Micrometer" and spin_box2.get() == "Foot":
                set_num = float(convert_from.get())
                converted = set_num/304800
                answer.set(f"{converted:.3f}ft")
            elif spin_box1.get() == "Micrometer" and spin_box2.get() == "Kilometer":
                set_num = float(convert_from.get())
                converted = set_num/1e+9
                answer.set(f"{converted:.3f}km")
            elif spin_box1.get() == "Micrometer" and spin_box2.get() == "Centimeter":
                set_num = float(convert_from.get())
                converted = set_num/10000
                answer.set(f"{converted:.3f}cm")
            elif spin_box1.get() == "Micrometer" and spin_box2.get() == "Meter":
                set_num = float(convert_from.get())
                converted = set_num/1e+6
                answer.set(f"{converted:.3f}m")
            elif spin_box1.get() == "Micrometer" and spin_box2.get() == "Millimeter":
                set_num = float(convert_from.get())
                converted = set_num/1000
                answer.set(f"{converted:.3f}mm")
            elif spin_box1.get() == "Micrometer" and spin_box2.get() == "Mile":
                set_num = float(convert_from.get())
                converted = set_num/1.609e+9
                answer.set(f"{converted:.3f}mi")
            elif spin_box1.get() == "Micrometer" and spin_box2.get() == "Yard":
                set_num = float(convert_from.get())
                converted = set_num/914400
                answer.set(f"{converted:.3f}yds")
            elif spin_box1.get() == "Micrometer" and spin_box2.get() == "Inch":
                set_num = float(convert_from.get())
                converted = set_num/25400
                answer.set(f"{converted:.3f}in")
            elif spin_box1.get() == "Micrometer" and spin_box2.get() == "Micrometer":
                set_num = float(convert_from.get())
                converted = set_num*1
                answer.set(f"{converted:.3f}μm")
            elif spin_box1.get() == "Micrometer" and spin_box2.get() == "Nanometer":
                set_num = float(convert_from.get())
                converted = set_num*1000
                answer.set(f"{converted:.3f}nm")
            elif spin_box1.get() == "Nanometer" and spin_box2.get() == "Foot":
                set_num = float(convert_from.get())
                converted = set_num/3.048e+8
                answer.set(f"{converted:.3f}ft")
            elif spin_box1.get() == "Nanometer" and spin_box2.get() == "Kilometer":
                set_num = float(convert_from.get())
                converted = set_num/1e+12
                answer.set(f"{converted:.3f}km")
            elif spin_box1.get() == "Nanometer" and spin_box2.get() == "Centimeter":
                set_num = float(convert_from.get())
                converted = set_num/1e+7
                answer.set(f"{converted:.3f}cm")
            elif spin_box1.get() == "Nanometer" and spin_box2.get() == "Meter":
                set_num = float(convert_from.get())
                converted = set_num/1e+9
                answer.set(f"{converted:.3f}m")
            elif spin_box1.get() == "Nanometer" and spin_box2.get() == "Millimeter":
                set_num = float(convert_from.get())
                converted = set_num/1e+6
                answer.set(f"{converted:.3f}mm")
            elif spin_box1.get() == "Nanometer" and spin_box2.get() == "Mile":
                set_num = float(convert_from.get())
                converted = set_num/1.609e+12
                answer.set(f"{converted:.3f}mi")
            elif spin_box1.get() == "Nanometer" and spin_box2.get() == "Yard":
                set_num = float(convert_from.get())
                converted = set_num/9.144e+8
                answer.set(f"{converted:.3f}yds")
            elif spin_box1.get() == "Nanometer" and spin_box2.get() == "Inch":
                set_num = float(convert_from.get())
                converted = set_num/2.54e+7
                answer.set(f"{converted:.3f}in")
            elif spin_box1.get() == "Nanometer" and spin_box2.get() == "Micrometer":
                set_num = float(convert_from.get())
                converted = set_num/1000
                answer.set(f"{converted:.3f}μm")
            elif spin_box1.get() == "Nanometer" and spin_box2.get() == "Nanometer":
                set_num = float(convert_from.get())
                converted = set_num*1
                answer.set(f"{converted:.3f}nm")
        except ValueError:
            pass
    
    
    root.columnconfigure(0, weight=2)
    
    #create the main frame
    main = ttk.Frame(root, padding=(30, 15))
    main.grid()
    
    initial_value1 = tk.StringVar(value="Choose Distance...")
    spin_box1 = ttk.Spinbox(main, values=distances, textvariable=initial_value1, wrap=True, width=13)
    spin_box1['state'] = 'readonly'
    
    initial_value2 = tk.StringVar(value="Convert To...")
    spin_box2 = ttk.Spinbox(main, values=distances, textvariable=initial_value2, wrap=True, width=13)
    spin_box2['state'] = 'readonly'
    
    #create your elements: labels, input areas, and buttons for the window
    convert_from = ttk.Entry(main, width=10, textvariable=spin_box1.get(), font=("Helvetica", 13))                         #textvariable corresponds with the string variable we created so we can use it in our function.
    convert_to = ttk.Label(main, textvariable=answer, width=12)
    calc_button = ttk.Button(main, text="Calculate", command=calculate_distance)
    done_button = ttk.Button(main, text="Quit", command=root.destroy)
    
    #put all of your elements into the mainframe using 'grid'
    spin_box1.grid(column=0, row=0, sticky="w")                                                     #this row/column setting is the default but it is here for reference.
    convert_from.grid(column=1, row=0, sticky="ew", columnspan=1)
    convert_from.focus()                                                                          #allows the user to type directly into the input area.
    
    spin_box2.grid(column=0, row=1, sticky="w")
    convert_to.grid(column=1, row=1, sticky="e", columnspan=1, rowspan=1)
    
    calc_button.grid(column=0, row=2, sticky="ew", columnspan=3)
    done_button.grid(column=0, row=3, sticky="ew", columnspan=3)
    
    for child in main.winfo_children():
        child.grid_configure(padx=15, pady=15)
    
    root.bind("<Return>", calculate_distance)
    
    
    return root.mainloop()


distance_converter()
