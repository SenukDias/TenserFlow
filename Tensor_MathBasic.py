import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

# Element wise addition
tensA = tf.constant([20,6,7])
tensB = tf.constant([45,7,21])

# Tensor Addition
print("Tensor Addition")
tensC = tf.add(tensA,tensB)
# tensC = tensA + tensB;
print(tensC)

# Tensor Substraction
print("Tensor Substraction")
tensD = tf.subtract(tensA,tensB)
# tensD = tensA - tensB
print(tensD)

# Tensor Divition
print("Tensor Divition")
tensE = tf.divide(tensB,tensA)
# tensE = tensB / tensA
print(tensE)

# Tensor multiplication
print("Tensor Multiplication")
tensF = tf.multiply(tensA,tensB)
print(tensF)

# Tensor Dot Product
import numpy as np

print("Dot Product")
tenA = tf.constant(np.array([[1,2],[3,4]]))
tenB = tf.constant(np.array([[11,12],[13,14]]))

print("Tensor A")
print(tenA)
print("Tensor B")
print(tenB)

print("Dot Product ")
tenC = tf.tensordot(tenA,tenB, axes=1)
print(tenC)