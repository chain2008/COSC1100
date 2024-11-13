# https://docs.python.org/3/library/tkinter.html
# https://www.pythontutorial.net/tkinter/
import tkinter as tk
import form
window = tk.Tk()
window.title("Pizza Cutter")
form.center(window, 600, 400)
form.layout(window)

# Start the event loop.
window.mainloop()