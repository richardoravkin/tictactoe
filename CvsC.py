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
        self.available_moves = []
        for i in range(8):
            for j in range(8):
                self.available_moves.append((i, j))

    def play(self):
        '''Plays game of tic tac toe with itself'''
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

        elif self.win == 1:
            pass

        else:
            pass



    def computer_move(self):
        'Selects move from available squares at random'
        available_moves = self.select_available_move(self.available_moves)
        self.move_position = tuple(available_moves[randint(0,len(available_moves)-1)])
        if self.whogoes == 1:
            self.player1move()
        else:
            self.player2move()

    def computer_trap(self):
        'Selects trap from available squares at random'
        available_moves = self.select_available_move(self.available_moves)
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
        'Check if a player won the game'
        self.check_column_win(player,position)
        if self.win == None:
            self.check_row_win(player,position)
        if self.win == None:
            self.check_diag_win(player,position)

    def check_column_win(self,player,position):
        'Checks if a player has 5 consecutive pieces in a column'
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
        'Checks if a player has 5 consecutive pieces in a row'
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
        'Checks if a player has 5 consecutive pieces in both diagonals'
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
    def select_available_move(moves):
        'Return a an available square'
        return moves.pop(random.randrange(len(moves)))
