board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
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

def find_empty(bo):
    '''
        finds the empty position in the board

        :param bo: 2d list of integer
        :return: tuple of row and column location of the empty spot 
    '''
    for i in range(9):
        for j in range(9):
            if bo[i,j] == 0:
                return i, j
    
    return None

def print_board(bo):
    '''
        pretty prints the board
        :param bo: 2d list of integers
    '''
    for i in range(9):
        if i % 3 == 0 and i != 0:
                print('- - - - - - - - - - - - - - - - -') 
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print('| ', end='')
            print(bo[i][j],' ', end='')
        print('\n')
        
        
    
print_board(board)