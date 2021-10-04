"""
Name: Max Oliver
lab6.py
"""


def name_reverse():
    name = input('Enter a first and last name:')
    name_list = name.split(" ")
    print(name_list[1] + "," + name_list[0])


def company_name():
    domain = input('Enter a three part domain name:')
    domain_list = domain.split(".")
    print(domain_list[1])


def initials():
    n = eval(input('Enter the number of names that will be input:'))
    for i in range(n):
        first_name = input('Enter the first name of student ' + str(i+1) + ':')
        last_name = input("Enter " + str(first_name) + "'s last name:")
        initial = first_name[0] + last_name[0]
        print(str(first_name) + "'s initials are: " + initial.upper())


def names():
    people_names = input("Enter people's names, separated by commas:")
    list_names = people_names.split(", ")
    for name in list_names:
        name = name.split(" ")
        names_initials = name[0][0] + name[1][0]
        print(names_initials.upper())


def thirds():
    n = eval(input("Enter the number of sentences that will be input:"))
    for i in range(n):
        sentence = input("Enter sentence" + str(i+1) + ":")
        print(sentence[2::3])


def word_average():
    sentence = input("Enter a sentence:")
    word_list = sentence.split(" ")
    acc = 0
    for word in word_list:
        acc = acc + len(word)
    avg = acc / len(word_list)
    print(avg)


def pig_latin():
    sentence = input("Enter a sentence:")
    word_list = sentence.split(" ")
    for word in word_list:
        pig_translation = word[1:] + word[0] + "ay"
        print(pig_translation.lower(), end=" ")


def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()


main()
