import numpy as np
import matplotlib.pyplot as plt

H = 1 / (2 * (1/(5+1))**2)

matrix_dimension = 5
matrix = np.array([[2, -1], [-1, 2]])

twos = np.ones(matrix_dimension) * 2

twos_matrix = np.diagflat(twos)

negative_ones = np.ones(matrix_dimension-1) * -1
upper_negative_ones = np.diagflat(negative_ones, 1)
lower_negative_ones = np.diagflat(negative_ones, -1)

matrix = twos_matrix + upper_negative_ones + lower_negative_ones
print(f'M = {matrix}')

eigenvalues, eigenvectors = np.linalg.eig(H*matrix)
print(f'lambda = {eigenvalues}')
print()
print(f'x = {eigenvectors}')
print()


def sin_function(x):
    return np.sqrt(2)*np.sin(np.pi*x)


x_list = np.linspace(0, 1, 20)
plt.plot(np.linspace(1/(5+1), 5/(5+1), 5),
         eigenvectors[-1],
         x_list,
         sin_function(x_list))
plt.xlim(0, 1)
plt.show()
