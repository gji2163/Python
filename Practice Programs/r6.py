def max(x,i=0):
    if i+1<len(x):
        if x[i]>x[i+1]:
            x[i],x[i+1]=x[i+1],x[i]
        max(x,i+1)
    return(x[-1])
y=max(eval(input()))
