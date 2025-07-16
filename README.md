README FILE for "Sudoku Solver"

----------------------------------------

Description:
This is a command-line Sudoku solver written in Python. It uses the 
backtracking algorithm to solve a 9x9 Sudoku puzzle provided by the user.
Empty cells must be filled with 0 during input.

----------------------------------------

Files Included:
- sudoku_solver.py – The main Python file containing the solver.
- README.txt – You’re reading it.

----------------------------------------

▶How to Run:

1. Make sure you have Python 3 and NumPy installed.
   - Install NumPy if needed:
     pip install numpy

2. Run the script in your terminal or command prompt:
   python sudoku_solver.py

----------------------------------------

How to Input the Puzzle:

- You will be prompted to enter 9 rows, one at a time.
- Each row must be exactly 9 digits.
- Use 0 to represent empty cells.

Example input row:
530070000

This means:
5 3 0 | 0 7 0 | 0 0 0

----------------------------------------

Features:

- Accepts user input for custom Sudoku puzzles.
- Displays the board in a clean, readable format.
- Uses efficient backtracking for solving.
- Notifies user if the puzzle is unsolvable.

----------------------------------------

Functions Overview:

- initialize_board() – Creates an empty 9x9 board.
- input_board() – Collects puzzle input from the user.
- display_board() – Nicely prints the board.
- is_valid() – Validates number placement.
- solve_sudoku() – Solves the puzzle using backtracking.
- main() – Entry point of the script.

----------------------------------------

Author: Shameer Asim
