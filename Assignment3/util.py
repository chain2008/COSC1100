"""
Assignment1: Pizza
"""
import math

DIAMETER_CONFIG = {
    8:4,
    12:6,
    14:8,
    16:10,
    20:12,
    math.inf:16
    }

def get_slices(diameter):
    """get slice out of diameter"""
    if diameter<6 or diameter>36:
        raise ValueError("Diameter should be between 6 and 36")

    slice_cuts = 0
    for diameter_setting in DIAMETER_CONFIG.items():
        if diameter < diameter_setting[0]:
            slice_cuts = diameter_setting[1]
            break
    return slice_cuts

def center(window,width,height):
    """put window in the center of screen"""
    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - width / 2)
    center_y = int(screen_height/2 - height / 2)

    # set the position of the window to the center of the screen
    window.geometry(f'{width}x{height}+{center_x}+{center_y}')

def layout_grid(master, **widgets):
    """
    layout widgets.
    """
    master.grid_columnconfigure(0, weight=1)
    master.grid_columnconfigure(1, weight=1)
    master.grid_rowconfigure(0, weight=1)
    master.grid_rowconfigure(1, weight=1)
    master.grid_rowconfigure(2, weight=3)


    widgets["label"].grid(row=0, column=0, sticky="nsew")
    widgets["diameter_entry"].grid(row=0, column=1, sticky="nsew")

    widgets["control_frame"].grid(row=1, column=0, columnspan=2, sticky="nsew")

    widgets["control_frame"].grid_columnconfigure(0, weight=1)
    widgets["control_frame"].grid_columnconfigure(1, weight=1)
    widgets["control_frame"].grid_columnconfigure(2, weight=1)
    widgets["btn_calculate"].grid(row=0, column=0, sticky="nsew")
    widgets["btn_clear"].grid(row=0, column=1, sticky="nsew")
    widgets["btn_exit"].grid(row=0, column=2, sticky="nsew")

    widgets["result_label"].grid(row=2, column=0, columnspan=2, sticky="nsew")
