import numpy as np
N = int(input("Enter the number of queens: "))
board = np.array([['.'] * N for _ in range(N)])
res = []

def is_safe(board, row, col, n):
    # ROW
    for i in range(col):
        if board[row][i] == 'Q':
            return False
    # COLUMN
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    # LEFT-DIAGONAL
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    # RIGHT-DIAGONAL
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False
    return True
    
def queens(board,row,n,res):
    if(row == n):
        res.append(board.copy())
        return
    for i in range(n):
        if(is_safe(board,row,i,n)):
            board[row][i] = 'Q'
            queens(board,row+1,n,res)
            board[row][i] = '.'

queens(board,0,N,res)
for i in res:
    for row in i:
        print(' '.join(row))
    print('-'*20)
