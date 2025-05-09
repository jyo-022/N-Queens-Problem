🧠 N-Queens Problem Solver in Python

This project solves the classic N-Queens problem using backtracking. The goal is to place N queens on an N×N chessboard such that no two queens threaten each other (i.e., no two queens share the same row, column, or diagonal).

 📝 Problem Statement

Place N queens on an N×N chessboard so that:
- No two queens are in the same row
- No two queens are in the same column
- No two queens are on the same diagonal

This is a common problem used to teach constraint satisfaction and recursion in computer science.

 💡 Approach

- Represent the chessboard using a 2D array (matrix).
- Use backtracking to try placing queens row-by-row.
- At each step, check if a queen can be safely placed.
- If not, backtrack and try the next possibility.

 📌 Features

- Easy-to-read output with board visualizations
- Customizable board size by setting N
- Uses simple Python logic with no external libraries

 🧪 Example Output (N=4)

. Q . .
. . . Q
Q . . .
. . Q .

. . Q .
Q . . .
. . . Q
. Q . .

🚀 How to Run

1. Clone this repository:
  
   git clone https://github.com/yourusername/n-queens-backtracking.git
   cd n-queens-backtracking
   
Run the Python script:
python n_queens.py

Change N in the code to solve for different board sizes:
N = 4  # Change to 8 for the 8-Queens problem, etc.

🔧 Requirements
Python 3.x
No external packages required.

🌐 License
This project is open source and available under the MIT License.
