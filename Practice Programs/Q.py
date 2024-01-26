p={}
while True:
    try:
        input()
        a=input("\n"*40+"1. Add Product\n2. Modify Product\n3. Delete Product\n")
        if a=="1":
            b=input("New ProdID")        
            if b not in p:
                p[b]=input("ProdName"),int(input("Price"))
        elif a=="2":
            b=input("Existing ProdID")
            if b in p:
                p[b]=input("ProdName"),int(input("Price"))
        elif a=="3":
            p.pop(input("Unwanted ProdID"))
        print(p)
    except:
        pass
