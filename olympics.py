#Charlie Goodrich
#09/22/17
#olympics. py - displays the olympic rings

from ggame import *

blue = Color(0x0000FF, 1)
red = Color(0xFF0000, 1)
white = Color(0xFFFFFF, 1)
black = Color(0x000000, 1)
yellow = Color(0xFFFF00, 1)
green = Color(0x008000, 1)

blueOutline = LineStyle(1, blue)
redOutline = LineStyle(1, red)
blackOutline = LineStyle(1, black)
yellowOutline = LineStyle(1, yellow)
greenOutline = LineStyle(1, green)

blueRing = CircleAsset(75, blueOutline, white)
redRing = CircleAsset(75, redOutline, white)
blackRing = CircleAsset(75, blackOutline, white)
yellowRing = CircleAsset(75, yellowOutline, white)
greenRing = CircleAsset(75, greenOutline, white)

Sprite(blueRing, (100, 100))
Sprite(blackRing, (260, 100))
Sprite(redRing, (420, 100))
Sprite(yellowRing, (180, 175))
Sprite(greenRing, (340, 175))
App().run()