def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fib(n-1) + fib(n-2)

def FIB(n):
    a,b = 0,1
    print('0',end=' ')
    for i in range(n-1):
        print(b,end = ' ')
        a,b = b,a+b
