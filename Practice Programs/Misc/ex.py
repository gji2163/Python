import sys
i=0
while True:
    sys.stdout.shell.write(">>> ","console")
    try:
        exec(input())
    except Exception:
        template = "Traceback (most recent call last):\n  File <pyshell#"+str(i)+">, line 1, in <module>\n   "+Exception.args[0].split()[1]+"\n{0}: {1!r}"
        message = template.format(type(Exception).__name__, Exception.args[0])
        sys.stdout.shell.write(message+"\n","COMMENT")
        i+=1
