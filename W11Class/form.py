"""
demo hot key
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# root window
root = tk.Tk()
root.geometry("300x250")
#root.resizable(False, False)
root.title('Sign In')

# store email address and password
email = tk.StringVar()
password = tk.StringVar()
number = tk.DoubleVar()

def login_clicked(event=None):
    """ callback when the login button clicked
    """
    msg = f'You entered email: {email.get()}, password: {password.get()}, Double: {number.get()}'
    messagebox.showinfo(
        title='Information',
        message=msg
    )


# Sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

# email
email_label = ttk.Label(signin, text="Email Address:")
email_label.pack(fill='x', expand=True)

# Create a Balloon object (tooltip)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

# password
password_label = ttk.Label(signin, text="Password:")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=password, show="*")
password_entry.pack(fill='x', expand=True)

# number
number_label = ttk.Label(signin, text="Double:")
number_label.pack(fill='x', expand=True)

number_entry = ttk.Entry(signin, textvariable=number)
number_entry.pack(fill='x', expand=True)

# login button
login_button = ttk.Button(signin, text="Login", underline=0, command=login_clicked)
login_button.pack(fill='x', expand=True, pady=10)
root.bind('<Alt-l>', login_clicked)

root.mainloop()
