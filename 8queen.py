def is_safe(board, row, col):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check if there is a queen in the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check if there is a queen in the lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens(board, col):
    # All queens are placed, return True
    if col == len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solve_nqueens(board, col + 1):
                return True

            # If placing queen in the current position doesn't lead to a solution,
            # then backtrack and try placing the queen in a different row.
            board[i][col] = 0

    # If no row is found in this column, return False
    return False

def print_solution(board):
    for row in board:
        print(" ".join(map(str, row)))

def eight_queens():
    # Initialize an 8x8 chessboard with all zeros
    board = [[0] * 8 for _ in range(8)]

    # Call the recursive function to solve the N-Queens problem
    if solve_nqueens(board, 0):
        print_solution(board)
    else:
        print("Solution does not exist.")
eight_queens()
