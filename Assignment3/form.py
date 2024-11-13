import tkinter as tk
from tkinter import ttk

def center(window,width,height):
    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - width / 2)
    center_y = int(screen_height/2 - height / 2)

    # set the position of the window to the center of the screen
    window.geometry(f'{width}x{height}+{center_x}+{center_y}')

def layout(window):
    # configure the grid
    window.columnconfigure(0, weight=1)
    window.rowconfigure(1, weight=3)

    # username
    username_label = ttk.Label(window, text="Username:")
    username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

    username_entry = ttk.Entry(window)
    username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

    # password
    password_label = ttk.Label(window, text="Password:")
    password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

    password_entry = ttk.Entry(window,  show="*")
    password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

    # login button
    login_button = ttk.Button(window, text="Login")
    login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
