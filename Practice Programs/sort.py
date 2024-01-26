a=eval(input())
for i in range(len(a)-1):
    b=0
    for j in range(1,len(a)-i):
        if a[j]<a[j-1]:
            a[j-1],a[j]=a[j],a[j-1]
            b=1
    if b==0:
        break
    print(a)
