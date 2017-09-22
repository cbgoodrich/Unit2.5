#Charlie Goodrich
#09/22/17
#israel.py - prints the israeli flag

from ggame import *

blue = Color(0x0000FF, 1)
white = Color(0xFFFFFF, 1)
black = Color(0x000000, 1)

blackOutline = LineStyle(1, black)

whiteBackground = RectangleAsset(300, 200, blackOutline, white)
blueRect = RectangleAsset(300, 45, blackOutline, blue)
star = PolygonAsset([(150, 56.6987), (100, 143.3013), (200, 143.3013), (100, 56.6987), (200, 56.6987), (150, 143.3013)], blackOutline, blue)

Sprite(whiteBackground)
Sprite(blueRect)
Sprite(blueRect, (0, 155))
Sprite(star)

App().run()

