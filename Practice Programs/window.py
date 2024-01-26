from tkinter import *
from tkinter.ttk import *
import time

	
root = Tk()

progress = Progressbar(root, orient = VERTICAL,
			length = 100, mode = 'indeterminate')
ii=0
c = ['Start', 'Stop']

def com():
    for i in range(105):
        progress['value'] = i
        root.update_idletasks()
        root.after(10)
    if ii==0:
        com()

def bar():
    global ii
    ii = (ii+1)%2
    b['text'] = c[ii]
    if ii==0:
        com()        

progress.pack(pady = 10)
b = Button(root, text = 'Start', command = bar)
b.pack(pady = 10)

root.mainloop()
'''

m = Tk()

progress = Progressbar(root, orient = HORIZONTAL,
			length = 100, mode = 'determinate')

'''
