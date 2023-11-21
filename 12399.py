# DSP :

import numpy as np

# Matrix: A, B, C...(3*3)
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[2, 4, 6], [2, 8, 9], [0, 2, 6]])
C = np.array([[7, 4, 8], [2, 9, 6], [8, 6, 0]])

# Print all Matrices
print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
print("Matrix C:")
print(C)

# Addition
print("A + B:")
print(A + B)
print("A + C:")
print(A + C)
print("B + C:")
print(B + C)
print("A + B + C:")
print(A + B + C)

# Subtraction
print("A - B:")
print(A - B)
print("A - C:")
print(A - C)
print("B - C:")
print(B - C)
print("A - B - C:")
print(A - B - C)

# Multiplication
print("A * B:")
print(np.dot(A, B))
print("A * C:")
print(np.dot(A, C))
print("B * C:")
print(np.dot(B, C))
print("A * B * C:")
print(np.dot(np.dot(A, B), C))

# Power
print("A^3:")
print(np.linalg.matrix_power(A, 3))
print("B^2:")
print(np.linalg.matrix_power(B, 2))
print("C^3:")
print(np.linalg.matrix_power(C, 3))
