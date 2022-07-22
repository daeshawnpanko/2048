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

    def mergeTiles(self, tile1, tile2):
        return
    def canMerge(self,tile1,tile2):
        # if tile1 value == tile2 value
        #   return True
        return False
    def isOpen(self,row,column):
        return self.board[row][column] == 0

    def newTile(self):
        row = random.randint(0,self.n_rows)
        column = random.randint(0,self.n_rows)
        val = random.randrange(2,4,2) #chose between either 2 or 4

        if(self.isOpen(row,column)):
            self.board[row][column]


