"""
https://matplotlib.org/stable/api/index.html
"""
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np

def pie(master,slice):
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5), dpi = 100)
    plot1 = fig.add_subplot()
    y = np.array([100/slice]*slice)
    plot1.pie(y)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master = master)
    canvas.draw()
    # placing the canvas on the Tkinter window
    return canvas.get_tk_widget()

def plot(master):

    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5), dpi = 100)

    # list of squares
    y = [i**2 for i in range(101)]

    # adding the subplot
    plot1 = fig.add_subplot(111)

    # plotting the graph
    plot1.plot(y)

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master = master)
    canvas.draw()
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, master)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
