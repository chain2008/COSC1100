# https://docs.python.org/3/library/tkinter.html
# https://www.pythontutorial.net/tkinter/
import tkinter as tk
from tkinter import ttk
import form
import util

window = tk.Tk()
window.title("Pizza Cutter")

form.create_form(window)

util.center(window, 500, 550)
# Start the event loop.
window.mainloop()