from CvsC import ComputervsComputer
import numpy as np
import codecs,json
import os
def generate_data(size):
    X_data = []
    Y_data = []
    for i in range(size):
        Game = ComputervsComputer(i%2+1)
        Game.play()
        #for j in range(len(Game.game_data)):
        X_data.append(Game.game_data[-1])
        Y_data.append(Game.win)
    X_data = np.array(X_data)
    Y_data = np.array(Y_data)
    with open('X_data.npy','wb') as f:
        np.save(f,X_data)
    with open('Y_data.npy','wb') as f:
        np.save(f,Y_data)



generate_data(10000)
