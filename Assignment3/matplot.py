import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter Matplotlib Demo')

        # Create a figure
        figure = Figure(figsize=(6, 4), dpi=100)
        axes = figure.add_subplot()
        axes.plot([1, 2, 3, 4], [10, 20, 25, 30])
        axes.set_title('Sample Plot')
        axes.set_xlabel('X Axis')
        axes.set_ylabel('Y Axis')

        # Create a canvas and add the figure to it
        canvas = FigureCanvasTkAgg(figure, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Add a toolbar
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        # email
        email_label = ttk.Label(text="Email Address:")
        email_label.pack(fill='x', expand=True)

        # Create a Balloon object (tooltip)

        email_entry = ttk.Entry()
        email_entry.pack(fill='x', expand=True)
        email_entry.focus()

        # password
        password_label = ttk.Label(text="Password:")
        password_label.pack(fill='x', expand=True)

        password_entry = ttk.Entry()
        password_entry.pack(fill='x', expand=True)

        # number
        number_label = ttk.Label(text="Double:")
        number_label.pack(fill='x', expand=True)

        number_entry = ttk.Entry()
        number_entry.pack(fill='x', expand=True)

        # login button
        login_button = ttk.Button(text="Login", underline=0)
        login_button.pack(fill='x', expand=True, pady=10)


if __name__ == '__main__':
    app = App()
    app.mainloop()
