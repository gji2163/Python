from tkinter import *

exp = ""

op={
    '+':'plus',
    '-':'minus',
    '*':'mult',
    '/':'div',
    '.':'dec'}

def press(num): 
	global exp 
	exp+=str(num) 
	equation.set(exp) 

for i in op:
    try:
        exec("def "+op[i]+"(event):\n\tpress('"+i+"')")
    except:
        pass

def equalpress(event=None):
    global exp
    try:  
        total = '='+str(eval(exp)) 
        equation.set(total)
    except: 
        equation.set(" error ")
    exp=''

def clear(event=None): 
    global exp 
    exp = "" 
    equation.set(exp)

def backsp(event=None):
    global exp
    exp=exp[:len(exp)-1]
    equation.set(exp)

def per(event=None):
    global exp
    try:
        total=str(eval(exp)/100)
        equation.set(total)
    except:
        equation.set(" error ")
    exp=''

for i in range(0,10):
    exec("def k"+str(i)+"(event):\n\tpress("+str(i)+")")

m = Tk() 
m.configure(background="black") 
m.title("Calculator")
m.resizable(0,0)

equation = StringVar() 

exp_field = Label(m, textvariable=equation,height=2,width=28,font=('Helvetica',16,'bold'),bg='black',fg='white') 
exp_field.grid(columnspan=4, ipadx=70,sticky='e')

for i in range(1,10):
    exec("button"+str(i)+"= Button(m, text="+str(i)+", fg='white', bg='black',relief='flat',command=lambda: press("+str(i)+"), height=1, width=7,font=('Helvetica',16,'bold'))\nbutton"+str(i)+".grid(row=(5+"+str(i)+")//3, column=(2+"+str(i)+")%3)")

button0 = Button(m, text=' 0 ', fg='white', bg='black', relief='flat',command=lambda: press(0), height=1, width=7,font=('Helvetica',16,'bold')) 
button0.grid(row=5, column=1) 

pl = Button(m, text=' + ', fg='orange', bg='black', relief='flat',command=lambda: press("+"), height=1, width=7,font=('Helvetica',16,'bold')) 
pl.grid(row=1, column=3) 

min = Button(m, text=' - ', fg='orange', bg='black', relief='flat',command=lambda: press("-"), height=1, width=7,font=('Helvetica',16,'bold'))
min.grid(row=2, column=3) 

multi = Button(m, text=' * ', fg='orange', bg='black', relief='flat',command=lambda: press("*"), height=1, width=7,font=('Helvetica',16,'bold'))
multi.grid(row=3, column=3) 

divide = Button(m, text=' / ', fg='orange', bg='black', relief='flat',command=lambda: press("/"), height=1, width=7,font=('Helvetica',16,'bold')) 
divide.grid(row=4, column=3) 

equal = Button(m, text=' = ', fg='white', bg='orange', relief='flat',command=equalpress, height=1, width=7,font=('Helvetica',16,'bold'))
equal.grid(row=5, column=3)

c = Button(m, text='C', fg='orange', bg='black', relief='flat',command=clear, height=1, width=7,font=('Helvetica',16,'bold'))
c.grid(row=1, column=0)

back = Button(m, text='←', fg='orange', bg='black', relief='flat',command=backsp, height=1, width=7,font=('Helvetica',16,'bold'))
back.grid(row=1, column=1) 

Decimal= Button(m, text='.', fg='orange', bg='black', relief='flat',command=lambda: press('.'), height=1, width=7,font=('Helvetica',16,'bold')) 
Decimal.grid(row=5, column=2)

perc=Button(m, text='%', fg='orange', bg='black', relief='flat',command=per, height=1, width=7,font=('Helvetica',16,'bold')) 
perc.grid(row=1,column=2)

for i in range(0,10):
    exec("m.bind('"+str(i)+"',k"+str(i)+")")

m.bind('c',clear)
m.bind('=',equalpress)
m.bind('<Return>',equalpress)
m.bind('<plus>',plus)
m.bind('-',minus)
m.bind('<asterisk>',mult)
m.bind('/',div)
m.bind('.',dec)
m.bind('<BackSpace>',backsp)
m.bind('<percent>',per)
