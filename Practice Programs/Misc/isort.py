a=eval(input())
for i in range(1, len(a)): 
    b = a[i] 
    j = i-1
    while j >=0 and b < a[j] : 
        a[j+1] = a[j] 
        j-=1
        a[j+1]=b 
    print(a)
