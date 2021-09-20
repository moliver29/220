"""
Name: Max Oliver
lab4.py
"""

from graphics import *
import math

def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move rectangle")
    instructions.draw(win)

    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        user_click = win.getMouse()
        # builds a rectangle
        shape = Rectangle(Point(user_click.x - 10, user_click.y - 10), Point(user_click.x + 10, user_click.y + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    quit_pt = Point(width / 2, 10)
    quit = Text(quit_pt, "Click again to quit")
    quit.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """


    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    p1 = win.getMouse()
    p2 = win.getMouse()
    rect = Rectangle(p1, p2)
    rect.setFill("blue")
    rect.draw(win)

    leng = abs(p1.getX() - p2.getX())
    wid = abs(p1.getY() - p2.getY())

    area = leng * wid
    perimeter = 2 * (leng + wid)
    txta = Text(Point(50, 50), "The area is:" + str(area))
    txtp = Text(Point(55, 70), "The perimeter is:" + str(perimeter))
    txta.draw(win)
    txtp.draw(win)

    quit_pt = Point(width / 2, 10)
    quit = Text(quit_pt, "Click again to quit")
    quit.draw(win)
    win.getMouse()
    win.close()


def circle():
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    p1 = win.getMouse()
    p2 = win.getMouse()
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    r = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    circle = Circle(p1, r)
    circle.draw(win)
    txtr = Text(Point(100, 50), "The radius is:" + str(r))
    txtr.draw(win)

    quit_pt = Point(width / 2, 10)
    quit = Text(quit_pt, "Click again to quit")
    quit.draw(win)
    win.getMouse()
    win.close()


def pi2():
    n = eval(input("enter the number of terms to sum:"))
    acc = 0
    for i in range(n):
        num = 4
        denom = 1 + 2*i
        frac = (num/denom) * ((-1)**i)
        acc = acc + frac
    print(acc)
    print(math.pi - acc)


def main():
    # squares()
    # rectangle()
    # circle()
    pi2()


main()
