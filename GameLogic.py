import random

class Game2048(object):
    UP = None
    DOWN = None
    LEFT = None
    RIGHT = None

    def __init__(self, row, column):
        self.board = [[0 for x in range(row)] for y in range(row)]
        self.n_rows = row
        self.boardSize = len(self.board)
        self.L_plus_ratio = False

    # ACTIONS

    def mergeTiles(self, moveDirection, tile1: list, tile2: list):
        if self.canMerge(tile1, tile2):
            if moveDirection == 1 or moveDirection == 2:
                self.board[tile1[0]][tile1[1]] *= 2
                self.board[tile2[0]][tile2[1]] = 0
            if moveDirection == 3 or moveDirection == 4:
                self.board[tile1[0]][tile1[1]] *= 2
                self.board[tile2[0]][tile2[1]] = 0
        else:
            return

    def canMerge(self, tile1: list, tile2: list):
        return self.board[tile1[0]][tile1[1]] == self.board[tile2[0]][tile2[1]]

    def isOpen(self,row,column):
        return self.board[row][column] == 0

    def newTile(self):
        row = random.randint(0,self.n_rows)
        column = random.randint(0,self.n_rows)
        val = random.randrange(2,4,2) #chose between either 2 or 4

        if self.isOpen(row, column):
            self.board[row][column] = val


