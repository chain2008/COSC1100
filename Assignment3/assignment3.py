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
    # do something
    slices = util.get_slices(diameter.get())

btn_calculate = ttk.Button(
   control_frame,
   text="Calculate",
   command=calculate
)

def clear(event=None):
    # do something
    pass
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

result = ttk.Label(window, text="")

util.layout_grid(window,label=label,diameter_entry=diameter_entry,\
    control_frame=control_frame,
    btn_calculate=btn_calculate,btn_clear=btn_clear,btn_exit=btn_exit,\
    result=result)
# Start the event loop.
window.mainloop()