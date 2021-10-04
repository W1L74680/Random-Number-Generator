import random
import os
import time

#create a function that clear the. console
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#print the random number
def randomNumber(x, y):
    while True:
        #the time can be changed
        time.sleep(1)
        print(random.randint(x, y))
        time.sleep(1)
        clear()

#call the function with the numbers
randomNumber(1, 10)