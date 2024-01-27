import sys
b={}

while True:

    sys.stdout.shell.write(">>> ","console")

    a=input()

    x=a.split()
    for i in x:
        if i[0]==i[-1]=="'" or i[0]==i[-1]=='"':
            i=i[1:len(i)-1]
        else:
            try:
                i=int(i)
            except:
                try:
                    i=float(i)
                except:
                    pass
    for i in range(len(x),0,-1):
        if x=="sqr":
             x[i+1]**=0.5
             x.remove(x[i])
        print(x)
    if x[0]=="var":
        y=x[2]
        if len(x)>3:
            x[2]=x[2:]
        if x[2][0]==x[2][-1]=="'" or x[2][0]==x[2][-1]=='"':
            x[2]=x[2][1:len(x[2])-1]
        else:
            try:
                x[2]=int(x[2])
            except:
                try:
                    x[2]=float(x[2])
                except:
                    print(x[2])
                    for i in range(len(x[2])):
                        if x[2][i] in b:
                            print(x[2][i])
                            x[2][i]=b[x[2][i]]
                    v=""
                    for i in x[2]:
                        v+=str(i)
                    x[2]=v
                    try:
                        f=eval(x[2])
                        b[x[1]]=eval(x[2])
                    except:
                        try:
                            var="Traceback (most recent call last):"+"\n    "+a+"\n"+"Name Error: name '"+x[2]+"' is not defined\n"
                        except:
                            var="Traceback (most recent call last):"+"\n    "+a+"\n"+"Name Error: name '"+y+"' is not defined\n"
                        sys.stdout.shell.write(var,"COMMENT")
        b[x[1]]=x[2]
    elif x[0]=="show":
        if x[1]=="var-val":
            for i in b:
                print(i,":",b[i])
        elif x[1]=="var":
            for i in b:
                print(i)
        elif x[1]=="val":
            for i in b:
                print(b[i])
    else:
        try:
            print(b[a])
            
        except:
            print(eval(a))
