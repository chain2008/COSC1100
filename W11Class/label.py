classic_label = tk.Label(root, text='Classic Label', foreground="Red", font=("Arial 12px",16))
classic_label.pack()

#themed widget
#https://www.pythontutorial.net/tkinter/tkinter-ttk/
# Create a style object 
style = ttk.Style()
style.configure('TLabel1.TLabel',font=('Helvetica',16),foreground='green')
# Configure the style for TLabel
style.configure('TLabel2.TLabel',font=('Helvetica',16),foreground='blue')


# Create a label with the custom style 
label = ttk.Label(root, text="Styled Label", style='TLabel1.TLabel')
label.pack()

themed_label = ttk.Label(root, text='Themed Label', style='TLabel2.TLabel')
themed_label.pack()