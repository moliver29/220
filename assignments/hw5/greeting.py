"""
Name: Max Oliver
greeting.py

Problem: display a valentines card that shows a heart with an arrow going through it.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import GraphWin, Circle, Polygon, Line, Point, Text, time


def main():
    # create window
    win = GraphWin("Greeting Card", 600, 600)

    # create the heart
    cp1 = Point(260, 200)
    circle1 = Circle(cp1, 50)
    circle1.setFill('red')
    circle1.draw(win)
    circle1.setOutline('red')
    cp2 = Point(340, 200)
    circle2 = Circle(cp2, 50)
    circle2.setFill('red')
    circle2.setOutline('red')
    circle2.draw(win)
    tp1 = Point(300, 370)
    tp2 = Point(210, 210)
    tp3 = Point(390, 210)
    triangle = Polygon(tp1, tp2, tp3)
    triangle.setFill('red')
    triangle.setOutline('red')
    triangle.draw(win)

    # display message
    msg_pt = Point(300, 500)
    message = Text(msg_pt, "Happy Valentine's Day!")
    message.draw(win)

    # create arrow
    arrow_line = Line(Point(50, 500), Point(150, 400))
    arrow_line.draw(win)
    ap1 = Point(160, 390)
    ap2 = Point(140, 400)
    ap3 = Point(156, 412)
    arrow_point = Polygon(ap1, ap2, ap3)
    arrow_point.setFill('black')
    arrow_point.draw(win)

    for _ in range(200):
        arrow_line.move(2, -2)
        arrow_point.move(2, -2)
        time.sleep(.02)

    # click to close window
    close_pt = Point(300, 10)
    close = Text(close_pt, "Click anywhere to close")
    close.draw(win)
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
