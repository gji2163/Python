def sum(N):
    if N>0:
        return(N+sum(N-1))
    return(0)
y=sum(int(input()))
