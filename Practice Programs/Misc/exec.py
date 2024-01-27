while True:
    try:
        inp=input()
        exec("""inp""")
    except:
        if inp[-1]==":":
            while True:
                try:
                    i=input()
                    inp+="\n    "+i
                    exec("""inp""")
                    break
                except:
                    if i=="":
                        print(inp)
                        exec("""inp""")
