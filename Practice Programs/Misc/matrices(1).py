try:
    
    def add(x,y):
        
        r=[]
        
        for i in x:
            r+=[[]]
            for j in x[0]:
                r[-1]+=[0]
                
        for i in range(len(x)):
            for j in range(len(x[0])):
                r[i][j] = x[i][j] + y[i][j]

        for i in range(len(r)):
            for j in range(len(r[i])):
                print(r[i][j],end=" ")
            print()
            
    def multiply(x,y):

        r=[]

        for i in x:
            r+=[[]]
            for j in y[0]:
                r[-1]+=[0]

        for i in range(len(x)):
            for j in range(len(y[0])):
                for k in range(len(y)):
                   r[i][j] += x[i][k] * y[k][j]

        for i in range(len(r)):
            for j in range(len(r[i])):
                print(r[i][j],end=" ")
            print()

    while True:
        input()
        print("\n"*40)
        a=eval(input("Matrix 1:"))
        b=eval(input("Matrix 2:"))
        eval("matrix."+input("add or multiply: ")+"(a,b)")

except:
    pass
