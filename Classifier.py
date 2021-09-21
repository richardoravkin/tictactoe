import tensorflow as tf
import numpy as np
from keras.layers import Dense
from keras.layers import Dropout
from keras.models import Sequential
with open('X_data.npy','rb') as f:
    X_data = np.load(f)
with open('Y_data.npy','rb') as f:
    Y_data = np.load(f)

print(len(X_data))


class Classifier:
    def __init__(self, numberOfInputs, numberOfOutputs, epochs, batchSize):
        self.epochs = epochs
        self.batchSize = batchSize
        self.numberOfInputs = numberOfInputs
        self.numberOfOutputs = numberOfOutputs
        self.model = Sequential()
        self.model.add(Dense(256, activation='relu', input_shape=(numberOfInputs, )))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(numberOfOutputs, activation='softmax'))
        self.model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    def train(self, X_data,Y_data):
        input = []

        for data in X_data:
            input.append(data.flatten())


        X = np.array(input).reshape((-1, self.numberOfInputs))
        y = tf.keras.utils.to_categorical(Y_data,num_classes = 3)
        # Train and test data split
        boundary = int(0.8 * len(X))
        X_train = X[:boundary]
        X_test = X[boundary:]
        y_train = y[:boundary]
        y_test = y[boundary:]

        self.model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=self.epochs, batch_size=self.batchSize)



NN = Classifier(64,3,32,10)
NN.train(X_data,Y_data)
