# Author: Zhanibek Kapen.
# Date: 2023-04-09.
# Description: This programs creates an application, that asks a user two speeds in kilometers in one hour, and then calculates saved kilometers per minute.

# Import tkinter
from tkinter import *
from tkinter.tix import *

def label(text_label, row_label, column_label, sticky_label, wraplength_label = 0, message = None, height_label = None):
    label = Label(text = text_label, border = 2,width = 30, height = height_label, wraplength = wraplength_label, relief = RAISED)
    label.grid(row = row_label, column = column_label , padx = 3, pady =3, sticky = sticky_label)
    label.configure(fg = "#00FF00" , bg = "Black") 
    tooltip.bind_widget(label, msg = message)
    return label
def entry(row_entry, column_entry, message):
    entry = Entry()
    entry.grid(row= row_entry, column= column_entry, sticky = W)
    entry.configure(fg = "#00FF00", bg = "Black")
    tooltip.bind_widget(entry, msg = message)
    return entry
def button(text_button, command, row_button, column_button,  message, columnspan_button = None):
    button = Button(text = text_button, width = 25, command = command)
    button.grid(row=row_button,column = column_button, columnspan = columnspan_button, padx = 1, pady = 1)
    button.configure(fg = "#00FF00", bg = "Black")
    tooltip.bind_widget(button, msg = message)
    return button
def calculate(_event= None):
    try:
        first_car_speed = float(first_car_entry.get())
        second_car_speed= float(second_car_entry.get())
        if first_car_speed > 0 and second_car_speed > 0:
            maximum_speed = max(first_car_speed, second_car_speed)
            minimum_speed = min(first_car_speed, second_car_speed) 
            speed_difference = (maximum_speed-minimum_speed)/60
            result_label.configure(text = ("Going from " + str(first_car_speed) + " km/h to " + str(second_car_speed) + " km/h can gain you " + str(round(speed_difference,1)) +
            " kilometres per minute."))
        else:
            result_label.configure(text = "ERROR: Speed values must be positive numbers.")
    except:
        result_label.configure(text = "ERROR: Speed values must be positive numeric numbers.")
def clear(_event= None):
    """This function cleares all inputs, and then focuses on the first first entry"""
    first_car_entry.delete(0, END)
    second_car_entry.delete(0, END)
    result_label.configure(text="")
    first_car_entry.focus()

# Create a window, and set it's size and minimum size
window = Tk()
window.geometry("450x200")
window.minsize(width = 250, height =200 )
window.title("Speed Difference Calculator")
tooltip = Balloon(window)
window.configure(bg="black")

first_car_label = label("First car's speed", 0, 0, E)
first_car_entry = entry(0, 1,"Enter first car's speed")
first_car_entry.focus()
units_first_car = label("km/h", 0, 2, W)
second_car_label = label("Second car's speed", 1, 0, E)
second_car_entry = entry(1, 1,"Enter second car's speed")
units_second_car = label("km/h", 1, 2, W)
output_label = label("Difference in speed", 2, 0, E)
result_label = label("", 2, 1, W, 150, "Displays a difference in speed result", 3)
calculate_button = button("Calculate", calculate,3, 0, "Click to calculate", 2)
clear_button = button("Clear", clear, 4, 0, "Click to clear entries")
exit_button = button("Exit", exit, 4, 1 , "Click to exit the program")

# Set binds for every button
window.bind("<Escape>", exit)
window.bind("<Alt-x>", clear)
window.bind("<Return>", calculate)

for row_index in range (4):
    window.rowconfigure(row_index, weight = 1)
for column_index in range(3):
    window.columnconfigure(column_index ,weight = 1)

window.mainloop()
 