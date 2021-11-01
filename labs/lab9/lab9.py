"""
Name: Max Oliver
lab9.py
"""
from graphics import *
import math


def addTens(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sumList(sums):
    acc = 0
    for i in range(len(nums)):
        acc += nums[i]
    return acc


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])


def writeSumOfSquares():
    infile = input("Enter the name of the input file:")
    outfile = input("Enter the name of the output file:")
    readfile = open(infile, "r")
    writefile = open(outfile, "w")
    for line in readfile:
        nums = line.split()
        toNumbers(nums)
        squareEach(nums)
        summation = sumList(nums)
        writefile.write("Sum of squares =" + str(summation))


def starter():
    weight = eval(input("Enter the weight:"))
    numWins = eval(input("Enter the number of wins:"))
    if 160 > weight >= 150 and numWins >= 5:
        print("is a starter")
    elif weight > 199 and numWins > 20:
        print("is a starter")
    else:
        print("is not a starter")


def leapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year, " is a leap year")
    else:
        print(year, " is not a leap year")


def circleOverlap():
    win = GraphWin("Circle Stuff", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    r1 = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    c1 = Circle(p1, r1)
    c1.draw(win)
    p3 = win.getMouse()
    p4 = win.getMouse()
    r2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    c2 = Circle(p3, r2)
    c2.draw(win)
    overlap = Text(Point(200, 350), "The circles overlap")
    notOverlap = Text(Point(200, 350), "The circles do not overlap")
    distance = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)
    if distance <= r1 + r2:
        overlap.draw(win)
    else:
        notOverlap.draw(win)

    win.getMouse()
    win.close()


def main():
    addTens([5, 2, -3])
    squareEach()
    sumList()
    toNumbers()
    writeSumOfSquares()
    starter()
    leapYear(2100)
    circleOverlap()
    pass


main()
