"""
Name: Max Oliver
Lab13.py
"""


def is_in_binary(lst, value):
    mid = lst[len(lst)//2]
    while mid != value and len(lst) != 1:
        if mid > value:
           lst = lst[:mid]
        else:
            lst = lst[mid + 1:]
        mid = lst[len(lst)//2]
    if len(lst) == 1 and lst[0] != value:
        return False
    else:
        return True


def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i+1, len(values)):
            if j < lowest:
                lowest = values[j]
                pos = j
        values[i], values[j] = values[j], values[i]


def rect_sort(rects):
    dict = {}
    areas = []
    for rect in rects:
        dict[calc_area(rect)] = rect
        areas.append(calc_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        rects[i] = dict[]


def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    dx = abs(p1.getX() - p2.getX())
    dy = abs(p1.getY() - p2.getY())
    return dx * dy


def star_find(filename):
    file = open(filename, "r")
    signals = file.read().split()
    found = []
    count = 0
    for i in signals:
        count = count + 1
        if 4000 <= int(i) <= 5000:
            found.append(i)
        if len(found) >= 5:
            break
    print(found)
    if len(found) < 5:
        print("We did not find 5 signals in the range")
    else:
        print(count)



def main():
    # is_in_binary()
   # selection_sort()
   # rect_sort()
   # calc_area()
    star_find(signals.txt)
    pass


main()
