#button = ttk.Button(master, **option) see func.py
def callback(event=None):
    # do something
    root.quit()

download_icon = tk.PhotoImage(file='./W11Class/assets/export_small.png')
#image = download_icon.resize((100, 100))
btn = ttk.Button(
   root,
   text="Demo Button",
   image=download_icon,
   compound=tk.LEFT,
   command=callback
)
btn.place(x=50, y=5, width=200, height=100)