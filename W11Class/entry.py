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