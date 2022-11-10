from graphics import *
def main():
    win=GraphWin("title",500,500)

    c1=Circle(Point(75,60),5)
    c2=Circle(Point(25,60),5)
    c3=Circle(Point(100,90),20)

    o1=Oval(Point(45,35),Point(155,120))

    o1.setFill("light blue")
    c1.setFill("black")
    c2.setFill("black")
    c3.setFill("pink")

    o1.draw(win)
    c1.draw(win)
    c2.draw(win)
    c3.draw(win)

    win.getMouse()
    win.close()
main()

def surprise_face(centerx,centery): # center x is 100, center y is 77.5
    o1=Oval(Point(centerx-55,centery-40.5),Point(centerx+55,centery+40.5))
surprise_face()