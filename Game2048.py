import tkinter as tk
import random as r
import GameLogic as logic
import properties as p

class Game2048(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>",self.keyPress)

        self.actions = {
            p.KEY_LEFT : logic.moveLeft,
            p.KEY_UP : logic.moveUp,
            p.KEY_RIGHT : logic.moveRight,
            p.KEY_DOWN : logic.moveDown
        }

        self.gameMatrix = []
        self.createGameScreen()
        self.gameGrid = self.newGame(size=p.LEN)
        self.updateCell()

        self.mainloop()


    def createGameScreen(self):
        bg = tk.Frame(self,bg=p.GAME_BG,width=p.SCREEN_SIZE,height=p.SCREEN_SIZE)
        bg.grid()

        for x in range(p.LEN):
            cellRow = []
            for y in range(p.LEN):
                cell = tk.Frame(bg, bg=p.EMPTY_CELL_COLOR, width=(p.SCREEN_SIZE / p.LEN),height=(p.SCREEN_SIZE / p.LEN))
                cell.grid(row=x,column=y,padx=p.PADDING,pady=p.PADDING)
                cell_value = tk.Label(master=cell,text='',bg=p.EMPTY_CELL_COLOR,justify=tk.CENTER,font=p.FONT,width=4,height=2)
                cell_value.grid()
                cellRow.append(cell_value)
            self.gameMatrix.append(cellRow)


    def keyPress(self,e):
        key = e.keysym
        print(e)

        if key == p.QUIT: exit()
        elif key in self.actions:
            self.gameGrid = self.actions[key](self.gameGrid)
        self.updateCell()


    def newGame(self,size):
        return logic.newGame(size)


    def updateCell(self):
        for x in (range(p.LEN)):
            for y in range(p.LEN):
                num = self.gameGrid[x][y]
                # empty cell handling
                if num == 0:
                    self.gameMatrix[x][y].configure(text='',bg=p.EMPTY_CELL_COLOR)
                else:
                    self.gameMatrix[x][y].configure(text=str(num),bg=p.CELL_COLOR_BY_VALUE[num],fg='#000000')
        self.update_idletasks()


Game2048()
