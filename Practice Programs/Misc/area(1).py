.import math

def area(a,b=None,c=None):
    if c is None:
        if b is None:
            print("Area of circle is",math.pi*(a**2))
        else:
            print("Area of rectangle is",a*b)
    else:
        s=(a+b+c)/2
        print("Area of triangle is",(s*(s-a)*(s-b)*(s-c))**1/2)

while True:
    input()
    print("\n"*40)
    a=int(input("1.Area of Circle\n2.Area of rectangle\n3.Area of triangle\n\n"))
    if a==1:
        area(float(input("radius:")))
    elif a==2:
        area(float(input("length:")),float(input("breadth:")))    
    elif a==3:
        area(float(input("side 1:")),float(input("side 2:")),float(input("side 3:")))
    else:
        pass
