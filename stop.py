#Charlie Goodrich
#09/27/17
#stop.py - makes a stop sign

from ggame import *
from math import sqrt

red = Color(0xFF0000, 1)
white = Color(0xFFFFFF, 1)

redOutline = LineStyle(1, red)

stopSign = PolygonAsset([(100, 0), (200, 0), (300, 100), (300, 200), (200, 300), (100, 300), (0, 200), (0, 100)], redOutline, red)
text = TextAsset("STOP", fill = white, style = "50pt Times")


Sprite(stopSign)
Sprite(text, (72.5, 122.5))
App().run()
