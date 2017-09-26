#Charlie Goodrich
#09/27/17
#warmup5.py - getting warm

from ggame import *

blue = Color(0x0000FF, 1)
yellow = Color(0xFFFF00, 1)
black = Color(0x000000, 1)

blackOutline = LineStyle(1, black)

yellowDiamond = PolygonAsset([(50, 25), (100, 75), (50, 125), (0, 75)], blackOutline, yellow)
blueName = TextAsset("Charlie", fill = blue, style = "12pt Times")

Sprite(yellowDiamond)
Sprite(blueName, (15, 70))

App().run()
