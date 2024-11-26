# https://docs.python.org/3/library/tkinter.html
# https://www.pythontutorial.net/tkinter/
import tkinter as tk
from tkinter import ttk
import form


window = tk.Tk()
window.title("Pizza Cutter")

frame1 = ttk.Frame(window)

form.create_form(frame1)
frame1.pack()

# Start the event loop.
window.mainloop()