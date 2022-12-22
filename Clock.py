from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    str=strftime('%H:%M:%S %p')
    label.config(text=str)
    label.after(1000,time)

label = Label(root,font=("Times New Roman",80),background="red",foreground="black" )
label.pack(anchor='center')
time()

mainloop()
