#Charlie Goodrich
#09/20/17
#name.py - prints out user's name

from ggame import *

name = input("Enter your name: ")
color_code = input("Enter a hex code for a color (Enter '0x' then the color code): ")
black = Color(0x000000, 1)
color = Color(color_code, 1)

blackOutline = LineStyle(1, black)

background = RectangleAsset(1000, 1000, blackOutline, color)
text = TextAsset(name, fill = color, style = "bold 48pt Times")


Sprite(background)
Sprite(text, (100, 100))
App().run()