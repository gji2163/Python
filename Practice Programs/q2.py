a=eval(input())
b=int(input())
c=[]
d={}
for i in a:
    c+=[i[b]]
    d[i[b]]=i
for i in range(len(c)):
    for j in range(len(c)-i-1):
        if c[j]>c[j+1]:
            c[j],c[j+1]=c[j+1],c[j]
a=[]
for i in c:
    a+=[d[i]]
for i in a:
    for j in i:
        print(j,end=" ")
    print()
