while True:
    a=eval(input())
    for i in range(len(a)):
        for j in range(1,len(a)-i):
            if a[j-1]>a[j]:
                a[j],a[j-1]=a[j-1],a[j]
    print("Sorted list",a)
    i=int(input())
    l = 0
    u = len(a)
    while l < u:
        x = l + (u - l) // 2
        v = a[x]
        if i == v:
            print(x)
            break
        elif i > v:
            if l == x:
                break
            l = x
        elif i < v:
            u = x
