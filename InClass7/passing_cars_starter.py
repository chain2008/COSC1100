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

speed_1 = tk.StringVar()
speed_2 = tk.StringVar()
entry_speed_1 = ttk.Entry(window, textvariable=speed_1, width=30) #30 characters
entry_speed_2 = ttk.Entry(window, textvariable=speed_2, width=30) #30 characters
label_output = ttk.Label(window)
entry_speed_1.pack()
entry_speed_2.pack()
label_output.pack()

def calculate(event= None):
    try:
        # Get the value from entry_speed_1 and treat it as a number.
        speed_one = float(speed_1.get())
        # Get the value from entry_speed_2 and treat it as a number.
        speed_two = float(speed_2.get())

        low_speed = min((speed_one, speed_two))
        high_speed = max((speed_one, speed_two))

        speed_difference = high_speed - low_speed

        speed_difference_seconds = speed_difference / MINUTES_PER_HOUR

        label_output.configure(text = "Going from " + str(round(low_speed, 1)) + \
            "km/h to " + str(round(high_speed, 1)) + \
            "km/h can gain you " + str(round(speed_difference_seconds, 2)) + \
            " kilometres per minute.")

    # If they don’t both have numbers:
    except:
        # Show an error message in the output labels
        label_output.configure(text = "Error: speed entries must be numeric.")

def reset():
    speed_1.set("")
    speed_2.set("")
    label_output.configure(text = "")
    entry_speed_1.focus()


# Now you need to set up the widgets!
# Note that if you use the exact names I did in the functions above, you won't need to modify those.
# If you use a different naming scheme, expect the functions to require some changes.


# Row 0 widgets.
# Add widgets for all rows, based on your plan.
# Add hotkey support.
# Anything else?

ttk.Button(
   window,
   text="Calculate",
   compound=tk.LEFT,
   command=calculate
).pack()
ttk.Button(
   window,
   text="Reset",
   compound=tk.LEFT,
   command=reset
).pack()

window.mainloop()

