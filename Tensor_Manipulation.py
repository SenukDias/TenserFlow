import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf

X = tf.constant([0,10,15,20,30,10,20,30])

print("Printing Tensor")
print(X)

print("X[:]")
print(X[:])

# Starting from 3rd value
print("X[2:]")
print(X[2:])

# Ending with 5th value
print("X[:4]")
print(X[:4])

# Skipping one
print("X[::2]")
print(X[::2])

# Skipping Two
print("X[::3]")
print(X[::3])

# Reverse
print("X[::-1]")
print(X[::-1])

print("Indiced")
indices_Indexes = tf.constant([0,3])
indexedTensor = tf.gather(X, indices=indices_Indexes)
print(indexedTensor)

TensorA = tf.constant([[10,20],[30,40],[50,60],[70,80]])
print(TensorA)
# Get first row with all elements
