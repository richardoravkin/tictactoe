from fourbyfour import ComputervsComputer
import numpy as np
from math import floor
def generate_data(size):
    positions = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    values = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    counts = []
    for i in range(size):
        Game = ComputervsComputer(i%2+1)
        Game.play()
        data = Game.game_data
        for j in range(len(data)):
            position = array_to_number(data[j])
            if Game.win != 0:
                check_list(positions[j],values[j],position,Game.win)

    return positions,values

def array_to_number(position):
    number = 0
    count = 0
    number = ''.join(map(str, position.flatten()))
    return int(number)

def check_list(keys, values, position,win):
    upper = len(keys)
    lower = 0
    init = False
    mid = 0
    while upper != lower:
        mid = floor((upper + lower)/2)
        if keys[mid] == position:
            init = True
            if win == 1:
                values[mid][0] += 1
            elif win == 2:
                values[mid][1] += 1
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
            value = [1,0]
        elif win == 2:
            value = [0,1]
        if len(keys) == 0 or keys[mid] > position:
            index = mid
        elif keys[mid] < position:
            index = mid + 1

        values.insert(index,value)
        keys.insert(index,position)


positions,values = generate_data(int(1e5))
def write(positions,values):
    with open("train_data.txt", "w") as text_file1, open('test_data.txt','w') as text_file2:
        for i in range(len(positions)):
            length = len(positions[i])
            for j in range(int(length*0.8)):
                variable = 16 - len(str(positions[i][j]))
                string = variable*'0'
                value1 = values[i][j][0]
                value2 = values[i][j][1]
                weight = set_weights(value1,value2)
                text_file1.write(string + str(positions[i][j])+ ':' + str([value1,value2])+':'+str((value1-value2)/(value1+value2))+':'+str(weight)+'\n')
            for k in range(int(length*0.8),length):
                variable = 16 - len(str(positions[i][k]))
                string = variable*'0'
                value1 = values[i][k][0]
                value2 = values[i][k][1]
                weight = set_weights(value1,value2)
                text_file2.write(string + str(positions[i][k])+ ':' + str([value1,value2])+':'+str((value1-value2)/(value1+value2))+':'+str(weight)+'\n')

def set_weights(value1,value2,z = 1.645):
    n = value1 + value2
    div = n//5 + 1
    if div > 6:
        upper = n*1/2 + z*(n*1/2*1/2)**1/2
        lower = n*1/2 - z*(n*1/2*1/2)**1/2
        if upper < value1 or lower > value1 or upper < value2 or lower > value2:
            weight = 10
        else:
            weight = 5
    elif div >= 3:
        upper = n*1/2 + z*(n*1/2*1/2)**1/2
        lower = n*1/2 - z*(n*1/2*1/2)**1/2
        if upper < value1 or lower > value1 or upper < value2 or lower > value2:
            weight = 10
        else:
            weight = div
    else:
        weight = div
    return weight
write(positions,values)
