"""
Name: Max Oliver
Partner: <your partner's name goes here – first and last>
lab7.py
"""
import math


def cash_conversion():
    i = eval(input("Enter any integer"))
    print('${:.2f}' .format(i))


def encode():
    acc = ""
    message = input("Enter a message:")
    key = eval(input("Enter a number for the key:"))
    for c in message:
        i = ord(c)
        newchar = chr(key + i)
        acc = acc + newchar
    print(acc)


def sphere_area(radius):
    area = (4 * math.pi * radius) ** 2
    return area


def sphere_volume(radius):
    volume = ((4 / 3) * math.pi * radius) ** 3
    return volume


def sum_n(n):
    acc = 0
    for i in range(n):
        acc = acc + i
    return acc


def sum_n_cubes(n):
    acc = 0
    for i in range(n):
        acc = acc + i ** 3
    return acc


def encode_better():
    acc = ""
    message = input("Enter a message:")
    k = input("Enter a word for the key:")
    for i in range(len(message)):
        c = ord(message[i])
        key = ord(k[i])
        result = c + key - 97
        acc = acc + chr(result)
    print(acc)


def main():
    cash_conversion()
    encode()
    print(sphere_area(3))
    print(sphere_volume(3))
    print(sum_n(3))
    print(sum_n_cubes(4))
    encode_better()
    pass


main()
