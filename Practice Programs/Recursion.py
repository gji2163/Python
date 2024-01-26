def sum(x):
    if x>0:
        return(x+sum(x-1))
    return(0)

def fac(x):
    if x>0:
        return(x*fac(x-1))
    return(1)

def fib(x,y=[1,1,1]):
    if x>0:
        x-=1
        print(y[1],end=" ")
        y[0]=y[2]
        y[2]+=y[1]
        y[1]=y[0]
        fib(x,y)
    return("")

def add(x,i=0):
    if i<len(x):
        return(x[i]+add(x,i+1))
    return(0)

def max(x,i=0):
    if i<len(x)-1:
        if x[i]>x[i+1]:
            x[i],x[i+1]=x[i+1],x[i]
        max(x,i+1)
    return(x[-1])

def q(n):
    if n>0:
        return((n/(n+1)**2)+q(n-1))
    return(0)

exec("print("+input("1.sum\n2.fac\n3.fib\n4.add\n5.max\n6.q\n")+"("+input()+"))")

