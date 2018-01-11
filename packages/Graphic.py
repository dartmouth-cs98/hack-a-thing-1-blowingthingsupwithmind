import packages.graphics as graphics
import time, os, sys

def render(array):
        win = graphics.GraphWin("My Circle", 300, 300)
        win.setBackground("grey")

        radius = 50

        rPoint1 = graphics.Point(100,100)
        rPoint2 = graphics.Point(200,200)

        r = graphics.Rectangle(rPoint1, rPoint2)

        aPoint1 = graphics.Point(0,0)
        aPoint2 = graphics.Point(100,100)
        bPoint1 = graphics.Point(0,300)
        bPoint2 = graphics.Point(100,200)
        cPoint1 = graphics.Point(300,0)
        cPoint2 = graphics.Point(200,100)
        dPoint1 = graphics.Point(300,300)
        dPoint2 = graphics.Point(200,200)

        aLine = graphics.Line(aPoint1, aPoint2)
        bLine = graphics.Line(bPoint1, bPoint2)
        cLine = graphics.Line(cPoint1, cPoint2)
        dLine = graphics.Line(dPoint1, dPoint2)

        aLine.draw(win)
        bLine.draw(win)
        cLine.draw(win)
        dLine.draw(win)

        r.draw(win)

        c = graphics.Circle(graphics.Point(150,150), radius)
        c.setFill("green")
        c.draw(win)

        t = 0
        while t < 60 :
            sys.stdout.write("Dropping back")
            radius = array.pop(0)
            sys.stdout.write("New Radius is " + str(radius))
            c.undraw()
            c = graphics.Circle(graphics.Point(150,150), radius)
            c.setFill("green")
            c.draw(win)
            time.sleep(0.25)
            t = t+1
        win.close()
