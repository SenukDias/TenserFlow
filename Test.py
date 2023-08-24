import tensorflow as tf

# Create two constant matrices
matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.],[2.]])

# Perform matrix multiplication
product = tf.matmul(matrix1, matrix2)

# Initialize the session
sess = tf.compat.v1.Session()

# Print the result
print(sess.run(product))

# Close the session
sess.close()
