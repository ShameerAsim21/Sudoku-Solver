import numpy as np


def initialize_board():
    """Initializes a 9x9 Sudoku board with zeros (empty cells)."""
    return np.zeros((9, 9), dtype=int)


def input_board():
    """
    Takes input from the user for a Sudoku puzzle.
    The user is asked to input 9 lines, each with 9 digits (0 for empty cells).
    """
    print("Enter the Sudoku puzzle row by row (use 0 for empty cells):")
    board = []
    for i in range(9):
        while True:
            row_input = input(f"Row {i + 1}: ")
            if len(row_input) == 9 and row_input.isdigit():
                row = [int(char) for char in row_input]
                board.append(row)
                break
            else:
                print("Invalid input. Please enter exactly 9 digits (0-9).")
    return np.array(board)


def display_board(board):
    """Displays the Sudoku board in a readable format."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else '.', end=" ")
        print()
    print()

# Code by: Shameer Asim


def is_valid(board, row, col, num):
    """Checks if placing `num` at (row, col) is valid."""

    if num in board[row]:
        return False

    if num in board[:, col]:
        return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    if num in board[start_row:start_row + 3, start_col:start_col + 3]:
        return False
    return True

def solve_sudoku(board):
    """Solves the Sudoku board using backtracking."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def main():
    board = input_board()
    print("\nInitial Board:")
    display_board(board)

    if solve_sudoku(board):
        print("Solved Sudoku:")
        display_board(board)
    else:
        print("No solution exists for the given Sudoku puzzle.")

if __name__ == "__main__":
    main()
#run using: python sudoku_solver.py