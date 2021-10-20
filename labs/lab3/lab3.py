"""
Name: Max Oliver
lab3.py
"""

def average():
    x = eval(input("Enter the number of homework assignments:"))
    acc = 0
    for i in range(x):
        grade = eval(input("Enter your grade on HW" + str(i+1) + ":"))
        acc = acc + grade
    print(acc / x, "%")


def tip_jar():
    acc = 0
    for i in range(5):
        tip = eval(input("Enter the amount of your tip:"))
        acc = acc + tip
    print("$", acc)


def newton():
    x = eval(input("what is x?:"))
    n = eval(input("how many times should the approximation be improved?:"))
    approx = x/2
    for i in range(n):
        approx = (approx + (x/approx)) / 2
    print(approx)


def sequence():
    n = eval(input("Enter the number of terms:"))
    for i in range(1, n+1):
        seq = 1 + (i // 2 * 2)
        print(seq, end=" ")


def pi():
    n = eval(input("Enter the number of terms in the series"))
    acc = 1
    for i in range(n):
        numerator = 2 + (i // 2 * 2)
        denominator = 1 + ((i+1) // 2 * 2)
        acc = acc * (numerator/denominator)
    print(acc)
