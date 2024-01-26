from tkinter import *
from tkinter import ttk
from mysql import connector as c

conn=c.connect(
        user='root',
        host='localhost',
        password='Giks@1602',
        )
cur=conn.cursor()
cur.execute("use cards")

d={
    '':('White','Black'),
    'Light Mode':('White','Black'),
    'Dark Mode':('Black','White')
    }

m=Tk()
m.attributes('-fullscreen', True)


Menu=Frame(m,bd=2,bg= 'green')
Menu.pack(fill= 'x')



B1=Label(Menu,bg= 'light green',bd=5,relief='flat',font=('BellMT',15),text='New Tab')
B1.pack(side= LEFT,fill= 'y')

B2=Label(Menu,relief= 'raised',font=('BellMT',15),text='+')
B2.pack(side= LEFT)

r=1;c=4

frame = Frame(m, bd=10, bg='SystemButtonFace')
frame.pack()

def on_field_change(index, value, op):
    m.config(bg=d[Mnu.get()][0])

m.update()

w=m.winfo_width()

n=StringVar()
Mnu=ttk.Combobox(m,font=('BellMT',15),textvariable=n,width = 10)
n.trace('w',on_field_change)
        
Mnu['values'] = (
    'Light Mode',
    'Dark Mode'
    )
Mnu.place(x=w-150,y=0)
Mnu.current(0)


def push(Entry):

    entry=[]
    
    for i in Entry:
        print(Entry)
        try:
            ent=i.get()
            if int(ent):
                entry.append(ent)
            else:
                raise ValueError
        except ValueError:
            entry.append("0")
    
    cur.execute("update game set Tarun= Tarun+{0}, Kirti= Kirti+{1}, Girik= Girik+{2}, Arav= Arav+{3} order by SNo DESC LIMIT 1;".format(entry[0],entry[1],entry[2],entry[3]))
    conn.commit()

    cur.execute("select * from game where SNo=max(SNo)")
    Score= cur.fetchone()

    l.config(text=Score)
    
    try:
        var=int(Te.get())
    except:
        var=100
    if not all(i < var for i in Score[1:]):
        cur.execute("insert into game values({},0,0,0,0)".format(Score[0]+1))
        conn.commit()
        l.config(text='New Game')
        
e=[]
clr=['red','cyan','green','yellow']

for j in range(4):
    exec("e{0}=Entry(frame, font= ('BellMT',15),bd=3,width=15,bg='{1}')".format(j+1,clr[j]))
    exec("e.append(e{})".format(j+1))
    exec("e{0}.grid(row=3,column={0})".format(j+1))
    
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(c+1, weight=1)

Mnu.tkraise()

Name=["Tarun","Kirti","Girik","Arav"]

for i in range(4):
    exec(Name[i]+"=Label(frame,bd=2,font=('BellMT',15),relief='raised',bg='"+clr[i]+"',width=15,text='"+Name[i]+"')")
    exec(Name[i]+".grid(row=2,column={})".format(i+1))

#void=Label(frame,font=('BellMT',15),text='',width=15)
#void.grid(row=1,column=1)

Tl=Label(frame,font=('BellMT',15),relief='raised',bg='light grey',text='Max Score',width=31)
Tl.grid(row=1,column=1,columnspan=2)

Te=Entry(frame, font= ('BellMT',15), width=31)
Te.grid(row=1,column=3,columnspan=2)

#void1=Label(frame,font=('BellMT',15),text='',width=15)
#void1.grid(row=1,column=4)

b=Button(frame,font=('BellMT',15),bd=5,text='Submit',activebackground='grey',command=lambda: push(e),width=30)
b.grid(row=4,column=2,columnspan=2)

l=Label(m,font= ('BellMT',15),bd=3,width=15)
l.pack()

m.mainloop()

