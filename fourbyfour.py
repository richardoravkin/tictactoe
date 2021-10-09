import numpy as np
from random import *
import copy

class ComputervsComputer():
    'Tic tac toe on a 4x4 board'
    def __init__(self,whogoes):
        self.board = np.zeros((4,4), dtype = int)
        self.move_position = None
        self.whogoes = whogoes
        self.win = None
        self.game_data = []
        self.moves = 0
        self.available_moves = []
        for i in range(4):
            for j in range(4):
                self.available_moves.append((i, j))

    def play(self):
        '''Play game and record game data'''
        self.computer_move()
        self.game_data.append(copy.deepcopy(self.board))
        self.moves += 1
        if self.win == None:
            if not self.moves == 16:
                self.play()
            else:
                self.win = 0


    def computer_move(self):
        'Perform move at random'
        move = self.select_available_move(self.available_moves)

        if self.whogoes == 1:
            self.board[move[0],move[1]] = 1
            self.check_win(1,move)
            self.whogoes = 2

        else:
            self.board[move[0],move[1]] = 2
            self.check_win(2,move)
            self.whogoes = 1



    def check_win(self,player,position):
        'Check if a player has won'
        self.check_column_win(player,position)
        if self.win == None:
            self.check_row_win(player,position)
        if self.win == None:
            self.check_diag_win(player,position)

    def check_column_win(self,player,position):
        'Check if 3 consecutive pieces in a column'
        row = position[0]
        col = position[1]
        if player == 1:
            count = 1
            j = 1
            k = 1
            while row + j < 4 and self.board[row + j][col] == 1:
                count += 1
                j += 1
                if count == 3:
                    self.win = 1
                    break
            while row - k > -1 and self.board[row-k][col] == 1:
                count += 1
                k += 1
                if count == 3:
                    self.win = 1
                    break
        if player == 2:
            count = 1
            j = 1
            k = 1
            while row + j < 4 and self.board[row + j][col] == 2:
                count += 1
                j += 1
                if count == 3:
                    self.win = 2
                    break
            while row - k > -1 and self.board[row-k][col] == 2:
                count += 1
                k += 1
                if count == 3:
                    self.win = 2
                    break

    def check_row_win(self,player,position):
        'Check if 3 consecutive pieces in a row'
        row = position[0]
        col = position[1]
        if player == 1:
            count = 1
            j = 1
            k = 1
            while col+ j < 4 and self.board[row][col+j] == 1:
                count += 1
                j += 1
                if count == 3:
                    self.win = 1
                    break
            while col - k > -1 and self.board[row][col-k] == 1:
                count += 1
                k += 1
                if count == 3:
                    self.win = 1
                    break
        if player == 2:
            count = 1
            j = 1
            k = 1
            while col + j < 4 and self.board[row][col+j] == 2:
                count += 1
                j += 1
                if count == 3:
                    self.win = 2
                    break
            while col - k > - 1 and self.board[row][col-k] == 2:
                count += 1
                k += 1
                if count == 3:
                    self.win = 2
                    break

    def check_diag_win(self,player,position):
        'Check if 3 consecutive pieces in a both diagonals'
        row = position[0]
        col = position[1]
        if player == 1:
            count = 1
            j = 1
            k = 1
            while col+ j < 4 and row + j < 4 and self.board[row+j][col+j] == 1:
                count += 1
                j += 1
                if count == 3:
                    self.win = 1
                    break
            while col - k > -1 and row - k > -1 and self.board[row-k][col-k] == 1:
                count += 1
                k += 1
                if count == 3:
                    self.win = 1
                    break
            count = 1
            j = 1
            k = 1
            while col+ j < 4 and row - j > -1 and self.board[row-j][col+j] == 1:
                count += 1
                j += 1
                if count == 3:
                    self.win = 1
                    break
            while col - k > -1 and row +k < 4 and self.board[row+k][col-k] == 1:
                count += 1
                k += 1
                if count == 3:
                    self.win = 1
                    break
        if player == 2:
            count = 1
            j = 1
            k = 1
            while col+ j < 4 and row + j < 4 and self.board[row+j][col+j] == 2:
                count += 1
                j += 1
                if count == 3:
                    self.win = 2
                    break
            while col - k > -1 and row - k > -1 and self.board[row-k][col-k] == 2:
                count += 1
                k += 1
                if count == 3:
                    self.win = 2
                    break
            count = 1
            j = 1
            k = 1
            while col+ j < 4 and row - j > -1 and self.board[row-j][col+j] == 2:
                count += 1
                j += 1
                if count == 3:
                    self.win = 2
                    break
            while col - k > -1 and row +k < 4 and self.board[row+k][col-k] == 2:
                count += 1
                k += 1
                if count == 3:
                    self.win = 2
                    break
    @staticmethod
    def select_available_move(moves):
        'Return available move'
        return moves.pop(randrange(len(moves)))
