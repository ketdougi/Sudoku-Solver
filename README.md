# Sudoku-Solver
## Introduction
Sudoku is a puzzle game where users can solve the puzzle by filling out the empty spaces on the board with numbers from 1-9 making sure no number is repeated in a row, column or box. 

## Purpose
1. To solidify understanding of backtracking algorithm by implementing 
2. To review basic python types and methods

## Implementation
The solver uses a backtracking algorithm to solve the given sudoku board. The algorithm is implemented in the solver method by using recursion. The solver firsts parses through the board to find the first empty spot. Then the lowest number that fulfills the rules of sudoku will be placed into that spot and the solver is called again with the updated board. This process is repeated until board is completed or an empty spot is reached that cannot be filled by following the rules of sudoku. If this case occurs, the program back-tracks to the last filled spot and tries the next lowest number that follows the rules of sudoku. When there are no more empty spots, the board has been solved.
