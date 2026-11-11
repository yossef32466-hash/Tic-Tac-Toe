from game_display import print_board
from functions import get_move, check_win


def main():
    board = [None] * 9
    player = "X"

    while True:
        print_board(board)
        index = get_move(board, player)
        board[index] = player

        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if None not in board:
            print_board(board)
            print("It's a draw!")
            break

        if player == "X":
            player = "O"
        else:
            player = "X"


main()