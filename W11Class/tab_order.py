import tkinter as tk

def set_tab_order(widgets):
    for widget in widgets:
        widget.lift()

# Create the main window
root = tk.Tk()
root.geometry("300x200")

# Create some entry widgets
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)
entry4 = tk.Entry(root)

# Pack the widgets
entry1.pack(pady=5)
entry2.pack(pady=5)
entry3.pack(pady=5)
entry4.pack(pady=5)

# Set the desired tab order
set_tab_order([entry1, entry3, entry2, entry4])

# Run the application
root.mainloop()
