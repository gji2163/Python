from keyboard import add_hotkey
from time import sleep
from pyautogui import click

var = 0

def end():
    global var
    var = (var + 1) % 2

add_hotkey('space', end)

while True:
    if var:
        click()
    else:
        sleep(2)
