def create_new_window(tk):
    """creat a new window"""
    new_window = tk.Toplevel()
    new_window.title("New Window")
    new_window.geometry("300x100")
    #new_window.resizable(0, 0)
    #new_window.attributes('-topmost', 1)
    #tk.Label(new_window, text="This is a new window").pack()

def center(window,width,height):
    """to center a window with size"""
    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - width / 2)
    center_y = int(screen_height/2 - height / 2)

    # set the position of the window to the center of the screen
    window.geometry(f'{width}x{height}+{center_x}+{center_y}')
