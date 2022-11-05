ROWS = 3
COLS = 3


def display_board(data):
    print("TIC TAC TOE")
    board = ""
    for row in range(ROWS):
        board += "*\t"
        for col in range(COLS - 1):
            board += f" {data[row][col]} |"
        board += f" {data[row][COLS-1]}"
        board += "\t*"
        board += "\n"
        if row != ROWS - 1:
            board += "*\t---|---|---\t*\n"
    print(board)


def player_input(player, data):
    print(f"Player {player} turn...")
    check = False
    while not check:
        row = int(input("Enter row: ")) - 1
        col = int(input("Enter col: ")) - 1
        if data[row][col] != " ":
            print("Already filled")
            continue
        check = True

    return row, col


def check_win(player, data):
    win = False
    for row in range(ROWS):
        data_row = data[row]
        win = all([item == player for item in data_row])
        if win:
            return True
    for col in range(COLS):
        data_col = [data[row][col] for row in range(ROWS)]
        win = all([item == player for item in data_col])
        if win:
            return True
    first_d = [data[row][row] for row in range(ROWS)]
    win = all([item == player for item in first_d])
    if win:
        return True

    second_d = [data[row][ROWS - row - 1] for row in range(ROWS)]
    win = all([item == player for item in second_d])
    if win:
        return True


def player_switch(player):
    if player == "X":
        player = "O"
    else:
        player = "X"
    return player


def play():
    player = "X"
    MAX_TURNS = COLS * ROWS
    turn = 1
    data = []
    for _ in range(ROWS):
        row = []
        for _ in range(COLS):
            row.append(" ")
        data.append(row)

    print(data)
    win = False
    while turn != MAX_TURNS:
        display_board(data)
        row, col = player_input(player, data)
        data[row][col] = player
        display_board(data)
        win = check_win(player, data)
        if win:
            print(f"{player} wins!")
            break
        player = player_switch(player)
        turn += 1

    if not win:
        print("TIE")


play()