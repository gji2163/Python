from os import path,listdir
from tkinter import *

m=Tk()
m.title("Save As")
files = [f for f in listdir('E:\\') if not path.isfile(f)]

def search(Event,txt=''):
    global files
    for i in files:
        if sear.get() in i:
            txt+=i+"\n"
        Labe.config(text=txt)

def loca(Event,txt=''):
    if loc.get()=='':
        x="E:\\"
    else:
        x=loc.get()
    files = [f for f in listdir(x) if not path.isfile(f)]
    for i in files:
        if sear.get() in i:
            txt+=i+"\n"
        Labe.config(text=txt)

b=Button(m,text="..",relief="flat")
b.grid(row=0,column=0)
    
loc=Entry(m,text=path.realpath(__file__))
loc.grid(row=0,column=1)
loc.config(width=60)
loc.bind('<Return>',loca)

sear=Entry(m)   
sear.grid(row=0,column=2)
sear.bind('<Return>',search)

Labe=Label(m,text="")
Labe.grid(row=1,column=1)



