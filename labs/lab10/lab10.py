"""
Name: Max Oliver
lab10.py
"""


def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def display_board(board):
    print("-" * 10)
    counter = 0
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(board[counter], end="|")
            counter += 1
    print("-" * 10)


def place_spot(board, spot, marker):
    board[spot] = marker


def legal_spot(board, spot):
    if board[spot] == "X" or board[spot] == "O" or spot < 1 or spot > 9:
        return False
    else: return True


def game_won(board):
    win_con = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for condition in win_con:
        counter = 0
        for spot in condition:
            if spot == "X":
                counter = 1
            if counter == 3:
                return "X Wins!"
        for spot in condition:
            if spot == "O":
                counter = 1
            if counter == 3:
                return "O Wins!"
        else:
            return False


def game_over(board, turn_count):
    if ((game_won(board) == "X Wins!" or game_won(board) == "O Wins!")
            or (turn_count > 9)):
        return True
    else:
        return False


def play_game():
    board = build_board()
    display_board(board)
    turn_count = 0
    while not game_over(board, turn_count):
        x_spot = eval(input("X's turn. Enter the spot you wish to mark:"))
        if legal_spot(board, x_spot):
            place_spot(board, x_spot, "X")
            turn_count += 1
            display_board(board)
        if not game_won(board):
            o_spot = eval(input("O's turn. Enter the spot you wish to mark:"))
            if legal_spot(board, o_spot):
                place_spot(board, o_spot, "X")
                turn_count += 1
                display_board(board)
    if game_won(board) == "X Wins!":
        return "X has won the game!"
    if game_won(board) == "O Wins!":
        return "O has won the game!"
    else:
        return "Draw"


def main():
    play_game()
    pass


main()
