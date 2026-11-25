from tkinter import *

root = Tk()
root .title('login pad')
root.geometry('400x400')

frame = Frame(master=root, height=200, width=360, bg ="#d0efff")

lbl1 =Label(frame, text="full name", bg = "#3895d3", fg = 'white', width=12)
lbl2 =Label(frame, text="email id", bg = "#3895d3", fg = 'white', width=12)
lbl3 =Label(frame, text="enter password", bg = "#3895d3", fg = 'white', width=12)

name_entry = Entry(frame)
emaIl_entry = Entry(frame)
pass_entry = Entry(frame , show="*")

def display():
    name = name_entry.get()
    greet = "hey"+name
    message = "\ncongratulation for your new account"