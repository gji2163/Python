import sys
import pypdftk

droppedFile = sys.argv[1]
print(droppedFile)
input()

try:
    pypdftk.fill_form(droppedFile, out_file=droppedFile, flatten=True)
except Exception as e:
    input(e)
