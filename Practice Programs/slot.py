from tkinter import *
import time
from PIL import ImageTk,Image
from random import choices
from collections import namedtuple
from time import sleep
from psutil import sensors_battery as bat

battery = bat()

win=Tk()
win.attributes('-fullscreen',True)
win.config(background='blue')

f=open('data.txt','r+')
m=Frame(win,height=50, background = 'purple')
m.pack(fill='x')

head=Label(m,text="Slot Machine")

label1=Label(m,anchor="nw")
label1.pack(side=LEFT)
label2=Label(m,text="    "+str(battery.percent)+'% | '+("Plugged In" if battery.power_plugged else "Not Plugged In"),anchor="nw", font = ('BellMT', 10, 'bold'), foreground='white' ,background='purple')
label2.pack(side=LEFT)

photo = ImageTk.PhotoImage(file = "reset.png")
Button(m,height=50,width=50,anchor="ne",image=photo,command=lambda: l.config(text="$10.00"), background='purple').pack(side=RIGHT)

l = Label(m,text="$"+f.read()+".00",anchor="n",font = ('BellMT', 30, 'bold'), foreground = 'white', background = 'purple')
l.pack(side=RIGHT)

game=Frame(win, height=500, background='blue')
game.pack(fill='x')

l1=Label(game,image=photo,background='cyan',height=300, width=250)
l1.place(x=150,y=200)

l2=Label(game,image=photo,background='cyan',height=300, width=250)
l2.place(x=650,y=200)

l3=Label(game,image=photo,background='cyan',height=300, width=250)
l3.place(x=1150,y=200)

lr= Label(win,text = '\nPress Start', font = ('BellMT', 30, 'bold'), background = 'blue')
lr.pack()

Fruits = namedtuple('Fruit', ['name', 'weight', 'reward'])
fruits = [
        Fruits(name="apple", weight=10000, reward=1),
        Fruits(name="banana", weight=5000, reward=2),
        Fruits(name="lemon", weight=4000, reward=3),
        Fruits(name="cherry", weight=3000, reward=4),
        Fruits(name="bar", weight=2000, reward=5),
        Fruits(name="peach", weight=400, reward=6),
        Fruits(name="diamond", weight=300, reward=10),
        Fruits(name="grapes", weight=200, reward=20),
        Fruits(name="7", weight=100, reward=100),
        Fruits(name="melon", weight=1, reward=10000)
        ]

def bal(val):
    l.config(text="$"+str(int(l['text'][1:-3])+val)+".00")
    f.seek(0)
    f.write(str(int(l['text'][1:-3])+val))
    f.flush()
    
def start(event=None):
    global game
    a,b,c = choices(fruits,
                    k=3,
                    weights=[fruit.weight for fruit in fruits]
                    )

    bal(-1)
    if a.name == b.name == c.name:
        bal(a.reward * 3)
        lr.config(text='\nCongratulations!! You got 3 '+a.name+" :)")
    elif a.name == b.name or a.name == c.name or b.name == c.name:
        if b.name == c.name:
            bal(c.reward * 2)
            lr.config(text='\nCongratulations!! You got 2 '+c.name+" :)")
        else:
            bal(a.reward * 2)
            lr.config(text='\nCongratulations!! You got 2 '+a.name+" :)")
    else:
        lr.config(text='\nSorry. Better Luck Next Time :(')
            
    p=a.name+'.png'
    photo1=ImageTk.PhotoImage(file=p)
    l1['image']=photo1

    p=b.name+'.png'
    photo2=ImageTk.PhotoImage(file=p)
    l2['image']=photo2

    p=c.name+'.png'
    photo3=ImageTk.PhotoImage(file=p)
    l3['image']=photo3
    int('f')

b=Button(win,text='Start',command=start, font = ('BellMT', 30, 'bold'), background = 'light blue')
b.pack(fill='x',side='bottom')

def clock():
    t=time.strftime('%I:%M:%S %p',time.localtime())
    if t!='':
        label1.config(text=t,font = ('calibri', 30, 'bold'),
			background = 'purple',
			foreground = 'white')
    win.after(1000,clock)

clock()
win.mainloop()
