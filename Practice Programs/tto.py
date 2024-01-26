from tkinter import *
m=""
win=Tk()
i="O"
a=[["" for j in range(3)] for k in range(3)]
b1,b2,b3,b4,b5,b6,b7,b8,b9="","","","","","","","",""
z=0
def check():
    global a
    for key in range(3):
        if a[key][0]==a[key][1]==a[key][2]=="O" or a[0][key]==a[1][key]==a[2][key]=="O":
            print("O won")
            m.destroy()
        elif a[key][0]==a[key][1]==a[key][2]=="X" or a[0][key]==a[1][key]==a[2][key]=="X":
            print("X won")
            m.destroy()
    if a[0][0]==a[1][1]==a[2][2] or a[0][2]==a[1][1]==a[2][0]:
        if a[1][1]=="O":
            print("O won")
            m.destroy()
        elif a[1][1]=="X":
            print("X won")
            m.destroy()
def x1():
    global i,a,z
    if b1.cget("text")=="":
        a[0][0]=i
        b1.config(text=i)
        if i=="O":
            i="X"
        else:
            i="O"
    z+=1;check()
def x2():
    global i,a,z
    if b2.cget("text")=="":
        a[0][1]=i
        b2.config(text=i)
        if i=="O":
            i="X"
        else:
            i="O"
    z+=1;check()
def x3():
    global i,a,z
    if b3.cget("text")=="":
        a[0][2]=i
        b3.config(text=i)
        if i=="O":
            i="X"
        else:
            i="O"
    z+=1;check()
def x4():
    global i,a,z
    if b4.cget("text")=="":
        a[1][0]=i
        b4.config(text=i)
        if i=="O":
            i="X"
        else:
            i="O"
    z+=1;check()
def x5():
    global i,a,z
    if b5.cget("text")=="":
        a[1][1]=i
        b5.config(text=i)
        if i=="O":
            i="X"
        else:
            i="O"
    z+=1;check()
def x6():
    global i,a,z
    if b6.cget("text")=="":
        a[1][2]=i
        b6.config(text=i)
        if i=="O":
            i="X"
        else:
            i="O"
    z+=1;check()
def x7():
    global i,a,z
    if b7.cget("text")=="":
        a[2][0]=i
        b7.config(text=i)
        if i=="O":
            i="X"
        else:
            i="O"
    z+=1;check()
def x8():
    global i,a,z
    if b8.cget("text")=="":
        a[2][1]=i
        b8.config(text=i)
        if i=="O":
            i="X"
        else:
            i="O"
    z+=1;check()
def x9():
    global i,a,z
    if b9.cget("text")=="":
        a[2][2]=i
        b9.config(text=i)
        if i=="O":
            i="X"
        else:
            i="O"
    z+=1;check()

def x(event):
    global m,b1,b2,b3,b4,b5,b6,b7,b8,b9
    m=Tk()
    b1=Button(m,text="",command=x1,width=5,relief=e.get())
    b2=Button(m,text="",command=x2,width=5,relief=e.get())
    b3=Button(m,text="",command=x3,width=5,relief=e.get())
    b4=Button(m,text="",command=x4,width=5,relief=e.get())
    b5=Button(m,text="",command=x5,width=5,relief=e.get())
    b6=Button(m,text="",command=x6,width=5,relief=e.get())
    b7=Button(m,text="",command=x7,width=5,relief=e.get())
    b8=Button(m,text="",command=x8,width=5,relief=e.get())
    b9=Button(m,text="",command=x9,width=5,relief=e.get())
    for j in range(9):
        exec("b"+str(j+1)+".grid(row='"+str(j//3)+"',column='"+str(j%3+1)+"')")
    win.destroy()
l=Label(win,text="ENTER BOARD TYPE: flat,groove,raised,ridge,solid,sunken",font="bold")
l.pack()
e=Entry(win)
e.pack()
win.bind('<Return>',x)
win.mainloop()
