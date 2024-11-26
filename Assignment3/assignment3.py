# https://docs.python.org/3/library/tkinter.html
# https://www.pythontutorial.net/tkinter/
import tkinter as tk
from tkinter import ttk
import util

window = tk.Tk()
window.title("Pizza Cutter")

label = ttk.Label(window, text="Diameter: ")

diameter = tk.DoubleVar()
diameter_entry = ttk.Entry(window, textvariable=diameter)

control_frame = tk.Frame(window, background="bisque")

def calculate(event=None):
    """calculate pizza slices"""
    try:
        slices = util.get_slices(diameter.get())
        result.set(f"{slices}")
    except Exception as exp:
        result.set(exp)

btn_calculate = ttk.Button(
   control_frame,
   text="Calculate",
   command=calculate
)

def clear(event=None):
    """clear form"""
    diameter.set(0)
    result.set("")
    
btn_clear = ttk.Button(
   control_frame,
   text="Clear",
   command=clear
)

def exit(event=None):
    quit()

btn_exit = ttk.Button(
   control_frame,
   text="Exit",
   command=exit
)
result = tk.StringVar()
result_label = ttk.Label(window, textvariable=result)

util.layout_grid(window,label=label,diameter_entry=diameter_entry,\
    control_frame=control_frame,
    btn_calculate=btn_calculate,btn_clear=btn_clear,btn_exit=btn_exit,\
    result_label=result_label)
# Start the event loop.

window.mainloop()