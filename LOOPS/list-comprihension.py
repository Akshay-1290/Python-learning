import random

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_board():
    print("\n___BOARD___")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


def change_board(place, sign):
    if board[place - 1] == "X" or board[place - 1] == "O":
        return False

    board[place - 1] = sign
    return True


def check_winner():
    win_patterns = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]
    ]

    for a, b, c in win_patterns:
        if board[a] == board[b] == board[c]:
            return board[a]

    return None


def is_draw():
    for cell in board:
        if cell != "X" and cell != "O":
            return False
    return True


def computer_move():
    available = []

    for cell in board:
        if cell != "X" and cell != "O":
            available.append(cell)

    move = random.choice(available)
    change_board(move, "O")


def main():

    while True:

        print_board()

        try:
            pos = int(input("Choose position (1-9): "))
        except ValueError:
            print("Enter a valid number!")
            continue

        if pos < 1 or pos > 9:
            print("Position must be between 1 and 9")
            continue

        if not change_board(pos, "X"):
            print("Position already occupied!")
            continue

        winner = check_winner()

        if winner:
            print_board()
            print(f"{winner} Wins!")
            break

        if is_draw():
            print_board()
            print("Match Draw!")
            break

        computer_move()

        winner = check_winner()

        if winner:
            print_board()
            print(f"{winner} Wins!")
            break

        if is_draw():
            print_board()
            print("Match Draw!")
            break


if __name__ == "__main__":
    main()