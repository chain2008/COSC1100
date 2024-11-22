"""Module utlities"""

def layout_grid(master, **widgets):
    """
    layout widgets.
    """
    master.grid_columnconfigure(0, weight=1)
    master.grid_columnconfigure(1, weight=2)
    master.grid_rowconfigure(0, weight=1)
    master.grid_rowconfigure(1, weight=1)
    master.grid_rowconfigure(2, weight=3)
    master.grid_rowconfigure(3, weight=1)

    widgets["label_1"].grid(row=0, column=0, sticky="nsew")
    widgets["label_2"].grid(row=1, column=0, sticky="nsew")

    widgets["entry_speed_1"].grid(row=0, column=1, sticky="nsew")
    widgets["entry_speed_2"].grid(row=1, column=1, sticky="nsew")

    widgets["label_output"].grid(row=2, column=0, columnspan=2, sticky="nsew")

    widgets["btn_calculation"].grid(row=3, column=1, sticky="w")
    widgets["btn_reset"].grid(row=3, column=1, sticky="e")
