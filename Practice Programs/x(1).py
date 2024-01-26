import matrix
while True:
    input()
    print("\n"*40)
    a=eval(input("Matrix 1:"))
    try:
        b=eval(input("Matrix 2:"))
        eval("matrix."+input("add or multiply: ")+"(a,b)")
    except:
        for i in a:
            for j in range(len(i)):
                print(i[j],end=" ")
            print()
