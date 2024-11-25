import tkinter as tk
from tkinter import ttk

window = None
login_button = None
user_name = tk.StringVar()



def layout(window):
    global login_button
    global username_entry
    # configure the grid
    window.columnconfigure(0, weight=1)
    window.rowconfigure(1, weight=3)

    # username
    username_label = ttk.Label(window, text="Username:")
    username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

    username_entry = ttk.Entry(window, textvariable=user_name)
    username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

    # password
    password_label = ttk.Label(window, text="Password:")
    password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

    password_entry = ttk.Entry(window,  show="*")
    password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

    # login button
    login_button = ttk.Button(window, text="Login")
    login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
