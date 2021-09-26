from fourbyfour import ComputervsComputer
import numpy as np
from math import floor
def generate_data(size):
    positions = [{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}]
    counts = []
    for i in range(size):
        Game = ComputervsComputer(i%2+1)
        Game.play()
        print(Game.board)
        data = Game.game_data
        for j in range(len(data)):
            position = array_to_number(data[j])
            check_list(positions[j],position,Game.win)

    return positions

def array_to_number(position):
    number = 0
    count = 0
    for i in range(4):
        for j in range(4):
            number += position[i][j]*3**(15-count)
            count += 1
    return number

def check_list(dic, position,win):
    keys = list(dic.keys())
    upper = len(keys)
    lower = 0
    init = False
    while upper != lower:
        mid = floor((upper + lower)/2)
        if keys[mid] == position:
            init = True
            if win == 1:
                dic[mid][0] += 1
            elif win == 2:
                dic[mid][1] += 1
            break
        elif keys[mid] > position:
            upper = mid

        else:
            if lower == mid:
                break
            else:
                lower = mid


    if not init:
        if win == 1:
            dic[position] = [1,0]
        elif win == 2:
            dic[position] = [0,1]


print(generate_data(100))
