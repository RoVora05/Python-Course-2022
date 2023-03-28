from graphics import *
from random import *
from math import *

def main():
    sims=int(input("input number of simulations: "))
    n=int(input("input number of steps in each simulation: "))
    eList=[]
    for i in range(sims):
        win=GraphWin("_",500,500)
        win.setCoords(-100,-100,100,100)
        x1,x2,y1,y2=0,0,0,0
        for e in eList:
            p=e
            p.setFill("red")
            p.draw(win)
        for j in range(n):
            x2,y2=move(x1,y1)
            Line(Point(x1,y1),Point(x2,y2)).draw(win)
            x1,y1=x2,y2
        eList.append(Point(x2,y2))
        if i==sims-1:
            last=eList[-1]
            last.setFill("red")
            last.draw(win)
            win.getMouse()
        else: win.close()

def move(x,y):
    rad=radians(randint(0,360))
    x+=cos(rad)
    y+=sin(rad)
    return x,y

main()