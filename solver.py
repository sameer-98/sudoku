board = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

# create a function that when given a board, a number and position checks if 
# the move is valid or not
def isValid(board, num, row, col):
    #Check the row
    for i in range(9):
        if board[row, i] == num:
            return False
    #Check the column
    for j in range(9):
        if board[i, col] == num:
            return False
    
    #Check the 3x3 subgrid
    box_x = row // 3 
    box_y = col // 3

    for i in range(box_x * 3, box_x * 3 + 3):
        for j in range(box_y * 3, box_y * 3 + 3):
            if board[i][j] == num:
                return False
    return True

# Create a function that given a row col and a board solves for the cell 
def solve(row, col, board):
    pass