from graphics import *
def drawFace(centerX,centerY,size,win):

    c1=Circle(Point(centerX,centerY),4*size)
    e1=Circle(Point(centerX-(2*size),(centerY+(1.5*size))),3*size/4)
    e2=Circle(Point(centerX+(2*size),(centerY+(1.5*size))),3*size/4)
    m1=Circle(Point(centerX,centerY-size),size)

    c1.draw(win).setFill("light blue")
    e1.draw(win).setFill("black")
    e2.draw(win).setFill("black")
    m1.draw(win).setFill("pink")

def main():
    win=GraphWin("title",500,500)
    win.setCoords(0,0,100,100)
    x=eval(input("Input x coordinate (0-200): "))
    y=eval(input("Input y coordinate (0-200): "))
    size=eval(input("Input size: "))
    drawFace(x,y,size,win)

    win.getMouse()
    win.close()
main()