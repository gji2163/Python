import sys
i=0
while True:
    print(">>>",end=" ")
    try:
        exec(input())
    except Exception as Exception:
        i+=1
        template = "An Exception of type {"+str(i)+"} occurred. Arguments:\n{1!r}"
        message = template.format(type(Exception).__name__, Exception.args)
        sys.stdout.shell.write(message,"COMMENT")
