from time import time as t
from datetime import datetime as d
tim=0
def start():
    global tim
    tim=t()
def pause():
    pass
def end():
    return("Time Elapsed",t()-tim)
print(t())
print(str(d.now()))
