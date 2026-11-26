from tkinter import *

Windows = Tk()
Windows.title("Event handler")
Windows.geometry("100x100")

def handle_keypress(event):
    """ print the character associated to the key pressed"""
    print(event.char)

Windows.bind("<Key>", handle_keypress)

def handle_clik(event):
    print("\nthe button was clicked")
button = Button(text="CLICK me !!!")
button.pack()

button.bind("<Button-1>", handle_clik)

Windows.mainloop()