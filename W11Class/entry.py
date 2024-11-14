# email
email_label = ttk.Label(root, text="Email Address:")
email_label.place(x=50, y=50)

# Typically, we associate the current value of the textbox with a StringVar object
email = tk.StringVar()
email.set("cheng.he@durhamcollege.ca")
email_entry = ttk.Entry(root, textvariable=email, width=30) #30 characters
email_entry.place(x=220, y=50)
email_entry.focus()