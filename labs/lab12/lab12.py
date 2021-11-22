"""
Name: max Oliver
lab12.py
"""
from random import randint


def find_and_remove_first(list, value):
    try:
        i = list.index(value)
        list[i] = "Max Oliver"
    except:
        pass


def read_data(int):
    f = open(int, "r")
    data = f.read()
    data = data.split()
    return data


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if values[i] == search_val:
            return True
        i += 1
    return False


def good_input():
    x = eval(input("Enter a number in the range of 1 - 10:"))
    while x < 1 or x > 10:
        x = eval(input("The number is not in the range, please enter another number in the range of 1 - 10:"))
    return x


def num_digits():
    num = eval(input("enter a number:"))
    while num >= 1:
        digits = 0
        while num > 0:
            num = num // 10
            digits += 1
        print("There are", digits, "digits in the number")
        num = eval(input("Enter another number:"))


def hi_lo_game():
    secret = randint(1, 100)
    guess = 1
    num = eval(input("guess a number:"))
    while num != secret and guess < 7:
        guess +=1
        if num > secret:
            print("your guess is too high")
        else:
            print("your guess is too low")
        if num == secret:
            print("You win in", guess, "guesses!")
        else:
            print("Sorry, you lose. The number was:", secret)


def main():
    find_and_remove_first(list, value)
    read_data(int)
    is_in_linear(search_val, values)
    good_input()
    num_digits()
    hi_lo_game()
    pass


main()
