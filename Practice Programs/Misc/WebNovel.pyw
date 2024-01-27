from tkinter import *

import pyautogui
pyautogui.FAILSAFE=False
t='0'

pyautogui.press('f11')

while True:
    try:
        def my_r(Event=None):
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

        m=Tk()
        m.title('')
        m.overrideredirect(1)
        m.eval('tk::PlaceWindow . center')
                
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

        m.bind('<Up>', lambda event: key_press(var=.1))
        m.bind('<Down>', lambda event: key_press(var=-.1))

        string.trace('w',check)
       
        m.mainloop()

        print(t)
        if float(t):
            while True:
                if pyautogui.position() not in [(i,j) for i in [0,pyautogui.size()[0]-1] for j in [0,pyautogui.size()[1]-1]]:
                    for i in range(10):
                        pyautogui.press('down')
                    pyautogui.sleep(float(t)*10)
                else:
                    pyautogui.sleep(20)

        while True:
            if pyautogui.position() not in [(i,j) for i in [0,pyautogui.size()[0]-1] for j in [0,pyautogui.size()[1]-1]]:
                pyautogui.press('down')
            else:
                pyautogui.sleep(4)
    except ValueError:
        t='0'
    except KeyboardInterrupt:
        continue

