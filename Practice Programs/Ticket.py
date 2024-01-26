from playsound import playsound as p
from random import choice,randint
from tkinter import *
from mysql import connector as c

conn=c.connect(host="localhost",auth_plugin="mysql_native_password", user="root",password="Giks@1602")
cur=conn.cursor()
try:
    cur.execute("create database tambola;")
except:
    pass
cur.execute("use tambola")
try:
    cur.execute("create table game (Name varchar(20))")
except:
    pass
conn.commit()

xx=None
m=Tk()
m.geometry('405x100+400+300')
m['bg']='orange'

cond=1

n=Tk()
n.geometry('410x190+400+20')

ln=1
for i in range(9):
    for j in range(10):
        exec("l"+str(ln)+"=Label(n,text='"+str(ln)+"',width=5,relief='raised',bg='brown',fg='white')")   
        exec("l"+str(ln)+".grid(row="+str(i)+",column="+str(j)+")")
        ln+=1

def pos2():
    x=[[0 for j in range(3)] for i in range(3)]
    x[0][0]=randint(1,2)
    if x[0][0]==1:
        x[0][1],x[0][2],x[1][0],x[2][0]=2,2,2,2
    else:
        x[0][1]=randint(1,2)
        if x[0][1]==1:
            x[0][2],x[1][1],x[2][1]=2,2,2
        else:
            x[0][2],x[1][2],x[2][2]=1,2,2
    if x[1][0]==2:
        x[1][1]=randint(1,2)
        if x[1][1]==1:
            x[2][2],x[2][1],x[1][2]=1,2,2
        else:
            x[2][2],x[2][1],x[1][2]=2,1,1
    elif x[1][1]==2:
        x[1][0]=randint(1,2)
        if x[1][0]==1:
            x[1][2],x[2][0],x[2][2]=2,2,1
        else:
            x[1][2],x[2][0],x[2][2]=1,1,2
    else:
        x[1][0]=randint(1,2)
        if x[1][0]==1:
            x[2][0],x[1][1],x[2][1]=2,2,1
        else:
            x[2][0],x[1][1],x[2][1]=1,1,2
    return(x)

