from tkinter import *
import pyautogui
from keyboard import add_hotkey, remove_hotkey
from os import system
pyautogui.FAILSAFE=False
t='0'

var = True
def end():
    try:
        StrVar.set('False')
    except:
        global var
        var=False

add_hotkey('Esc', end)     
while True:   
    try:

        def my_r(*args):
            global t
            t=string.get()
            m.destroy()

        def key_press(var=None):
            string.set( "{:.1f}".format(float(string.get())+var) )

        def check(*args):
            try:
                float(string.get())
            except:
                string.set('0')

        def Quit(event):
            icon.stop()
            system("taskkill /im novel_reader.exe /f")

        m=Tk()
        m.title('')
        m.overrideredirect(1)
        m.eval('tk::PlaceWindow . center')
                
        StrVar = StringVar(m)
        StrVar.set('True')
        
        string = StringVar(m)
        string.set(t)
            
        b1= Button(m,text="<",font=('BellMT',15), bg='white', command=lambda: string.set( "{:.1f}".format(float(string.get())-.1) ))
        b1.grid(row=0,column=0,sticky="nsew")

        e= Entry(m, textvariable=string, font=('BellMT',15), width=5,justify='center')
        e.grid(row=0,column=1,sticky="ns")
        e.icursor("end")
        e.focus_force()

        b2= Button(m,text=">", font=('BellMT',15) ,bg='white', command=lambda: string.set( "{:.1f}".format(float(string.get())+.1) ))
        b2.grid(row=0,column=2,sticky="nsew")

        b= Button(m,text="Submit", font=('BellMT',15), bg='white', command=my_r)
        b.grid(row=1,column=0,columnspan=3,sticky="nsew")

        #Binding        
        m.bind('<Return>', my_r)
        m.bind('<space>', Quit)

        m.bind('<Up>', lambda event: key_press(var=.1))
        m.bind('<Down>', lambda event: key_press(var=-.1))

        string.trace('w',check)
        StrVar.trace('w',my_r)

        m.mainloop()

        print(t)
        if float(t):
            while True:      
                if pyautogui.position()[0] not in [0, pyautogui.size()[0]-1] or pyautogui.position()[1] not in [0, pyautogui.size()[0]-1]:
                    for i in range(10):
                        pyautogui.press('down')
                    for i in range(10):
                        if not var:
                            raise KeyboardInterrupt
                        pyautogui.sleep(float(t))
                else:
                    pyautogui.sleep(20)

        while True:
            if not var:
                raise KeyboardInterrupt
        
            if pyautogui.position()[0] not in [0, pyautogui.size()[0]-1] or pyautogui.position()[1] not in [0, pyautogui.size()[0]-1]:
                pyautogui.press('down')
            else:
                pyautogui.sleep(4)
    except ValueError:
        if float(t)<0:
            Quit()
        t='0'
    except KeyboardInterrupt:
        var = True
