import numpy as np
from collections import Counter

board = np.array([["5","3",".",".","7",".",".",".","."],
                   ["6",".",".","1","9","5",".",".","."],
                   [".","9","8",".",".",".",".","6","."],
                   ["8",".",".",".","6",".",".",".","3"],
                   ["4",".",".","8",".","3",".",".","1"],
                   ["7",".",".",".","2",".",".",".","6"],
                   [".","6",".",".",".",".","2","8","."],
                   [".",".",".","4","1","9",".",".","5"],
                   [".",".",".",".","8",".",".","7","9"]])
output=np.matrix([["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]])


def checkFinish(board):
        n=np.arange(1,10)
        #3X3 boxes creation in the sudoku. Total nine boxes
        x=[[row[i:i+3]   for row in board][j-3:j]  for i in range(0,7,3) for j in range(3,10,3)]
        #checks horizontal rows for numbers 1-9
        if all([all([(Counter(row)[num]==1 and int(num) in n) for num in row]) for row in board]):
                #checks vertical columns for numbers 1-9
                if all(Counter([col[j] for col in board])[column[j]]==1 and int(column[j]) in n  for column in board for j in range(9)):
                        #checks each of the nine boxes for numbers 1-9
                        if all(all(t==1 for t in Counter([j for j in x[k][i]]).values()) for i in range(3) for k in range(9)):
                                return True
        return False

def checkValidBoard(board):
        n=np.arange(1,10)
        #3X3 boxes creation in the sudoku. Total nine boxes
        x=[[row[i:i+3]   for row in board][j-3:j]  for i in range(0,7,3) for j in range(3,10,3)]
        #checks horizontal rows for numbers 1-9
        if all([all([(Counter(row)[num]<=1 and int(num) in n) for num in row if num!='.']) for row in board]):
                #checks vertical columns for numbers 1-9
                if all([all([(Counter(col)[num]<=1 and int(num) in n) for num in col if num!='.']) for col in board.T]):
                        #checks each of the nine boxes for numbers 1-9
                        if all(all(t<=1 for t in Counter([j for j in x[k][i] if j!='.']).values()) for i in range(3) for k in range(9)):
                                return True
        return False

def solveSudoku(board)->None:
        

        dummy = board
        while not checkFinish(board):
                if checkValidBoard(board=board):
                        print('yes')
                        break
                
                                
                
        print("finished")

solveSudoku(board)
# print(list(board[i][0] for i in range(9)))
# print(board.T[0])

