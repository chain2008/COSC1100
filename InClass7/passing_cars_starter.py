"""
In Class 7: Passing car
Author: Cheng He
Date: 2024-11-26
Version: 2
"""

import tkinter as tk
from tkinter import ttk
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

style = ttk.Style()
style.configure('TLabel1.TLabel',font=('Helvetica',8),foreground='light gray')
# Configure the style for TLabel
style.configure('TLabel2.TLabel',font=('Helvetica',16),foreground='black')

label_1 = ttk.Label(window, text="Your Speed", style='TLabel1.TLabel')
label_2 = ttk.Label(window, text="Target Speed", style='TLabel2.TLabel')
speed_1 = tk.DoubleVar(value = 0)
speed_2 = tk.DoubleVar(value = 0)
output = tk.StringVar()
entry_speed_1 = ttk.Entry(window, textvariable=speed_1, width=30) #30 characters
entry_speed_2 = ttk.Entry(window, textvariable=speed_2, width=30) #30 characters
label_output = ttk.Label(window, textvariable=output, wraplength=300)
# Make the ScrolledText read-only
#label_output.config(state=tk.DISABLED)

def calculate(event=None):
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

    # If they don’t both have numbers:
    except Exception as exp:
        # Show an error message in the output labels
        output.set(f"Error: {exp}.")

def reset(event=None):
    speed_1.set(0)
    speed_2.set(0)
    output.set("")
    entry_speed_1.focus()

btn_calculation = ttk.Button(
   window,
   text="Calculate", underline=0,
   command=calculate
)
window.bind('<Alt-c>', calculate)
btn_reset = ttk.Button(
   window,
   text="Reset", underline=0,
   compound=tk.LEFT,
   command=reset
)
util.layout_grid(window, label_1=label_1, label_2=label_2, \
            entry_speed_1=entry_speed_1,entry_speed_2=entry_speed_2, \
            label_output=label_output,
            btn_calculation=btn_calculation,btn_reset=btn_reset)

Hovertip(entry_speed_1, "Enter your current speed in km/h.")
Hovertip(entry_speed_2, "Enter your desired speed in km/h.")
Hovertip(btn_calculation, "Click to calculate the time saved.")
Hovertip(btn_reset, "Click to reset the form.")

window.mainloop()
