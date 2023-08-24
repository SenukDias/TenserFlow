import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist

(x_train , y_train) , (x_test , y_test) = mnist.load_data()

print(x_train.shape)
print(y_train.shape)

x_train = x_train.reshape(-1,28 * 28).astype("float32")/255.0
x_test = x_test.reshape(-1,28 * 28).astype("float32")/255.0

def createModel():
    model = keras.Sequential()
    model.add(keras.Input(shape=28*28))
    model.add(layers.Dense(512,activation='relu'))
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(10))
    return model

myModel = createModel()
print(myModel.summary())

myModel.compile(
    loss = keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    metrics=["accuracy"],
)

myModel.fit(x_train, y_train, batch_size=32, epochs=5, verbose=2)
myModel.evaluate(x_test, y_test, batch_size=32, verbose=2)