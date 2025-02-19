def print_board(board):
    """
    Displays the current state of the Tic-Tac-Toe board.

    Args:
        board (list of list of str): A 3x3 grid representing the board,
                                     where each cell contains "X", "O", or " ".
    """
    for r in board:
        print(" | ".join(r))
        print("-" * 5)


def check_winner(board, player):
    """
    Checks if the given player has won the game.

    Args:
        board (list of list of str): A 3x3 grid representing the board,
                                     where each cell contains "X", "O", or " ".
        player (str): The player's symbol ("X" or "O").

    Returns:
        bool: True if the player has won, otherwise False.
    """
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
        if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
            return True
        return False


def is_board_full(board):
    """
    Checks if the board is full, i.e., no empty cells remain.

    Args:
        board (list of list of str): A 3x3 grid representing the board, 
                                     where each cell contains "X", "O", or " ".

    Returns:
        bool: True if all cells are occupied, otherwise False.
    """
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    """
    Main function to play a game of Tic-Tac-Toe.

    This function initializes the game board, alternates turns between two players ("X" and "O"),
    and checks for a winner or a draw after each move. The game continues until a player wins 
    or all cells are filled.

    Players take turns inputting their moves, and the board's state is displayed after each move.

    Returns:
        None
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    print("Tic-Tac-Toe Game")
    print_board(board)
    for turn in range(9):
        current_player = players[turn % 2]
        get_player_input(board, current_player)
        print_board(board)
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            return
        if is_board_full(board):
            print("It's a draw!")
            return
    print("It's a draw!")


def get_player_input(board, current_player):
    """
    Handles input from the current player and updates the game board.

    Prompts the current player to enter the row and column numbers (between 0 and 2) 
    to place their symbol on the board. The function ensures that the input is valid 
    and that the chosen cell is not already occupied.

    Args:
        board (list of list of str): A 3x3 grid representing the board,
                                     where each cell contains "X", "O", or " ".
        current_player (str): The player's symbol ("X" or "O").

    Returns:
        None
    """
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


tic_tac_toe()
