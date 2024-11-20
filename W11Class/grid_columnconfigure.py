import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")

f1 = tk.Frame(root, background="bisque", height=200)
f2 = tk.Frame(root, background="pink", height=200)

f1.grid(row=0, column=0, sticky="nsew")
f2.grid(row=0, column=1, sticky="nsew")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)

def callback(event):
    # do something
    root.quit()

download_icon = tk.PhotoImage(file='./W11Class/assets/export_small.png')
#image = download_icon.resize((100, 100))
btn = ttk.Button(
   f2,
   text="Demo Button",
   image=download_icon,
   compound=tk.LEFT,
   command=callback
)
btn.place(x=50, y=5, width=200, height=100)

root.mainloop()
