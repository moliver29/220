"""
Name: Max Oliver
lab2.py
"""
import math


def sum_of_threes():
    a = eval(input("Enter upper bound number"))
    acc = 0
    for x in range(0, a+1, 3):
        acc = acc + x
    print(acc)


def multiplication_table():
    for L in range(1, 11):
        for h in range(1, 11):
            print(L*h, end=" ")
        print()


def triangle_area():
    a = eval(input("enter length of side a"))
    b = eval(input("enter the length of side b"))
    c = eval(input("enter the length of side c"))
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(area)


def sumSquares():
    low = eval(input("enter the lower number of range"))
    up = eval(input("enter the upper number of range"))
    acc = 0
    for x in range(low, up+1, 1):
        acc = acc + x ** 2
    print(acc)


def power():
    base = eval(input("enter the base number"))
    exp = eval(input("enter the exponent"))
    acc = 1
    for x in range(exp):
        acc = acc * base
    print(base, "^", exp, "=", acc)
