def prime(n):
    if n<2:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

def PRIME(n):
    for i in range(2,n+1):
        if prime(i):
            print(i)
