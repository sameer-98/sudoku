from solver import find_empty,isValid, board

def test_find_empty():
    assert find_empty(board) == (0,2)

    # filling (0,2)
    board[0][2] = 1
    assert find_empty(board) == (0,4)

def test_is_valid():
    assert isValid(board, 7, (2,0)) == False
    assert isValid(board, 7, (0,2)) == False
    assert isValid(board, 8, (1,7)) == False
    