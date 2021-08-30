"""
Name: Max Oliver
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_rec_area():
    length = eval (input("Enter the length: "))
    width = eval (input("Enter the width: "))
    area = length * width
    print("Area =", area)

def calc_volume():
    length = eval (input("Enter the length:"))
    width = eval (input("Enter the width"))
    height = eval (input("Enter the height"))
    volume = length * width * height
    print("Volume =", volume)

def shooting_percentage():
    shotsMade = eval (input("Enter the number of shots made"))
    totalShots = eval (input("Enter the number of shots attempted"))
    shootingPercentage = (shotsMade / totalShots) * 100
    print("Shooting Percentage =", shootingPercentage,"%")

def coffee():
    pounds = eval (input("Enter the pounds of coffee ordered"))
    cost = (10.50 * pounds) + (.86 * pounds) + 1.50
    print("Cost =", "$", cost)

def kilometers_to_miles():
    kilometers = eval (input("Enter the distance traveled in kilometers"))
    miles = kilometers * 0.621
    print("Conversion =", miles, "miles")