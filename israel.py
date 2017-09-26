#Charlie Goodrich
#09/22/17
#israel.py - prints the israeli flag

from ggame import *

blue = Color(0x0000FF, 1)
white = Color(0xFFFFFF, 0)
black = Color(0x000000, 1)

blueOutline = LineStyle(1, blue)

whiteBackground = RectangleAsset(300, 200, blueOutline, white)
blueRect = RectangleAsset(300, 45, blueOutline, blue)
star1 = PolygonAsset([(150, 60.0385),  (120, 111.9615),  (180, 111.9615)], blueOutline, white)
star2 = PolygonAsset([(120, 78.0385), (150, 129.9615), (180, 78.0385)], blueOutline, white)
Sprite(whiteBackground)
Sprite(blueRect)
Sprite(blueRect, (0, 155))
Sprite(star1)
Sprite(star2)

App().run()

