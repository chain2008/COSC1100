import tkinter as tk

# Create the master object
master = tk.Tk()
master.geometry("240x100") 
# Create the label objects and pack them using grid
tk.Label(master, text="Label 1").grid(row=0, column=0)
tk.Label(master, text="Label 2").grid(row=1, column=0)

# Create the entry objects using master
e1 = tk.Entry(master)
e2 = tk.Entry(master)

# Pack them using grid
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

#button span 2 columns
button1 = tk.Button(master, text="Button 1")
button1.grid(columnspan=2, row=2, column=0)
# The mainloop
tk.mainloop()
