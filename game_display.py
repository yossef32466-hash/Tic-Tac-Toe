def print_board(board):
    cells = []
    for i in range(9):
        sign = board[i] if board[i] else " "
        cells.append(f"[{i + 1}] {sign}")

    print(f"{cells[0]} | {cells[1]} | {cells[2]}")
    print("------+-------+------")
    print(f"{cells[3]} | {cells[4]} | {cells[5]}")
    print("------+-------+------")
    print(f"{cells[6]} | {cells[7]} | {cells[8]}")