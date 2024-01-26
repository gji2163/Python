dic={}
while True:
    while True:
        if input("Press only Enter to continue: ")!="":
            break
        print("\n"*40)
        dic[input("Country: ")]=["Capital",input("capital: ")],"Population",int(input("Pop: "))
    print("\n"*40,dic[input("Country: ")])
    while True:
        if input("Press only Enter to continue: ")!="":
            break
        print("\n"*40,dic[input("Country: ")])
