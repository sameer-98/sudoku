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

board1 = [[0,0,0,2,6,0,7,0,1],
          [6,8,0,0,7,0,0,9,0],
          [1,9,0,0,0,4,5,0,0],
          [8,2,0,1,0,0,0,4,0],
          [0,0,4,6,0,2,9,0,0],
          [0,5,0,0,0,3,0,2,8],
          [0,0,9,3,0,0,0,7,4],
          [0,4,0,0,5,0,0,3,6],
          [7,0,3,0,1,8,0,0,0]
          ]

board2 = [[0,2,0,6,0,8,0,0,0],
          [5,8,0,0,0,9,7,0,0],
          [0,0,0,0,4,0,0,0,0],
          [3,7,0,0,0,0,5,0,0],
          [6,0,0,0,0,0,0,0,4],
          [0,0,8,0,0,0,0,1,3],
          [0,0,0,0,2,0,0,0,0],
          [0,0,9,8,0,0,0,3,6],
          [0,0,0,3,0,6,0,9,0],
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
        if board[row][i] == num and i != col:
            return False
    
    # check the whole column
    for j in range(9):
        if board[j][col] == num and j != row:
            return False
        
    # check the 3x3 subgrid
    grid_x = row // 3
    grid_y = col // 3

    for i in range(grid_x*3, grid_x*3 + 3):
        for j in range(grid_y*3, grid_y*3 + 3):
            if board[i][j] == num:
                return False
            
    return True

# Create a function that recursively solves the board
def solve(board):
    '''
        Solves the board
        :param board: 2d array of integers
        :return bool: True or False if the solution is found or not
    '''
    #find if there are empty spaces left, if there are none then the board is solved
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    
    # Now loop through 1 - 9 and try to place a number in the spot
    for i in range(1,10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i 

            if solve(board):
                return True
            
            # if the board comes to a point where none of the numbers at the position are valid then reset to 0
            board[row][col] = 0        

    return False


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
    solve(board)
    solve(board1)
    solve(board2)

    print(board)
    print(board1)
    print(board2)

    

