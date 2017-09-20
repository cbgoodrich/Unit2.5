#Charlie Goodrich
#09/20/17
#house.py - makes a house

from ggame import *

white = Color(0xFFFFFF, 1)
brown = Color(0xD2691E, 1)
black = Color(0x000000, 1)

blackOutline = LineStyle(1.75, black)

whiteHouse = RectangleAsset(400, 200, blackOutline, white)
brownRoof = PolygonAsset([(0, 50), (200, 0), (400, 50)], blackOutline, brown)
window = RectangleAsset(25, 25, blackOutline, white)


Sprite(whiteHouse, (0, 50))
Sprite(brownRoof)
Sprite(window, (25, 75))
Sprite(window, (125, 75))
Sprite(window, (250, 75))
Sprite(window, (350, 75))
App().run()
