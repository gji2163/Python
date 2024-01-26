from tkinter import *
from PIL import Image,ImageTk
import tkinter.scrolledtext as st

def main():
    def wux_on_enter(event):
        bg['image'] = img1_hover        

    def wux_on_leave(event):
        bg['image'] = img1

    def cont_on_enter(event):
        b['image'] = img2_hover

    def cont_on_leave(event):
        b['image'] = img2
            
    def start():
        m.destroy()
        read()
    
    m = Tk()
    m['background'] = 'black'
    m.attributes('-fullscreen',True)

    img = ImageTk.PhotoImage(Image.open('ico.png'))

    logo = Label(m,image = img, borderwidth = 0, highlightthickness = 0)
    logo.pack()

    img1 = ImageTk.PhotoImage(Image.open('wux.png'))
    img1_hover = ImageTk.PhotoImage(Image.open('wux_hover.png'))

    bg = Label(m, image = img1, bg = 'black')
    bg.pack()

    bg.bind("<Enter>", wux_on_enter)
    bg.bind("<Leave>", wux_on_leave)    

    img2 = ImageTk.PhotoImage(Image.open('cont.png'))
    img2_hover = ImageTk.PhotoImage(Image.open('cont_hover.png'))

    b = Button(m, image = img2, command = start, borderwidth = 0, highlightthickness = 0)
    b.pack(side = BOTTOM)

    b.bind("<Enter>", cont_on_enter)
    b.bind("<Leave>", cont_on_leave)

    m.mainloop()

def read():
    
    m=Tk()
    m['background'] = 'black'
    m.attributes('-fullscreen',True)

    m.update()
    w=m.winfo_width()

    Chap = Frame(m)
    Chap.pack(side='top', pady = 10, padx = 10)
    
    l = Label(Chap, text='Chapter ', font = ('Arial',20))
    l.grid(row=0, column=0)
    
    e = Entry(Chap,font = ('Arial',20))
    e.grid(row=0, column=1)
    e.insert(0,'1')
    
    def chapter(val, event = None):
        L.delete(index1=0.0, index2='end')
        L.insert(INSERT, '\n'+open('0'*(4-len(val))+val+'.txt','r',encoding = 'utf-8').read())
        e.delete(0,'end')
        e.insert(0,val)

    b=Button(Chap,text='Enter',command= lambda: chapter(e.get()))
    b.grid(row=0, column=2)

    m.bind('<Return>', lambda event: chapter(e.get(), event))  

    L = st.ScrolledText(m, height = 34, font = ("Arial", 15))
    L.pack(fill = X)

    L.insert(INSERT, '\n'+open('0001.txt','r',encoding = 'utf-8').read())

    chap_ch = Frame(m)
    chap_ch.pack()

    b1 = Button(chap_ch, text = '<', command= lambda: chapter(str(int(e.get())-1)))
    b1.grid(row=0, column=0)

    b2 = Button(chap_ch, text = '>', command= lambda: chapter(str(int(e.get())+1)))
    b2.grid(row=0, column=1)

    m.bind('<Left>', lambda event: chapter(str(int(e.get())-1), event))
    m.bind('<Right>', lambda event: chapter(str(int(e.get())+1), event))
   
    m.mainloop()

main()
