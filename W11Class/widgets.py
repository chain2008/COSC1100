"""
Tkinter widgets are the building blocks of any Tkinter-based GUI application. 
They are the elements that make up the user interface, 
allowing you to display information and interact with the user. 
Here are some of the most commonly used Tkinter widgets
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import gui_util

root = tk.Tk()
root.title("Durham College - COSC1100")

gui_util.center(root,600,400)

f1 = tk.Frame(root, background="bisque", height=200)
f2 = tk.Frame(root, background="pink", height=200)

f1.grid(row=0, column=0, sticky="nsew")
f2.grid(row=0, column=1, sticky="nsew")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)



download_icon = tk.PhotoImage(file='./W11Class/assets/export_small.png')
#image = download_icon.resize((100, 100))
btn = ttk.Button(
   f2,
   text="Demo Button",
   image=download_icon,
   compound=tk.LEFT
)
btn.place(x=50, y=5, width=200, height=100)

#image = download_icon.resize((100, 100))
btn2 = ttk.Button(
   root,
   text="Demo Button",
   image=download_icon,
   compound=tk.LEFT
)
btn2.place(x=50, y=5, width=200, height=100)

root.mainloop()
