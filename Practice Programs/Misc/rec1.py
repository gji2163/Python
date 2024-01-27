import sounddevice as sd
from scipy.io.wavfile import write
from numpy import array
from tkinter import *

m=Tk()
drw=0
myrecording=[]

try:
    int("r")
    fs=10000*int(input("Enter quality(Default is 5):"))
except:    
    fs = 50000  # Sample rate

def choose():
    global myrecording
    if drw:                       #Varying Condition
        a=sd.rec(int(fs/20), samplerate=fs, channels=2)
        myrecording+=list(a)
        m.after(50,choose)      #Enter time delay here
    else:
        print(myrecording)
        write('output.wav', fs, array(myrecording))  # Save as WAV file
    
def draw(event):                  #Binding Space press
    global drw
    drw=(drw+1)%2
    choose()
           
m.bind("<space>", draw)           #Bind call

#sd.wait()  # Wait until recording is finished
#print(type(myrecording[0]))
#write(input(location))  #End statement
