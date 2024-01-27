from tkinter import *
from tkinter.ttk import * 
from time import strftime

m=Tk()
m.configure(bg='black')
m.resizable(0,0)

l=0


def clear():
    global l
    l=0
    conf()

def res():
    pass

def conf():
    lab.config(text=l)

def k0():
    global l
    l=10*l
    conf()

def backspace():
    global l
    l=l//10
    conf()

def plus():
    pass

def minus():
    pass

def mult():
    pass

def div():
    pass

lab=Label(m,text=l,width=20,font=('Helvetica',16,'bold'),bg='black',fg='orange')
lab.grid(row=0,column=1)

bcl=Button(m,text='C',command=clear,width=10,font=('Helvetica',16,'bold'),bg='black',fg='orange')
bcl.grid(row=1,column=0)

bck=Button(m,text='<=',command=backspace,width=10,font=('Helvetica',16,'bold'),bg='black',fg='orange')
bck.grid(row=1,column=2)

bres=Button(m,text='=',command=res,width=10,font=('Helvetica',16,'bold'),bg='black',fg='orange')
bres.grid(row=5,column=3)

#Number Keys
b0=Button(m,text='0',command=k0,width=10,font=('Helvetica',16,'bold'),bg='black',fg='orange')
b0.grid(row=5,column=1)

for i in range(1,10):
    exec("def k"+str(i)+"():\n\tglobal l\n\tl=10*l+"+str(i)+"\n\tconf()")
    exec("b"+str(i)+"=Button(m,text='"+str(i)+"',width=10,font=('Helvetica',16,'bold'),bg='black',fg='orange',command=k"+str(i)+")\nb"+str(i)+".grid(row="+str((i+5)//3)+",column="+str((i+2)%3)+")")

#Operators
bplus=Button(m,text='+',command=plus,width=10,font=('Helvetica',16,'bold'),bg='black',fg='orange')
bplus.grid(row=1,column=3)

bminus=Button(m,text='-',command=minus,width=10,font=('Helvetica',16,'bold'),bg='black',fg='orange')
bminus.grid(row=2,column=3)

bmult=Button(m,text='*',command=mult,width=10,font=('Helvetica',16,'bold'),bg='black',fg='orange')
bmult.grid(row=3,column=3)

bdiv=Button(m,text='/',command=div,width=10,font=('Helvetica',16,'bold'),bg='black',fg='orange')
bdiv.grid(row=4,column=3)

