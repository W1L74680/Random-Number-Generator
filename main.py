import random
import os
import time

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def randomNumber(x, y):
    while True:
        print(random.randint(x, y))
        time.sleep(5)
        clear()
        time.sleep(5)

randomNumber(1, 10)
