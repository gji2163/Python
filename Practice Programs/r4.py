def add(x,i=-1):
    if i+len(x)>-1:
        return(x[i]+add(x,i-1))
    return("")
y=add(input())
