from graphics import *
width = 400
height = 400

win=GraphWin("e",width,height)
win.setCoords(-12,-12,12,12)

color=["purple","blue","pink"]
for i in range (12,0,-1):
    Circle(Point(0,0),i).draw(win).setFill(color[i])

win.getMouse()
win.close()