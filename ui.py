# https://docs.python.org/3/library/tkinter.html
# https://www.pythontutorial.net/tkinter/
import tkinter as tk

window = tk.Tk()
window.title("Hello World")


def handle_button_press(event):
    window.destroy()


button = tk.Button(text="My simple app.")
button.bind("<Button-1>", handle_button_press) # <Button-1> is the left mouse button click event
button.pack()

# Start the event loop.
window.mainloop()