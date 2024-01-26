def bs(a,b,c,d):
    if b>=c:
        return(-1)
    m=(b+c)//2
    if a[m]<d:
        return(bs(a,m+1,c,d))
    elif a[m]>d:
        return(bs(a,b,m,d))
    else:
        return(m)
x=eval(input())
y=bs(x,0,len(x),int(input()))
if y<0:
    print(False)
else:
    print(True)
