from os import system as s
from datetime import datetime as d

while True:
    print(str(d.now())[:-7])
    s("cls")
