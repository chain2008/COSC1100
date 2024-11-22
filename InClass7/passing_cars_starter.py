"""
In Class 7: Passing car
Author: Cheng He
Date: 2024-11-22
Version: 1
"""

import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from idlelib.tooltip import Hovertip

import util

MINUTES_PER_HOUR = 60
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300

WINDOW_MIN_WIDTH = 220
WINDOW_MIN_HEIGHT = 220

window = tk.Tk()

window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
window.minsize(width = WINDOW_MIN_WIDTH, height = WINDOW_MIN_HEIGHT)

window.title("Should I Pass?")

label_1 = ttk.Label(window, text="Your Speed")
label_2 = ttk.Label(window, text="Target Speed")
speed_1 = tk.DoubleVar(value = 0)
speed_2 = tk.DoubleVar(value = 0)
output = tk.StringVar()
entry_speed_1 = ttk.Entry(window, textvariable=speed_1, width=30) #30 characters
entry_speed_2 = ttk.Entry(window, textvariable=speed_2, width=30) #30 characters
label_output = ScrolledText(window, height=5)
# Make the ScrolledText read-only
#label_output.config(state=tk.DISABLED)

def calculate(event= None):
    try:
        # Get the value from entry_speed_1 and treat it as a number.
        speed_one = speed_1.get()
        # Get the value from entry_speed_2 and treat it as a number.
        speed_two = speed_2.get()

        low_speed = min((speed_one, speed_two))
        high_speed = max((speed_one, speed_two))

        speed_difference = high_speed - low_speed

        speed_difference_seconds = speed_difference / MINUTES_PER_HOUR

        output.set("Going from " + str(round(low_speed, 1)) + \
            "km/h to " + str(round(high_speed, 1)) + \
            "km/h can gain you " + str(round(speed_difference_seconds, 2)) + \
            " kilometres per minute.")
        label_output.delete('1.0', tk.END)
        label_output.insert(tk.END,output.get())

    # If they don’t both have numbers:
    except Exception as exp:
        # Show an error message in the output labels
        output.set(f"Error: {exp}.")

def reset():
    speed_1.set(0)
    speed_2.set(0)
    output.set("")
    entry_speed_1.focus()

btn_calculation = ttk.Button(
   window,
   text="Calculate",
   compound=tk.LEFT,
   command=calculate
)
btn_reset = ttk.Button(
   window,
   text="Reset",
   compound=tk.LEFT,
   command=reset
)
util.layout_grid(window, label_1=label_1, label_2=label_2, \
            entry_speed_1=entry_speed_1,entry_speed_2=entry_speed_2, \
            label_output=label_output,
            btn_calculation=btn_calculation,btn_reset=btn_reset)


window.mainloop()
