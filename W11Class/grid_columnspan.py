import tkinter as tk
from tkinter import ttk
import gui_util

root = tk.Tk()
root.title("Durham College - COSC1100")

gui_util.center(root,600,400)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)
root.grid_columnconfigure(3, weight=2)

# Create the label objects and pack them using grid
label1 = ttk.Label(root, text="Label 1")
label1.grid(row=0, column=0)
labe12 = ttk.Label(root, text="Label 2")
labe12.grid(row=1, column=0)

# Create the entry objects using master
e1 = ttk.Entry(root)
e2 = ttk.Entry(root)

# Pack them using grid
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

#button span 2 columns
button1 = tk.Button(root, text="Button 1")
button1.grid(columnspan=2, row=2, column=0)
# The mainloop
tk.mainloop()
