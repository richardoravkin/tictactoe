import numpy as np
import tkinter
canvas = tkinter.Canvas(width = 801, height = 801)
canvas.pack()
class TicTacToe():
    def __init__(self):
        self.board = np.zeros((8,8))
        self.move_position = None
        self.trap_position = None
        self.whogoes = 1
        self.win = False
    def create_board(self):
        canvas.create_rectangle(0,0,800,800)
        for i in range(1,8):
            canvas.create_line(100*i,0,100*i,800)
            canvas.create_line(0,100*i,800,100*i)
    def start_game(self):
        self.moves_manually()
    def moves_manually(self):
        '''Obtains move information when game is played through string inputs'''
        if self.whogoes == 1:
            self.get_trap_input(2)
            self.get_move_input(1)
            self.player1move()
            self.whogoes = 2
            self.trap_position = None
        else:
            self.get_trap_input(1)
            self.get_move_input(2)
            self.player2move()
            self.whogoes = 1
            self.trap_position = None

        if self.win == 0:
            self.moves_manually()
        elif self.win == 1:
            print('GAME OVER - Player 1 wins')
        else:
            print('GAME OVER - Player 2 wins')

    def get_move_input(self,integer):
        '''Obtains moves via string input'''
        user_input = input('Player '+ str(integer)+ ' input your move: ')
        position = tuple(map(int,user_input.split(',')))
        if self.isempty(self.board,position):
            self.move_position = position
        else:
            print('That square is taken,try again!')
            self.get_move_input(integer)

    def get_trap_input(self,integer):
        '''Obtains traps via string input'''
        user_input = input('Player '+ str(integer)+ ' input your trap: ')
        position = tuple(map(int,user_input.split(',')))
        if self.isempty(self.board,position):
            self.trap_position = position
        else:
            print('That square is taken,try again!')
            self.get_trap_input(integer)


    def player1move(self):
        '''Performs move of player 1'''
        if self.move_position != self.trap_position:
            self.board[self.move_position[0],self.move_position[1]] = 1
            self.draw(1,self.move_position)
            self.check_win(1,self.move_position)

        else:
            self.board[self.move_position[0],self.move_position[1]] = -1
            self.draw(2,self.move_position)
            self.check_win(2,self.move_position)


    def player2move(self):
        '''Performs move of player 2'''
        if self.move_position != self.trap_position:
            self.board[self.move_position[0],self.move_position[1]] = -1
            self.draw(2,self.move_position)
            self.check_win(2,self.move_position)
        else:
            self.board[self.move_position[0],self.move_position[1]] = 1
            self.draw(1,self.move_position)
            self.check_win(1,self.move_position)

    def check_win(self,player,position):
        self.check_column_win(player,position)
        self.check_row_win(player,position)
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

    @staticmethod
    def draw(player,position):
        if player == 1:
            canvas.create_line(position[1]*100,position[0]*100,(1+position[1])*100,(1+position[0])*100, fill = 'blue', width = 4)
            canvas.create_line((1+position[1])*100,position[0]*100,position[1]*100,(1+position[0])*100, fill = 'blue', width = 4)
        else:
            canvas.create_oval(position[1]*100,position[0]*100,(1+position[1])*100,(1+position[0])*100, outline = 'red', width = 4)

game = TicTacToe()
game.create_board()
game.start_game()
