def fib(x,y=[1,1,1]):
    if x>0:
        x-=1
        print(y[1],end=" ")
        y[0]=y[2]
        y[2]+=y[1]
        y[1]=y[0]
        fib(x,y)
fib(int(input()))
