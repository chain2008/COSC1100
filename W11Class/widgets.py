"""
Tkinter widgets are the building blocks of any Tkinter-based GUI application. 
They are the elements that make up the user interface, 
allowing you to display information and interact with the user. 
Here are some of the most commonly used Tkinter widgets

https://www.pythontutorial.net/tkinter/tkinter-ttk/
"""

import tkinter as tk
from tkinter import ttk
import gui_util

root = tk.Tk()
root.title("Durham College - COSC1100")

gui_util.center(root,600,400)

root.mainloop()
