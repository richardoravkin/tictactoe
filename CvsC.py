import numpy as np
from random import *
import copy

class ComputervsComputer():
    def __init__(self,whogoes):
        self.board = np.zeros((8,8))
        self.move_position = None
        self.trap_position = None
        self.whogoes = whogoes
        self.win = None
        self.game_data = []
        self.moves = 0

    def play(self):
        '''Obtains move information when game is played through string inputs'''
        #self.computer_trap()
        self.computer_move()
        self.game_data.append(copy.deepcopy(self.board))

        self.trap_position = None
        self.moves += 1
        if self.win == None:
            if not self.moves == 64:
                self.play()
            else:
                self.win = 0
                #self.game_end()
        elif self.win == 1:
            pass
            #self.game_end()
        else:
            pass
            #self.game_end()


    def computer_move(self):
        available_moves = self.check_available_moves(self.board)
        self.move_position = tuple(available_moves[randint(0,len(available_moves)-1)])
        if self.whogoes == 1:
            self.player1move()
        else:
            self.player2move()

    def computer_trap(self):
        available_moves = self.check_available_moves(self.board)
        self.trap_position = tuple(available_moves[randint(0,len(available_moves)-1)])


    def player1move(self):
        '''Performs move of player 1'''
        if self.move_position != self.trap_position:
            self.board[self.move_position[0],self.move_position[1]] = 1
            self.check_win(1,self.move_position)
        else:
            self.board[self.move_position[0],self.move_position[1]] = -1
            self.check_win(2,self.move_position)
        self.whogoes = 2


    def player2move(self):
        '''Performs move of player 2'''
        if self.move_position != self.trap_position:
            self.board[self.move_position[0],self.move_position[1]] = -1
            self.check_win(2,self.move_position)
        else:
            self.board[self.move_position[0],self.move_position[1]] = 1
            self.check_win(1,self.move_position)
        self.whogoes = 1


    def check_win(self,player,position):
        self.check_column_win(player,position)
        if self.win == None:
            self.check_row_win(player,position)
        if self.win == None:
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
    def check_available_moves(board):
        return np.argwhere(board == 0)
