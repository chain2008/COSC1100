def callback(event=None):
    # do something
    root.quit()

#bind key press event with callback
root.bind('<Alt-l>', callback)