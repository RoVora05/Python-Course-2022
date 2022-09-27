from graphics import *

win=GraphWin()

p1=Point(100,72)
p2=Point(76, 90)
p3=Point(124, 90)
p4=Point(85, 120)
p5=Point(115, 120)

l1=Line(p5,p1)
l2=Line(p1,p4)
l3=Line(p4,p3)
l4=Line(p3,p2)
l5=Line(p2,p5)

l1.draw(win)
l2.draw(win)
l3.draw(win)
l4.draw(win)
l5.draw(win)

win.getMouse()
win.close()