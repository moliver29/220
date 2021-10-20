"""
Name: Max Oliver
vigenere.py

Problem: Create a graphic interface that accepts a message and will return an encoded message using a vigenere cipher.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *


# code function
def code(message, keyword):
    m = message.upper
    k = keyword.upper
    acc = ""
    for i in range(len(m)):
        c = ord(m[i])
        key = ord(k[i])
        result = c + key - 97
        acc = acc + chr(result)
    return acc



def main():
    # create window
    win = GraphWin("Vigenere", 500, 500)

    # create text, entry boxes and button
    text_entry1 = Text(Point(150, 100), "Message to Code")
    text_entry1.draw(win)
    text_entry2 = Text(Point(150, 200), "Enter Keyword")
    text_entry2.draw(win)
    entry1 = Entry(Point(350, 100), 20)
    entry1.draw(win)
    entry2 = Entry(Point(350, 200), 20)
    entry2.draw(win)
    button = Text(Point(250, 300), "Encode")
    button.draw(win)
    Rectangle(Point(220, 280), Point(280, 320)).draw(win)

    # click button to encode
    win.getMouse()
    code(text_entry1.getText(), text_entry2.getText())

    # click to close window
    close_pt = Point(250, 450)
    close = Text(close_pt, "Click Anywhere to Close Window")
    close.draw(win)
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()

