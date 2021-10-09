'NOT WORKING YET!'

import tensorflow as tf
import numpy as np
from keras.layers import Dense
from keras.layers import Dropout
from keras.models import Sequential

X_train = []
Y_train = []
trainingWeights = []
X_test = []
Y_test = []
with open('train_data.txt','r') as f1,open('test_data.txt','r') as f2:
    for line in f1:
        list1 = line.split(':')
        x_data = list(list1[0])
        x_data = list(map(int,x_data))
        y_data = float(list1[2])
        weight = int(list1[3])
        X_train.append(x_data)
        Y_train.append(y_data)
        trainingWeights.append(weight)
    for line in f2:
        list1 = line.split(':')
        x_data = list(list1[0])
        x_data = list(map(int,x_data))
        y_data = float(list1[2])
        X_test.append(x_data)
        Y_test.append(y_data)


class Classifier:
    def __init__(self, numberOfInputs, numberOfOutputs, epochs, batchSize):
        self.epochs = epochs
        self.batchSize = batchSize
        self.numberOfInputs = numberOfInputs
        self.numberOfOutputs = numberOfOutputs
        self.model = Sequential()
        self.model.add(Dense(128, input_shape=(numberOfInputs,)))

        self.model.add(Dense(128, activation='relu'))

        self.model.add(Dense(128, activation='relu'))

        self.model.add(Dense(128, activation='relu'))


        self.model.add(Dense(128, activation='relu'))

        self.model.add(Dense(128, activation='relu'))

        self.model.add(Dense(128, activation='relu'))

        self.model.add(Dense(128, activation='relu'))


        self.model.add(Dense(numberOfOutputs, activation='linear'))
        self.model.compile(loss='mse', optimizer='rmsprop', metrics=['accuracy'])

        #sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
        #model.compile(loss='binary_crossentropy', optimizer=sgd)

    def train(self, X_train,Y_train,X_test,Y_test,trainingWeights):
        X_train = np.array(X_train)
        Y_train = np.array(Y_train)
        trainingWeights = np.array(trainingWeights)
        X_test = np.array(X_test)
        Y_test = np.array(Y_test)

        self.model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=self.epochs, batch_size=self.batchSize, sample_weight = trainingWeights)

NN = Classifier(16,1,32,50)
NN.train(X_train,Y_train,X_test,Y_test,trainingWeights)
