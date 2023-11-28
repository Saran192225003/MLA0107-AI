def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
  
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_player_move(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0, 1, or 2): "))
            col = int(input(f"Player {player}, enter column (0, 1, or 2): "))
            if 0 <= row < 3 and 0 <= col < 3:
                return row, col
            else:
                print("Invalid input. Row and column must be between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    print("Welcome to Tic Tac Toe!")

    while True:
        print_board(board)
        row, col = get_player_move(players[current_player])

        if board[row][col] == ' ':
            board[row][col] = players[current_player]
            if check_winner(board, players[current_player]):
                print_board(board)
                print(f"Player {players[current_player]} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = 1 - current_player  # Switch player
        else:
            print("Cell already occupied. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
