def str(x,i=-1):
    if i+len(x)>-1:
        return(x[i]+str(x,i-1))
    return("")
print(str(input()))
