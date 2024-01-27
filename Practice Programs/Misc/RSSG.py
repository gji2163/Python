from tkinter import *
from mysql import connector as c
from keyboard import add_hotkey
from os import system

def Quit(event):
    system('taskkill /im data.exe /f')

conn = c.connect(
    user = 'root',
    host = 'localhost',
    db = 'Novel_data',
    password = 'Giks@1602'
    )

m=Tk()
m.title('')
m.overrideredirect(1)
m.eval('tk::PlaceWindow . center')

m.bind('<space>',Quit)

m.mainloop()    
