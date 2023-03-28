from graphics import *

def main():
    cube1=cube(float(input("Size:\n")))
    x=float(input("x:\n"))
    y=float(input("y:\n"))
    cube2=cube(float(input("Size:\n")))
    x=float(input("x:\n"))
    y=float(input("y:\n"))
    win=GraphWin("cube",500,500)
    win.setCoords(-10,-10,10,10)
    cube1.generateCube1(x,y,win)
    cube2.generateCube1(x,y,win)
    win.getMouse()

class cube():
    def __init__(self,size):
        self.size=(size)

    def generateCube1(self,x,y,win):
        pL=[Point(0+x,-0.125*self.size+y),
            Point(0+x,-1.375*self.size+y),
            Point(1*self.size+x,0.375*self.size+y),
            Point(-1*self.size+x,0.375*self.size+y),
            Point(0+x,0.875*self.size+y),
            Point(1*self.size+x,-0.875*self.size+y),
            Point(-1*self.size+x,-0.875*self.size+y),]
            
        for i in [Line(pL[0],pL[1]),
        Line(pL[0],pL[2]),
        Line(pL[0],pL[3]),
        Line(pL[2],pL[4]),
        Line(pL[3],pL[4]),
        Line(pL[1],pL[5]),
        Line(pL[1],pL[6]),
        Line(pL[2],pL[5]),
        Line(pL[3],pL[6])]:
            i.draw(win)

if __name__=="__main__":
    main()