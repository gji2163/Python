from tkinter import *
s=[]
b=c=m=""
f=open("read.txt","w")
import mysql.connector
def create_database():
    try:
        conn=mysql.connector.connect(host="127.0.0.1",auth_plugin="mysql_native_password", user="root",password="Giks@1602")
        cur=conn.cursor()
        cur.execute("create database cabinet_elections;");
        cur.execute("use cabinet_elections;")
        cur.execute("create table elections (Name varchar(20) primary key,Votes varchar(4));")
        conn.commit()
        conn.close();
    except Exception as e:
        pass
def append_database(x):
    try:
        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="Giks@1602", auth_plugin="mysql_native_password")
        cur=conn.cursor()
        cur.execute("use cabinet_elections")
        cur.execute("insert into elections values('{}',0);".format(x))
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
        pass
def l():
    global b
    global c
    global m
    y.destroy()
    create_database() # first database should be created
    m=Tk()
    m.geometry("500x500")
    a=Label	(m,text="Canidate")
    a.grid(row=0,column=0)
    b=Entry(m)
    b.grid(row=0,column=1)
    c=Button(m,text="Submit",command=x)
    c.grid(row=0,column=2)
def x():
    global s
    if b.get()=="":
        m.destroy()
        f.writelines(s)
        f.close()
        return()
    else:
        append_database(b.get())
        s+=[b.get()+"\n"]
    b.delete(0, END)
y=Tk()
y.geometry("800x500")
a=Label(y)
a.config(text="TIS CABINET ELECTION MANAGEMENT SYSTEM",bg="white",fg="red",font=("courier",20),relief="raised")
a.pack(fill="both",expand=True)
c=Button(y,text="Start Election",command=l)
c.pack(fill="x",expand=True)
