from graphics import *
from random import *
import math

def sim(n):
    win=GraphWin("visual",750,750)
    win.setCoords(-1,-1,1,1)
    Circle(Point(0,0),1).draw(win)
    h=0
    for i in range(n):
        x=2*random()-1
        y=2*random()-1
        p=Point(x,y)
        if math.sqrt(x**2+y**2)<1:
            h+=1
            p.setFill("Red")
        else:
            p.setFill("Blue")
        p.draw(win)
    win.getMouse()
    return 4*h/n

print(sim(1000))