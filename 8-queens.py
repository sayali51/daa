# 8-Queens Problem Using Backtracking (with first queen pre-placed)

N = 8

def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()


def is_safe(board, row, col, n):
    for j in range(n):
        if board[row][j] == 1:
            return False

    for dr, dc in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
        i, j = row + dr, col + dc
        while 0 <= i < n and 0 <= j < n:
            if board[i][j] == 1:
                return False
            i += dr
            j += dc

    return True


def solve_nqueens(board, col, n, first_col):
    if col >= n:
        return True

    if col == first_col:
        return solve_nqueens(board, col + 1, n, first_col)

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_nqueens(board, col + 1, n, first_col):
                return True
            board[row][col] = 0

    return False


# Driver code
first_row = int(input(f"Enter row index for first queen (0 to {N - 1}): "))
first_col = int(input(f"Enter column index for first queen (0 to {N - 1}): "))

if not (0 <= first_row < N and 0 <= first_col < N):
    print("Invalid position for the first queen.")
else:
    board = [[0] * N for _ in range(N)]
    board[first_row][first_col] = 1

    if solve_nqueens(board, 0, N, first_col):
        print("\nFinal 8-Queens Matrix:")
        print_board(board)
    else:
        print("\nNo solution exists with the given first queen position.")
