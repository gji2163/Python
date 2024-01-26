from matplotlib import pyplot as p
import numpy as n

def graph(a,col="black"):
    p.plot([a[0],a[1]],[0,0],col)
    p.plot([0,0],[a[2],a[3]],col)
    p.plot([a[0]],[0],'black',marker="<")
    p.plot([a[1]],[0],'black',marker=">")
    p.plot([0],[a[2]],'black',marker="v")
    p.plot([0],[a[3]],'black',marker="^")

def trigo(f,start,end):
    x=n.linspace(start,end,(end-start)*10)
    exec("p.plot(x,n."+f+"(x))")

def display():
    p.show()

