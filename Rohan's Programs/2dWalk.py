import random
from graphics import *  
import time  

def main():
    win=GraphWin("2dWalk", 750, 750)
    win.setCoords(-50,-50,50,50)
    x1,y1,x2,y2=0,0,0,0
    for i in range (1000):
        dir=random.randint(0,3)
        if dir==0:
            y2+=1 # up
        elif dir==1:
            x2+=1 # right
        elif dir==2:
            y2-=1 # down
        else:
            x2-=1 # left
        l=Line(Point(x1,y1),Point(x2,y2))
        l.setFill("red")
        l.draw(win)
        time.sleep(0.03)
        l.undraw()
        l.setFill("black")
        l.draw(win)
        x1=x2
        y1=y2
    l.undraw()
    l.setFill("blue")
    l.draw(win)
    win.getMouse()
main()