#Charlie Goodrich
#09/20/17
#graphicsDemo.py - intro to ggame

from ggame import *

red = Color(0xFF0000, 1)
green = Color(0x00FF00, 1)
blue = Color(0x0000FF, 1)
black = Color(0x000000, 1)

blackOutline = LineStyle(1, black) #pixels, color

redRectangle = RectangleAsset(200, 100, blackOutline, red) #width, height, outline, fill

blueCircle = CircleAsset(50, blackOutline, blue) #radius, outline, fill

greenEllipse = EllipseAsset(100, 50, blackOutline, green) #horiztonal axis, vertical axis, outline, fill

blackLine = LineAsset(50, 160, blackOutline) #x-endpoint, y-endpoint, lineStyle

redTriangle = PolygonAsset([(0,0), (120, 180), (60, 300)], blackOutline, red)

Sprite(redRectangle)
Sprite(blueCircle, (50, 50))
Sprite(greenEllipse, (200, 400))
Sprite(blackLine)
Sprite(redTriangle)
App().run()
