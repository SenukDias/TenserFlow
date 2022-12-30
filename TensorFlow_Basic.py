import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

print(tf.__version__)

# Tensor
tensorA = tf.constant(8) # INT Tensor
print(tensorA)

tensorA = tf.constant(8.0) # FLOAT Tensor
print(tensorA)

# dtype [Data Type]
tensorC = tf.constant(8 ,shape=(1,1), dtype=float)
print(tensorC)

# Shape
tensorB = tf.constant([[10,20,30],[40,50,60]],shape=(3,2))
print(tensorB)

# Matrix
tensorD = tf.ones((3,3))
print(tensorD)

tensorD = tf.zeros((4,3))
print(tensorD)

# identity matrix
tensorD = tf.eye(5)
print(tensorD)

# Normal Distribution
DisA = tf.random.normal((4,4),mean=0,stddev=1)
print("Normal Distribution")
print(DisA)

# Uniform Distribution
DisB = tf.random.uniform((1,5),minval=0,maxval=2)
print("Uniform Distribution")
print(DisB)

# Range Function
X = tf.range(start=5, limit=20, delta=3)
print("Range Function")
print(X)

# Casting
y = tf.cast(X, dtype=tf.float64)
print("Casting")
print(y)

