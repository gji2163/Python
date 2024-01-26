while True:
    a=input()
    exec("import "+a)
    print(help(a))
