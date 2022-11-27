N = int(input('Enter count of Queens: '))
board = [['#' for x in range(N)] for y in range(N)]
countofsolutions = 0

def isValid(board, row, column):
    for i in range(row):
        if board[i][column] == 'Q':
            return False
    i = row
    j = column
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1
    g = row
    k = column
    while g >= 0 and k < len(board):
        if board[g][k] == 'Q':
            return False
        g = g - 1
        k = k + 1
    return True

def printSolution(board):
    for row in board:
        print(str(row).replace(',', '').replace('\'', ''))
    print(f'{(N+1)*"__"}\n') 
    
def nQueen(board, row):
    if row == len(board):
        global countofsolutions
        printSolution(board)
        countofsolutions += 1
        return 
    
    for column in range(len(board)):
        if isValid(board, row, column):
            board[row][column] = 'Q'
            nQueen(board, row + 1)
            board[row][column] = '#'

nQueen(board,0) 
print(f'Found {countofsolutions} solutions:')