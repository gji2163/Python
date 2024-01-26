from tkinter import *
import shutil         
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb
from PIL import ImageTk,Image

def open_file():
    read=filedialog.askopenfilenames(parent=root, title='Choose a file')
    try:
        for i in read:
            os.startfile(i)
    except:
        mb.showinfo('confirmation', "File not found!")

root = Tk()
root.title('')
root.eval('tk::PlaceWindow . center')
Label(root, text="EZLyf", font=("Helvetica", 16), fg="blue").pack()

Button(root, text = "Open a File", command = open_file).pack()
root.mainloop()
exit()
