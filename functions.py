WINNING_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


def get_move(board, player):
    while True:
        text = input(f"Player {player}, choose a cell (1-9): ")

        if not text.isdigit():
            print("Please enter a number.")
            continue

        num = int(text)
        if num < 1 or num > 9:
            print("The number must be between 1 and 9.")
            continue

        if board[num - 1] is not None:
            print("That cell is already taken.")
            continue

        return num - 1


def check_win(board, player):
    for a, b, c in WINNING_LINES:
        if board[a] == player and board[b] == player and board[c] == player:
            return True
    return False
