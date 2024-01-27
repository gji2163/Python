def a(x,i=0):
    if i<len(x):
        return(x[i]+a(x,i+1))

    return(0)
y=a(eval(input()))
