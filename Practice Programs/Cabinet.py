a=["Ekta","Pragati","Shakti","Shanti"]
c=[[],[],[],[]]

Pragati={}
Ekta={}
Shakti={}
Shanti={}

def z():
    input()
    print("\n"*40)

z()

for i in range(len(a)):
    b=0
    print(a[i],"House:")
    while True:
        b+=1
        d=input(str(b)+". ")
        if d=="":
            print()
            break
        else:
            c[i]+=d

z()

i=input("Enter Name of House")
while True:
    for j in range(len(c[a.index(i)])):
        print(str(j+1)+".",c[a.index(i)][j])
        eval(i)[c[a.index(i)][int(input())-1]]=1
        
    
