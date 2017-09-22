#Charlie Goodrich
#09/22/17
#israel.py - prints the israeli flag

from ggame import *

blue = Color(0x0000FF, 1)
white = Color(0xFFFFFF, 1)
black = Color(0x000000, 1)

blueOutline = LineStyle(1, blue)

whiteBackground = RectangleAsset(300, 200, blueOutline, white)
blueRect = RectangleAsset(300, 45, blueOutline, blue)
star1 = PolygonAsset([(150, 56.6987),  (100, 143.3013),  (200, 143.3013)], blueOutline, blue)
star2 = PolygonAsset([(100, 66.6987), (150, 153.3013), (200, 66.6987)], blueOutline, blue)
Sprite(whiteBackground)
Sprite(blueRect)
Sprite(blueRect, (0, 155))
Sprite(star1)
Sprite(star2)

App().run()

