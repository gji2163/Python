a=eval(input())
b=int(input())
c=f=p=0
n=len(a)
while c<=n-1:
    if a[c]==b:
        p=c+1
        f=1
        break
    else:
        c+=1
if f==1:
    print(b,"is in",a)
else:
    print(b,"is not in",a)
