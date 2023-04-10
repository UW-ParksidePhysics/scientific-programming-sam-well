import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

matrix_dimension = 2
matrix = np.array([[2, -1], [-1, 2]])
print(f'A = {matrix}')

twos = np.ones(matrix_dimension) * 2
print(f'T-array = {twos}')

twos_matrix = np.diagflat(twos)
print(f'T-matrix = {twos_matrix}')

negative_ones = np.ones(1) * -1
print(f'N-array = {negative_ones}')

upper_negative_ones = np.diagflat(negative_ones, 1)
print(f'N-upper = {upper_negative_ones}')
lower_negative_ones = np.diagflat(negative_ones, -1)
print(f'N-lower = {lower_negative_ones}')

matrix = twos_matrix + upper_negative_ones + lower_negative_ones
print(f'M = {matrix}')

eigenvalues, eigenvectors = np.linalg.eig(matrix)
print(f'lambda = {eigenvalues}')
print()
print(f'x = {eigenvectors}')
print()
