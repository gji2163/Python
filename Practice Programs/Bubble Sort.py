a=eval(input())
for i in range(0,len(a)):
    for j in range(1,len(a)-i):
        if a[j-1]>a[j]:
            a[j],a[j-1]=a[j-1],a[j]
    print(a)
