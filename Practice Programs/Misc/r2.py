def fac(x):
    if x>0:
        return(fac(x-1)*x)
    return(1)
y=fac(int(input()))
