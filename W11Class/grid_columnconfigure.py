import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")

#we set up grid here
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=2)

f1 = tk.Frame(root, background="bisque", height=50)
f2 = tk.Frame(root, background="pink", height=50)

f1.grid(row=0, column=0, sticky="nsew")
f2.grid(row=0, column=1, sticky="nsew")


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
   text="Demo Button"
)
btn2.grid(row=1, column=2, sticky="nsew")

#image = download_icon.resize((100, 100))
btn3 = ttk.Button(
   root,
   text="Demo Button"
)
btn3.grid(row=1, column=0, columnspan=2, padx=15, pady=10,sticky="nsew")

root.mainloop()
