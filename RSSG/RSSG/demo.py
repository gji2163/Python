from tkinter import *
from PIL import Image,ImageTk

def main():
    def on_enter(event, var):
        if var:
            b['image'] = img2_hover
        else:
            bg['image'] = img1_hover

    def on_leave(event,var):
        if var:
            b['image'] = img2
        else:
            bg['image'] = img1
    def start():
        m.destroy()
        read()
    
    m = Tk()
    m['background'] = 'black'
    m.attributes('-fullscreen',True)

    img = ImageTk.PhotoImage(Image.open('icon.png'))

    logo = Label(m, image = img, bg = 'black')
    logo.pack()

    img1 = ImageTk.PhotoImage(Image.open('wux.png'))
    img1_hover = ImageTk.PhotoImage(Image.open('wux_hover.png'))

    bg = Label(m, image = img1, bg = 'black')
    bg.pack()

    bg.bind("<Enter>", lambda event: on_enter(event, False))
    bg.bind("<Leave>", lambda event: on_leave(event, False))

    img2 = ImageTk.PhotoImage(Image.open('cont.png'))
    img2_hover = ImageTk.PhotoImage(Image.open('cont_hover.png'))

    b = Button(m, image = img2, command = start, bg = 'black', relief = 'flat')
    b.pack(side = BOTTOM)

    b.bind("<Enter>", lambda event: on_enter(event, True))
    b.bind("<Leave>", lambda event: on_enter(event, True))

    m.mainloop()

def read():
    
    m=Tk()
    m['background'] = 'black'
    m.attributes('-fullscreen',True)

    img = ImageTk.PhotoImage(Image.open('ico.png'))

    logo = Label(m,image = img, borderwidth = 0, highlightthickness = 0)
    logo.place(x=0,y=0)

    m.mainloop()

main()
