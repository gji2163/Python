def bs(a,b,c):
    m=int(a+b/2)
    if c not in range(a,b+1):
        return(False)
    elif c==m:
        return(True)
    elif c>m:
        return(bs(m,b,c))
    elif c<m:
        return(bs(a,m,c))
    else:
        return(False)

y=bs(0,len(eval(input())),input())
