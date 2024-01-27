a=eval(input())
b=a[0][1]
for i in range(len(a)-1):
    a[i][1]=a[i+1][1]
a[-1][1]=b
print(a)