def pos3(x):
    y=[[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(x[i][j]):
                if y[i][j]==0:
                    y[i][j]=[randint(0,2)]
                else:
                    tt=[0,1,2]
                    tt.remove(y[i][j][0])
                    y[i][j]=tt
    for i in y:
        for j in i:
            j=j.sort()
    for i in y:
        for j in i:
            for k in j:
                k%=3
    return(y)

def sel(y):
    a=[[] for i in range(9)]
    x=[j for j in range(1,10)]
    p3=[0 for i in range(9)]
    for i in range(3):
        for j in range(3):
            for k in range(len(y[i][j])):
                p3[y[i][j][k]+i*3]+=1
    for i in range(p3[0]):
        y=choice(x)
        x.remove(y)
        a[0]+=[y]
    for i in range(1,8):
        x=[j for j in range(10*i,10*(i+1))]
        for j in range(p3[i]):
            y=choice(x)
            x.remove(y)
            a[i]+=[y]
    x=[j for j in range(80,91)]
    for i in range(p3[8]):
        y=choice(x)
        x.remove(y)
        a[8]+=[y]
    for i in a:
        i.sort()
    return(a)

def arr(x,y):
    z=[[[None for i in range(3)] for j in range(3)] for k in range(3)]
    m=[0 for i in range(9)]
    for i in range(3):
        for j in range(3):
            for k in range(len(y[i][j])):
                z[i][j][y[i][j][k]]=x[y[i][j][k]+i*3][m[y[i][j][k]+i*3]] #i is column number, j is row
                m[y[i][j][k]+i*3]+=1
    return(z)

cou=[]
drw=0
l=[i for i in range(1,91)]                          #Initial Numbers
lbl=Label(m,text="",width=5,bg='cyan')              #Declaring Label
lbl.grid(row=3,column=4)

ad=pos3(pos2())
asd=sel(ad)
arrr=arr(asd,ad)

de=1
for k in range(3):
    for i in range(len(arrr)):
        for j in range(3):
            if arrr[i][k][j]:
                exec("""
def c"""+str(de)+"""():
    if b"""+str(de)+"""['bg']=='yellow':
        b"""+str(de)+""".config(bg='green')
    else:
        b"""+str(de)+""".config(bg='yellow')""")
                exec("b"+str(de)+"=Button(m,text='"+str(arrr[i][k][j])+"',width=5,bg='yellow',command=c"+str(de)+")")
            else:
                exec("b"+str(de)+"=Button(m,text=' ',width=5,bg='yellow')")
            exec("b"+str(de)+".grid(row="+str(k)+",column="+str(3*i+j)+")")
            de+=1

row=[[] for i in range(3)]
col=[[] for i in range(3)]

for k in range(3):
    for i in arrr:
        for j in range(3):
            if i[k][j]:
                row[k]+=[i[k][j]]
                
for i in range(len(arrr)):
    for j in arrr[i]:
        for k in j:
            if k:
                col[i]+=[k]

##############################################################################################

def choose():
    global xx
    if drw:                       #Varying Condition
        xx=choice(l)               #Choosing a number
        l.remove(xx)
        try:
            if cond:
                exec("l"+str(xx)+".config(bg='black')")
        except Exception as e:
            print(e)
        if xx in [j for i in row for j in i]:
            cou.append(xx)
        try:
            lbl.config(text=xx)    #Displaying Number
        except:
            pass
        #p(str(xx)+".mp3")
        m.after(4000,choose)      #Enter time delay here
    
def draw(event):                  #Binding Space press
    global drw
    drw=(drw+1)%2
    choose()

def hide(event):
    global lbl
    try:
        if lbl:
            lbl.config(text="")
            lbl.destroy()
    except Exception as e:
        print(e)
        lbl=Label(m,text="",width=5,bg='cyan')              #Declaring Label
        lbl.grid(row=3,column=4)

m.bind("<space>", draw)           #Bind call
m.bind('<h>',hide)

o=Tk()
o.geometry('5x{0}+0+0'.format(o.winfo_screenheight()))

def E5():
    if len(cou)==5 and xx in cou:
        ob1['bg']='red'
        cur.execute("insert into game values('Early Five')")
        conn.commit()
    ob1['state']='disabled'

def Cor():
    ob2['state']='disabled'
    if xx not in cou:
        return
    for i in [row[0][0],row[0][4],row[2][0],row[2][4]]:
        if i not in cou:
            return
    ob2['bg']='red'
    cur.execute("insert into game values('Corners')") 
    conn.commit()
    
def row1():
    ob3['state']='disabled'
    if xx not in cou:
        return
    for i in row[0]:
        if i not in cou:
            return
    ob3['bg']='red'
    cur.execute("insert into game values('row 1')")
    conn.commit()
    
def row2():
    ob4['state']='disabled'
    if xx not in cou:
        return
    for i in row[1]:
        if i not in cou:
            return
    ob4['bg']='red'
    cur.execute("insert into game values('row 2')")
    conn.commit()
    
def row3():
    ob5['state']='disabled'
    if xx not in cou:
        return
    for i in row[2]:
        if i not in cou:
            return
    ob5['bg']='red'
    cur.execute("insert into game values('row 3')")
    conn.commit()
    
def col1():
    ob6['state']='disabled'
    if xx not in cou:
        return
    for i in col[0]:
        if i not in cou:
            return
    ob6['bg']='red'
    cur.execute("insert into game values('column 1')")
    conn.commit()

def col2():
    ob7['state']='disabled'
    if xx not in cou:
        return
    for i in col[1]:
        if i not in cou:
            return
    ob7['bg']='red'
    cur.execute("insert into game values('column 2')")
    conn.commit()
    
def col3():
    ob8['state']='disabled'
    if xx not in cou:
        return
    for i in col[2]:
        if i not in cou:
            return
    ob8['bg']='red'
    cur.execute("insert into game values('column 3')")
    conn.commit()
    
def BP():
    ob9['state']='disabled'
    f=[j for i in row for j in i]
    f.sort()
    print(f)
    if xx not in cou or f[0] not in cou or f[-1] not in cou:
        return
    ob9['bg']='red'
    cur.execute("insert into game values('BP')")
    conn.commit()
    
def mid():
    ob10['state']='disabled'
    if xx not in cou or row[1][2] not in cou:
        return
    ob10['bg']='red'
    cur.execute("insert into game values('mid')")    
    conn.commit()
    
def Ful():
    ob['state']='disabled'
    if xx not in cou:
        return
    for i in [j for i in row for j in i]:
        if i not in cou:
            return
    ob['bg']='red'
    cur.execute("insert into game values('Full House')")
    conn.commit()
    
ob1=Button(o,text="Early Five",command=E5,width=12,bg='black',fg='white')
ob2=Button(o,text="Corners",command=Cor,width=12,bg='black',fg='white')
ob3=Button(o,text="Row 1",command=row1,width=12,bg='black',fg='white')
ob4=Button(o,text="Row 2",command=row2,width=12,bg='black',fg='white')
ob5=Button(o,text="Row 3",command=row3,width=12,bg='black',fg='white')
ob6=Button(o,text="Column 1",command=col1,width=12,bg='black',fg='white')
ob7=Button(o,text="Column 2",command=col2,width=12,bg='black',fg='white')
ob8=Button(o,text="Column 3",command=col3,width=12,bg='black',fg='white')
ob9=Button(o,text="BP",command=BP,width=12,bg='black',fg='white')
ob10=Button(o,text="Middle Number",command=mid,width=12,bg='black',fg='white')
ob=Button(o,text="Full House",command=Ful,width=12,bg='black',fg='white')
ob.pack()
for i in range(1,11):
    exec("ob"+str(i)+".pack()")
