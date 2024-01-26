from tkinter import *
m=Tk()
i="O"
def x1():
    global i
    b1=Button(m,text=i,command=X1)
    b1.grid(row=0,column=0)
    if i=="O":
        i="X"
    else:
        i="O"
def X1():
    global i
    b1=Button(m,text=i,command=x1)
def x2():
    global i
    b1=Button(m,text=i,command=X1)
    b1.grid(row=0,column=0)
    if i=="O":
        i="X"
    else:
        i="O"
def x3():
    global i
    b1=Button(m,text=i,command=X1)
    b1.grid(row=0,column=0)
    if i=="O":
        i="X"
    else:
        i="O"
def x4():
    global i
    b1=Button(m,text=i,command=X1)
    b1.grid(row=0,column=0)
    if i=="O":
        i="X"
    else:
        i="O"
def x5():
    global i
    b1=Button(m,text=i,command=X1)
    b1.grid(row=0,column=0)
    if i=="O":
        i="X"
    else:
        i="O"
def x6():
    global i
    b1=Button(m,text=i,command=X1)
    b1.grid(row=0,column=0)
    if i=="O":
        i="X"
    else:
        i="O"
def x7():
    global i
    b1=Button(m,text=i,command=X1)
    b1.grid(row=0,column=0)
    if i=="O":
        i="X"
    else:
        i="O"
def x8():
    global i
    b1=Button(m,text=i,command=X1)
    b1.grid(row=0,column=0)
    if i=="O":
        i="X"
    else:
        i="O"
def x9():
    global i
    b1=Button(m,text=i,command=X1)
    b1.grid(row=0,column=0)
    if i=="O":
        i="X"
    else:
        i="O"
for j in range(9):
    exec("b"+str(j+1)+"=Button(m,text=\"\",command=x"+str(j+1)+")")
    exec("b"+str(j+1)+".grid(row=\""+str(j//3)+"\",column=\""+str(j%3+1)+"\")")
