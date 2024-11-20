"""
https://www.pythontutorial.net/tkinter/tkinter-window/
Demo:
window.geometry('600x400-50+50')
window.geometry('600x400+50+50')
center(window,600,400)
create_new_window()
"""
import tkinter as tk
import gui_util
width = 400
height = 300

window = tk.Tk()
window.title("Durham College - COSC1100")

gui_util.center(window, width, height)

window.minsize(100, 60)
window.maxsize(800, 600)

window.mainloop()
