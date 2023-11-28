class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def display_board(self):
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i+3]))
            if i < 6:
                print("---------")

    def is_winner(self, player):
        # Check rows, columns, and diagonals for a win
        for i in range(0, 9, 3):
            if all(self.board[i:i+3] == [player] * 3) or all(self.board[i::3] == [player] * 3):
                return True
        return all(self.board[0::4] == [player] * 3) or all(self.board[2:7:2] == [player] * 3)

    def is_full(self):
        return " " not in self.board

    def is_game_over(self):
        return self.is_winner("X") or self.is_winner("O") or self.is_full()

    def get_available_moves(self):
        return [i for i, value in enumerate(self.board) if value == " "]

    def make_move(self, move):
        self.board[move] = self.current_player
        self.current_player = "O" if self.current_player == "X" else "X"

    def undo_move(self, move):
        self.board[move] = " "
        self.current_player = "O" if self.current_player == "X" else "X"

def minimax(board, depth, maximizing_player):
    if board.is_winner("X"):
        return -1
    elif board.is_winner("O"):
        return 1
    elif board.is_full():
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for move in board.get_available_moves():
            board.make_move(move)
            eval = minimax(board, depth + 1, False)
            board.undo_move(move)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.get_available_moves():
            board.make_move(move)
            eval = minimax(board, depth + 1, True)
            board.undo_move(move)
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_score = float('-inf')
    best_move = None
    for move in board.get_available_moves():
        board.make_move(move)
        score = minimax(board, 0, False)
        board.undo_move(move)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def main():
    game = TicTacToe()

    while not game.is_game_over():
        game.display_board()

        if game.current_player == "X":
            move = int(input("Enter your move (0-8): "))
        else:
            move = get_best_move(game)

        if move in game.get_available_moves():
            game.make_move(move)
        else:
            print("Invalid move. Try again.")

    game.display_board()

    if game.is_winner("X"):
        print("You win!")
    elif game.is_winner("O"):
        print("Computer wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
