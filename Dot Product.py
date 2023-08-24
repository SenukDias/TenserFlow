import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import numpy as np

Arr1 = [[0,0], [0,0]]

startR = 0
startC = 0;

print("\nDot Product")

Row = int(input("Enter Count of Rows : "))
Column = int(input("Enter Count of Columns : "))

if(Row == 2 and Column == 2):
    while(startR < Row):
        startC = 0
        while(startC < Column):
            Arr1[startR][startC] = int(input("Enter a Number : "))
            startC = startC + 1
        startR += 1
    startR = 0

tenA = tf.constant([[Arr1[0][0],Arr1[0][1]],[Arr1[1][0],Arr1[1][1]]],shape=(2,2))
print("Check")

Row = int(input("Enter Count of Rows : "))
Column = int(input("Enter Count of Columns : "))

if(Row == 2 and Column == 2):
    while(startR < Row):
        startC = 0
        while(startC < Column):
            Arr1[startR][startC] = int(input("Enter a Number : "))
            startC = startC + 1

        startR += 1

tenB = tf.constant([[Arr1[0][0],Arr1[0][1]],[Arr1[1][0],Arr1[1][1]]],shape=(2,2))
print("Check\n")

print("Tensor A")
print(tenA)
print("Tensor B")
print(tenB)

print("Dot Product of Tensor A and B")
tenC = tf.tensordot(tenA,tenB, axes=1)
print(tenC)