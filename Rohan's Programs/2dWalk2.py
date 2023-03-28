from graphics import *
import random
from math import *

def main():
    win=GraphWin("2dWalk", 750, 750)
    win.setCoords(-50,-50,50,50)
    x1,y1,x2,y2=0,0,0,0
    for i in range (1000):
        x2,y2=takeStep(x1,y1)
        l=Line(Point(x1,y1),Point(x2,y2))
        l.setFill("red")
        l.draw(win)
        l.undraw()
        l.setFill("black")
        l.draw(win)
        x1=x2
        y1=y2
    l.undraw()
    l.setFill("blue")
    l.draw(win)
    win.getMouse()
    print(sqrt((x2**2)+(y2**2)))

def takeStep(x,y):
    rad=radians(random.randint(0,360))
    x+=cos(rad)
    y+=sin(rad)
    return x,y

main()