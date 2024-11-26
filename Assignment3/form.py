import tkinter as tk
from tkinter import ttk
import util
import graph

canvas = None
def create_form(master):    
    label = ttk.Label(master, text="Diameter: ")

    diameter = tk.DoubleVar()
    diameter_entry = ttk.Entry(master, textvariable=diameter)

    control_frame = tk.Frame(master, background="bisque")
    graph_frame = tk.Frame(master, background="bisque")
    def calculate(event=None):
        """calculate pizza slices"""
        global canvas
        try:
            slices = util.get_slices(diameter.get())
            result.set(f"can cut into {slices} slices")
            if canvas is not None:
                canvas.destroy()
            canvas = graph.pie(graph_frame, slices)
            canvas.pack()
        except Exception as exp:
            result.set(exp)

    btn_calculate = ttk.Button(control_frame,text="Calculate",command=calculate)

    def clear(event=None):
        """clear form"""
        diameter.set(0)
        result.set("")
        
    btn_clear = ttk.Button(control_frame,text="Clear",command=clear)

    def exit(event=None):
        quit()

    btn_exit = ttk.Button(control_frame,text="Exit",command=exit)
    result = tk.StringVar()
    result_label = ttk.Label(master, textvariable=result)

    util.layout_grid(master,label=label,diameter_entry=diameter_entry,\
        control_frame=control_frame, graph_frame=graph_frame,
        btn_calculate=btn_calculate,btn_clear=btn_clear,btn_exit=btn_exit,\
        result_label=result_label)
