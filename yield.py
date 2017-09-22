#Charlie Goodrich
#09/22/17
#yield.py - displays a yield sign

from ggame import *

red = Color(0xFF0000, 1)
white = Color(0xFFFFFF, 1)
black = Color(0x000000, 1)
outline = LineStyle(1, black)

redTriangle = PolygonAsset([(50, 50), (150, 50), (100, 136.6025)], outline, red)
whiteTriangle = PolygonAsset([(70, 65), (130, 65), (100, 116.9615)], outline, white)

Sprite(redTriangle)
Sprite(whiteTriangle)

App().run()
