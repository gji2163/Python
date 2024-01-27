from tkinter import *
m=Tk()

a='*'
l=Label(m,text=a)
l.grid(row=0,column=0)
xx=0

def up(Event):
                          

def rght(Event):
    global a
    a=' '+a
    l.config(text=a)

def dwn(Event):
    global a,l,m,xx
    l.config(text='')
    l=Label(m,text=a)
    xx+=1
    l.grid(row=xx,column=1)

m.bind('<Right>',rght)
m.bind('<Down>',dwn)
