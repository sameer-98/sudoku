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
def is_valid(board, num, pos):
    '''
        checks whether the given position is a valid move or not
        :param board: 2d list of integer
        :param num: The number to be inserted at the position
        :param pos: A tuple of row and column number where the number is to be inserted
        :return bool: True or False 
    '''
    row = pos[0]
    col = pos[1]

    #Check the whole row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # check the whole column
    for j in range(9):
        if board[j][col] == num:
            return False
        
    # check the 3x3 subgrid
    grid_x = row // 3
    grid_y = col // 3

    for i in range(grid_x*3, grid_x*3 + 3):
        for j in range(grid_y*3, grid_y*3 + 3):
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
            if bo[i][j] == 0:
                return (i, j)
    
    return None

def print_board(bo):
    '''
        pretty prints the board
        :param bo: 2d list of integers
    '''
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - - - - - - -')
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0 :
                print(' | ', end='')

            if j == 8:
                print(bo[i][j], end='')
            else:
                print(bo[i][j], ' ', end='')
        
        print('\n')
        
if __name__ == '__main__':    
    print_board(board)
    