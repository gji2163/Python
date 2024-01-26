f=open('Index.txt','r').readlines()

#for i in f[:500]:
 #   print('-'.join(''.join(e.lower() for e in i[14:] if e.isalpha() or e==' ').split(' ')))

#f=[i.split('-')[1].strip(' \n') for i in f[:10]]

for i in f:
    a=''
    for j in i.split('-')[1].strip(' \n'):
        if j==' ':
            a+='-'
        elif j.isalpha():
            a+=j.lower()
    print(a)

        
