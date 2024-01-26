import io

for i in range(200):
    a = str(i+1)
    
    with io.open('New Folder/'+'0'*(4-len(a))+a+'.txt', 'r') as f:
        try:
            g = open('0'*(4-len(a))+a+'.txt', 'w')
        
            x = f.read()
            x.replace('\n','\n\n')
            g.write(x)
            g.close()
            f.close()
        except Exception as e:
            print(repr(e))
            print(a)
