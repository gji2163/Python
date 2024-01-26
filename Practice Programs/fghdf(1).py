import time
input()
for j in range(100):
    for i in range(40):
        print("\n"*(35-i)+" "*j+"*"+"\n"*i)
    for i in range(40):
        print("\n"*i+" "*j+"*"+"\n"*(35-i))    
        
