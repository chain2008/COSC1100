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

#themed widget
#https://www.pythontutorial.net/tkinter/tkinter-ttk/
# Create a style object 
style = ttk.Style()
style.configure('TLabel1.TLabel',font=('Helvetica',16),foreground='blue')
# Configure the style for TLabel
style.configure('TLabel2.TLabel',font=('Helvetica',14),foreground='blue')
style.configure('TEntry1.TEntry',font=('Helvetica',16),foreground='blue')

# Create a label with the custom style 
email_label = ttk.Label(root, text="Email Address:", style='TLabel1.TLabel')
email_label.place(x=50, y=50)
# Typically, we associate the current value of the textbox with a StringVar object
email = tk.StringVar()
email.set("cheng.he@durhamcollege.ca")
email_entry = ttk.Entry(root, 
    textvariable=email, 
    width=30,
    style='TLabel2.TLabel') #30 characters
email_entry.place(x=200, y=50)

email_entry.focus()
root.mainloop()
