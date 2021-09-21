import numpy as np
from random import *
from graphics import draw, make_text,create_board
import tkinter
from math import floor
canvas = tkinter.Canvas(width = 801, height = 801)
canvas.pack()

class HumanvsComputer():
    def __init__(self):
        self.board = np.zeros((8,8))
        self.move_position = None
        self.trap_position = None
        self.clicked = None
        self.whogoes = 1
        self.win = 0

    def moves(self):
        '''Obtains move information when game is played through string inputs'''
        if self.whogoes == 1:
            self.move_position = self.clicked

            self.computer_trap()
            self.player1move()
            self.whogoes = 2
            self.clicked = None
            print('lay your trap')

        elif self.whogoes == 2:
            print('make your move')
            self.trap_position = self.clicked
            self.computer_move()
            self.whogoes = 1
            self.clicked = None

        if self.win == 1:
            make_text(canvas,1)
            print('GAME OVER - Player 1 wins')
        elif self.win == 2:
            make_text(canvas,2)
            print('GAME OVER - Player 2 wins')

    def computer_move(self):
        i = randint(0,7)
        j = randint(0,7)
        if self.isempty(self.board,(i,j)):
            self.move_position = (i,j)
            print((i,j))
            self.player2move()
        else:
            self.computer_move()
    def computer_trap(self):
        i = randint(0,7)
        j = randint(0,7)
        if self.isempty(self.board,(i,j)):
            self.trap_position = (i,j)
            print((i,j))
        else:
            self.computer_trap()

    def click_input(self,tuple):
        y = tuple[0]/100
        y = floor(y) %8
        x = tuple[1]/100
        x = floor(x) % 8

        if self.isempty(self.board,(x,y)):
            self.clicked = (x,y)
            if self.win == 0 and 0 in self.board:
                self.moves()

    def player1move(self):
        '''Performs move of player 1'''
        if self.move_position != self.trap_position:
            self.board[self.move_position[0],self.move_position[1]] = 1
            draw(canvas,1,self.move_position)
            self.check_win(1,self.move_position)

        else:
            self.board[self.move_position[0],self.move_position[1]] = -1
            draw(canvas,2,self.move_position)
            self.check_win(2,self.move_position)


    def player2move(self):
        '''Performs move of player 2'''
        if self.move_position != self.trap_position:
            self.board[self.move_position[0],self.move_position[1]] = -1
            draw(canvas,2,self.move_position)
            self.check_win(2,self.move_position)
        else:
            self.board[self.move_position[0],self.move_position[1]] = 1
            draw(canvas,1,self.move_position)
            self.check_win(1,self.move_position)

    def check_win(self,player,position):
        self.check_column_win(player,position)
        if self.win == 0:
            self.check_row_win(player,position)
        if self.win == 0:
            self.check_diag_win(player,position)

    def check_column_win(self,player,position):
        row = position[0]
        col = position[1]
        if player == 1:
            count = 1
            j = 1
            k = 1
            while row + j < 8 and self.board[row + j][col] == 1:
                count += 1
                j += 1
                if count == 5:
                    self.win = 1
                    break
            while row - k > -1 and self.board[row-k][col] == 1:
                count += 1
                k += 1
                if count == 5:
                    self.win = 1
                    break
        if player == 2:
            count = 1
            j = 1
            k = 1
            while row + j < 8 and self.board[row + j][col] == -1:
                count += 1
                j += 1
                if count == 5:
                    self.win = -1
                    break
            while row - k > -1 and self.board[row-k][col] == -1:
                count += 1
                k += 1
                if count == 5:
                    self.win = -1
                    break

    def check_row_win(self,player,position):
        row = position[0]
        col = position[1]
        if player == 1:
            count = 1
            j = 1
            k = 1
            while col+ j < 8 and self.board[row][col+j] == 1:
                count += 1
                j += 1
                if count == 5:
                    self.win = 1
                    break
            while col - k > -1 and self.board[row][col-k] == 1:
                count += 1
                k += 1
                if count == 5:
                    self.win = 1
                    break
        if player == 2:
            count = 1
            j = 1
            k = 1
            while col + j < 8 and self.board[row][col+j] == -1:
                count += 1
                j += 1
                if count == 5:
                    self.win = -1
                    break
            while col - k > - 1 and self.board[row][col-k] == -1:
                count += 1
                k += 1
                if count == 5:
                    self.win = -1
                    break
    def check_diag_win(self,player,position):
        row = position[0]
        col = position[1]
        if player == 1:
            count = 1
            j = 1
            k = 1
            while col+ j < 8 and row + j < 8 and self.board[row+j][col+j] == 1:
                count += 1
                j += 1
                if count == 5:
                    self.win = 1
                    break
            while col - k > -1 and row - k > -1 and self.board[row-k][col-k] == 1:
                count += 1
                k += 1
                if count == 5:
                    self.win = 1
                    break
            count = 1
            j = 1
            k = 1
            while col+ j < 8 and row - j > -1 and self.board[row-j][col+j] == 1:
                count += 1
                j += 1
                if count == 5:
                    self.win = 1
                    break
            while col - k > -1 and row +k < 8 and self.board[row+k][col-k] == 1:
                count += 1
                k += 1
                if count == 5:
                    self.win = 1
                    break
        if player == 2:
            count = 1
            j = 1
            k = 1
            while col+ j < 8 and row + j < 8 and self.board[row+j][col+j] == -1:
                count += 1
                j += 1
                if count == 5:
                    self.win = -1
                    break
            while col - k > -1 and row - k > -1 and self.board[row-k][col-k] == -1:
                count += 1
                k += 1
                if count == 5:
                    self.win = -1
                    break
            count = 1
            j = 1
            k = 1
            while col+ j < 8 and row - j > -1 and self.board[row-j][col+j] == -1:
                count += 1
                j += 1
                if count == 5:
                    self.win = -1
                    break
            while col - k > -1 and row +k < 8 and self.board[row+k][col-k] == -1:
                count += 1
                k += 1
                if count == 5:
                    self.win = -1
                    break


    @staticmethod
    def isempty(board,tuple):
        if board[tuple[0],tuple[1]] == 0:
            return True
        return False


game = HumanvsComputer()
create_board(canvas)
def click(event):
    x = event.x
    y = event.y
    game.click_input((x,y))
canvas.bind('<Button-1>', click)
canvas.mainloop()
