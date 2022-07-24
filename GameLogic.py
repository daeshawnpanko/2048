import random as r
import properties as p

def newGame(size):
    temp = []
    for x in range(size):
        temp.append([0]*size)

    temp = newTile(temp)
    temp = newTile(temp)
    return temp
# ACTIONS

def reverse(board):
    temp = []
    for x in range(p.LEN):
        temp.append([])
        for y in range(p.LEN):
            temp[x].append(board[x][p.LEN - (y+1)])
    return temp

def transpose(board):
    temp = []
    for x in range(p.LEN):
        temp.append([])
        for y in range(len(board)):
            temp[x].append(board[y][x])
    return temp

def mergeTiles( board):
    for x in range(4):
        for y in range(4):
            if board[x][y] != 0 and board[x][y] == board[x][y+1]:
                board[x][y] *=2
                board[x][y+1] = 0
    return board

def newTile(board):
    row = r.randint(0,p.LEN-1)
    col = r.randint(0,p.LEN-1)

    while board[row][col] !=0:
        row = r.randint(0, p.LEN-1)
        col = r.randint(0, p.LEN-1)
    board[row][col] = r.choice([2,4])
    return board




def shift(board):
    temp = [[0] * 4 for x in range(4)]
    for x in range(4):
        tempIndex = 0
        for y in range(4):
            if board[x][y] != 0:
                temp[x][tempIndex] = board[x][y]
                tempIndex+=1
    board = temp
    return board

def moveLeft(board):
    if not horizontalMoveAvailable(board):
        return
    print("moved left")
    board = shift(board)
    board = mergeTiles(board)
    board = shift(board)

    board = newTile(board)

    return board

def moveUp(board):
    if not verticleMoveAvailable(board):
        return
    print("moved up")

    board = transpose(board)
    board = shift(board)
    board = mergeTiles(board)
    board = shift(board)
    board = transpose(board)

    board = newTile(board)

    return board

def moveRight(board):
    if not horizontalMoveAvailable(board):
        return
    print("moved right")
    board = reverse(board)

    board = shift(board)
    board = mergeTiles(board)
    board = shift(board)

    board = reverse(board)

    board = newTile(board)

    return board

def moveDown(board):
    if not verticleMoveAvailable(board):
        return
    board = transpose(board)
    board = reverse(board)
    board = shift(board)
    board = mergeTiles(board)
    board = shift(board)
    board = reverse(board)
    board = transpose(board)

    board = newTile(board)

    return board



def verticleMoveAvailable(board):
    canMove = False
    for x in range(3):
        for y in range(4):
            if board[x][y] == board[x+1][y]:
                canMove = True

    if not canMove:
        print("column is full")
    return canMove

def horizontalMoveAvailable(board):
    canMove = False
    for x in range(4):
        for y in range(3):
            if board[x][y] == board[x][y+1]:
                canMove = True
    if not canMove:
        print("row is full")
    return canMove


def GameOver(board):
    return not verticleMoveAvailable(board) and not horizontalMoveAvailable(board)
