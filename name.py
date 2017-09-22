#Charlie Goodrich
#09/20/17
#name.py - prints out user's name

from ggame import *

name = input("Enter your name: ")
color = input("Enter a hex code for a color (Enter '0x' then the color code): ")

color = Color(color, 1)

text = TextAsset(name, fill = color, style = "bold 48pt Times")

Sprite(text, (100, 100))
App().run()