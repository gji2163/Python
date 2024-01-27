from playsound import playsound as p
from random import choice as c
from tkinter import *

drw=0
m=Tk()                            #Creating Window
l=[i for i in range(90)]          #Initial Numbers
lbl=Label(m,text="")              #Declaring Label
lbl.pack()

def choose():
    if drw:                       #Varying Condition
        x=c(l)                    #Choosing a number
        l.pop(x)                  
        lbl.config(text=x)        #Displaying Number
        #p(str(x)+".mp3")
        m.after(4000,choose)      #Enter time delay here
    
def draw(event):                  #Binding Space press
    global drw
    drw=(drw+1)%2
    choose()
           
m.bind("<space>", draw)           #Bind call
