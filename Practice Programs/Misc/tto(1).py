from tkinter import *
m = Tk() 
i=0
j=0
a=Label(m,text="")
a.grid(row=0,column=0)
def leftKey(event):
    global i
    if i>0:
        i-=3
    a.config(text="\n"*j+" "*i+"+")
def rightKey(event):
    global i
    i+=3
    a.config(text="\n"*j+" "*i+"+")
def upKey(event):
    global j
    if j>0:
        j-=1
    a.config(text="\n"*j+" "*i+"+")
def downKey(event):
    global j
    j+=1
    a.config(text="\n"*j+" "*i+"+") 
    
frame = Frame(m, width=100, height=100)    
m.bind('<Left>', leftKey)    
m.bind('<Right>', rightKey)
m.bind('<Up>', upKey)
m.bind('<Down>', downKey)
frame.grid(row=1,column=1)
m.mainloop()
