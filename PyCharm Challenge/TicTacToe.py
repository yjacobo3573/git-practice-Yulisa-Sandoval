

def print_board(board):
    for r in board:
        print(" | ".join(r))
        print("-" * 5)


def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
        if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
            return True
        return False


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    print("Tic-Tac-Toe Game")
    print_board(board)
    for turn in range(9):
        current_player = players[turn % 2]
        while True:
            try:
                row, col = map(int,
                               input(f"Player {current_player}, enter row and column (0-2): ").split())
                if board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("Cell in use! Try again.")
            except(ValueError, IndexError):
                print("Cell occupied! Try again.")
        print_board(board)
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            return
        if is_board_full(board):
            print("It's a draw!")
            return
    print("It's a draw!")

tic_tac_toe()
