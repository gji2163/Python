def add(x,i=0):
    if i<len(x):
        return(x[i]+add(x,i+1))
    return(0)
y=add(eval(input()))
