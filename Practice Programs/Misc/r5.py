def x(n):
    if n>0:
        return(n/(n+1)**2+x(n-1))
    return(0)
y=x(int(input()))
