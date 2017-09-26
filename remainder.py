#Charlie Goodrich
#09/26/17
#remainder.py - makes you guess the remainder and prints a face

from ggame import *
from random import randint

yellow = Color(0xFFFF00, 1)
black = Color(0x000000, 1)
white = Color(0xFFFFFF, 1)
yellowOutline = LineStyle(1, yellow)
blackOutline = LineStyle(1, black)

num1 = randint(25,50) #creating random numbers for the division
num2 = randint(1,5)
print("Number 1 =", num1)
print("Number 2 =", num2)
answer = num1%num2
guess = float(input("Whats the remainder to number 1 divided by number 2? "))

if answer == guess:
    face = CircleAsset(100, blackOutline, yellow)
    eye = CircleAsset(25, blackOutline, white)
    Sprite(face, (100, 100))
    Sprite(eye, (15, 15))
    App().run()
    
