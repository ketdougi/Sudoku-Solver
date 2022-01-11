def find_empty(board):
    for row in board:
        for entry in row:
            if entry == 0:
                return board.index(row), row.index(entry)
    return 0, 0

def column(board, col):
    column = []
    for row in board:
        column.append(row[col])
    return column

def row_check(board, row, num):
    try:
        board[row].index(num)
    except:
        return True
    return False

#returns true if num is not in row
def column_check(board, column, num):
    try:
        column.index(num)
    except:
        return True
    return False

def square_check(board, row, col, num):
    row_temp = get_index(row)
    col_temp = get_index(col)

    row_ind = row_temp
    col_ind = col_temp

    while row_ind < row_temp+3:
        while col_ind < col_temp+3:
            if board[row_ind][col_ind] == num:
                return False
            col_ind+=1
        row_ind+=1
        col_ind = col_temp
    return True


def get_index(num):
    if num in list(range(0,3)):
        return 0
    elif num in list(range(3,6)):
        return 3
    elif num in list(range(6,9)):
        return 6


def solve(board):
    found = find_empty(board)
    if found == (0,0):
        return board
    else: 
        row, col = found
        values = list(range(1,10))

        cur_column = column(board, col)

        for num in values:
            if row_check(board, row, num) and column_check(board, cur_column, num ) and square_check(board, row, col, num):
                board[row][col] = num
                solve(board)
    
def print_board(board):
    for row in board:
        print(row)
    
def check_correct(board, answerkey):
    return board == answerkey



unsolved = [[8,0,7,1,5,0,0,9,6],
[0,6,5,3,0,7,1,4,0],
[3,4,1,0,8,0,7,0,2],
[5,9,3,4,6,8,2,7,0],
[4,0,0,0,1,0,0,0,9],
[0,1,8,9,7,2,4,3,5],
[7,0,6,0,3,0,9,1,4],
[0,5,4,7,0,6,8,2,0],
[2,3,0,0,4,1,5,0,7]]


solved = [[8,2,7,1,5,4,3,9,6],
[9,6,5,3,2,7,1,4,8],
[3,4,1,6,8,9,7,5,2],
[5,9,3,4,6,8,2,7,1],
[4,7,2,5,1,3,6,8,9],
[6,1,8,9,7,2,4,3,5],
[7,8,6,2,3,5,9,1,4],
[1,5,4,7,9,6,8,2,3],
[2,3,9,8,4,1,5,6,7]]


print("Unsolved Board")
print_board(unsolved)

solve(unsolved)

print()
print("Board solved using backtracking algorithm")
print_board(unsolved)

if check_correct(unsolved, solved):
    print("Sudoku board is correct")
else: 
    print("Sudoku board is incorrect")