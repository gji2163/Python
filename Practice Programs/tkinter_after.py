from tkinter import Tk,Button
from time import sleep as s

m=Tk()
check=1

def init():
    global check
    check=1

def strt():
    if check:
        print(1)
        m.after(200,strt)
        b1.config(text="Stop",command=stp)
    else:
        init()

def stp():
    global check
    check=0
    b1.config(text="Start",command=strt)

b1=Button(m,text="Start",command=strt)
b1.grid(row=0,column=0)
