import numpy as np

matrix_A = np.array([[1, 2], [3, 4]])
matrix_B = np.array([[2, 1], [1, 0]])
scalar_C = 2

print(f"A + B = {matrix_A + matrix_B}\n")
print(f"A - B = {matrix_A - matrix_B}\n")
print(f"C * A = {scalar_C * matrix_A}\n")
print(f"A * B = {np.dot(matrix_A, matrix_B)}\n")  # or np.matmul(A, B) or A @ B

print(f"{len(matrix_A)} rows in A\n")
print(f"First row in A: {matrix_A[0]}\n")
print(f"Type of A is {type(matrix_A)}\n")
print(f"Last value in first row of A: {matrix_A[0][1]}\n")  # or matrix_A[0, 1]

print(f"shape of A: {np.shape(matrix_A)}\n")

print(f"transpose(A): {matrix_A.transpose()}\n")  # or matrix_A.T
print(f"det(A): {np.linalg.det(matrix_A):.8f}\n")
print(f"A**-1: {np.linalg.inv(matrix_A)}\n")

vector_b = np.array([[1], [1]])
print(f"A^-1.b: {np.linalg.solve(matrix_A, vector_b)}\n")

print((5+np.sqrt(33))/2)
print((5-np.sqrt(33))/2)
print()

eigenvalues, eigenvectors = np.linalg.eig(matrix_A)
print(f"lambda +/- : {eigenvalues}\n")
print(f"x +/- : {eigenvectors}\n")

print(f"norm(b): {np.linalg.norm(vector_b)}\n")