#Charlie Goodich
#09/20/17
#germany.py - displays the german flag

from ggame import *

black = Color(0x000000, 1)
red = Color(0xFF0000, 1)
yellow = Color(0xFFFF00, 1)

blackOutline = LineStyle(1, black)

blackRectangle = RectangleAsset(500, 100, blackOutline, black)
redRectangle = RectangleAsset(500, 100, blackOutline, red)
yellowRectangle = RectangleAsset(500, 300, blackOutline, yellow)

Sprite(yellowRectangle)
Sprite(blackRectangle)
Sprite(redRectangle, (0, 100))

App().run()
