def primefactors(n):
    d={}

    while n%2==0:
        if 2 in d:
            d[2] += 1
        else:
            d[2] = 1
        n/=2

    for i in range(3, int(n**.5)+1, 2):
        while n%i==0:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            n/=i
    for i in d:
        print(i,d[i])

    if n>2:
        print(n)
