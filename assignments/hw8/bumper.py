"""
Name: Max Oliver
bumper.py

Problem: will create a graphical simulation of a bumper car system.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import time
from random import randint
from graphics import Circle, Point, GraphWin, color_rgb


# function that will return a random integer number in the range [–move_amount, +move_amount]
def get_random(move_amount):
    return randint(-move_amount, move_amount)


# function that will return a boolean value based on the collision of the two balls
def did_collide(ball, ball2):
    ball_center = ball.getCenter()
    ball2_center = ball2.getCenter()
    ball_x = ball_center.getX()
    ball_y = ball_center.getY()
    ball2_x = ball2_center.getX()
    ball2_y = ball2_center.getY()
    ball_radius = ball.getRadius()
    ball2_radius = ball2.getRadius()
    distance = (((ball2_x - ball_x) ** 2) + ((ball2_y - ball_y) ** 2)) ** (1 / 2)
    radius = ball_radius + ball2_radius
    if distance <= radius:
        collision = True
    else:
        collision = False
    return collision


# function that returns a True value if ball hits a vertical wall, False if otherwise
def hit_vertical(ball, win):
    ball_center = ball.getCenter()
    ball_x = ball_center.getX()
    radius = ball.getRadius()
    width = win.getWidth()
    if ball_x <= radius or ball_x >= width - radius:
        hit = True
    else:
        hit = False
    return hit


# function that returns a True value if ball hits a horizontal wall, False if otherwise
def hit_horizontal(ball, win):
    ball_center = ball.getCenter()
    ball_y = ball_center.getY()
    radius = ball.getRadius()
    height = win.getHeight()
    if ball_y <= radius or ball_y >= height - radius:
        hit = True
    else:
        hit = False
    return hit


# function that will return a random color
def get_random_color(ball):
    r_color = randint(0, 255)
    g_color = randint(0, 255)
    b_color = randint(0, 255)
    ball.setFill(color_rgb(r_color, g_color, b_color))


def main():
    # create window
    win = GraphWin("Bumper", 600, 600)
    # create balls
    radius = 30
    ball1 = Circle(Point(100, 300), radius)
    ball2 = Circle(Point(500, 300), radius)
    get_random_color(ball1)
    get_random_color(ball2)
    ball1.draw(win)
    ball2.draw(win)
    # make balls move
    move_1x = get_random(15)
    move_1y = get_random(15)
    move_2x = get_random(15)
    move_2y = get_random(15)
    while ball1.move and ball2.move:
        time.sleep(.02)
        ball1.move(move_1x, move_1y)
        ball2.move(move_2x, move_2y)
        if did_collide(ball1, ball2):
            move_1x = -move_1x
            move_1y = -move_1y
            move_2x = -move_2x
            move_2y = -move_2y
        if hit_vertical(ball1, win):
            move_1x = -move_1x
        if hit_vertical(ball2, win):
            move_2x = -move_2x
        if hit_horizontal(ball1, win):
            move_1y = -move_1y
        if hit_horizontal(ball2, win):
            move_2y = -move_2y

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
