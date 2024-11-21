# Author: Kyle Chapman
# Date: March 29, 2023
# Description:
# This program uses a tkinter UI to help someone determine whether
# they should pass another car.

import tkinter as tk
from tkinter import ttk
from idlelib.tooltip import Hovertip

MINUTES_PER_HOUR = 60
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300

WINDOW_MIN_WIDTH = 220
WINDOW_MIN_HEIGHT = 220

window = tk.Tk()

window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
window.minsize(width = WINDOW_MIN_WIDTH, height = WINDOW_MIN_HEIGHT)

window.title("Should I Pass?")
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=2)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=3)
window.grid_rowconfigure(3, weight=1)

label_1 = ttk.Label(window, text="Your Speed")
label_2 = ttk.Label(window, text="Target Speed")
speed_1 = tk.DoubleVar(value = 0)
speed_2 = tk.DoubleVar(value = 0)
output = tk.StringVar()
entry_speed_1 = ttk.Entry(window, textvariable=speed_1, width=30) #30 characters
entry_speed_2 = ttk.Entry(window, textvariable=speed_2, width=30) #30 characters
label_output = ttk.Label(window, textvariable=output)

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

    # If they don’t both have numbers:
    except Exception as exp:
        # Show an error message in the output labels
        output.set(f"Error: {exp}.")

def reset():
    speed_1.set(0)
    speed_2.set(0)
    output.set("")
    entry_speed_1.focus()

# Now you need to set up the widgets!
# Note that if you use the exact names I did in the functions above, you won't need to modify those.
# If you use a different naming scheme, expect the functions to require some changes.


# Row 0 widgets.
# Add widgets for all rows, based on your plan.
# Add hotkey support.
# Anything else?

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

label_1.grid(row=0, column=0, sticky="nsew")
label_2.grid(row=1, column=0, sticky="nsew")

entry_speed_1.grid(row=0, column=1, sticky="nsew")
entry_speed_2.grid(row=1, column=1, sticky="nsew")

label_output.grid(row=2, column=0, columnspan=2, sticky="nsew")

btn_calculation.grid(row=3, column=1, sticky="w")
btn_reset.grid(row=3, column=1, sticky="e")

window.mainloop()
