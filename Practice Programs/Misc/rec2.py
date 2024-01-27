from tkinter import Tk,Button
import sounddevice as sd
from scipy.io.wavfile import write as w
from numpy import ndarray as a
m=Tk()
check=1

def init():
    global check
    check=1

def strt():
    global myrec
    if check:
        try:
            myrec+=sd.rec(50, samplerate=50000, channels=2)
        except Exception as e:
            print(e)
            myrec=sd.rec(50, samplerate=50000, channels=2)
        m.after(1,strt)
        b1.config(text="Stop",command=stp)
    else:
        init()

def stp():
    global check
    check=0
    b1.config(text="Start",command=strt)
    w(input("File Name:")+".wav",50000,myrec)
    print(myrec)
b1=Button(m,text="Start",command=strt)
b1.grid(row=0,column=0)
