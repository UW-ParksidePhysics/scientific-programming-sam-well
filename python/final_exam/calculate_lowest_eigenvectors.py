"""
Identify eigenvectors with smallest K eigenvalues given input matrix using
NumPy's eig function
"""

__author__ = "Sam Rodriguez"

import numpy as np


def calculate_lowest_eigenvectors(square_matrix, number_of_eigenvectors=3):
    """
    Identify eigenvectors with smallest K eigenvalues given input matrix using
    NumPy's eig function
    :param square_matrix: ndarray, shape (M, M)
        Matrix to be characterized. Must be a square matrix of M rows and M
        columns where M is >=1.
    :param number_of_eigenvectors: int, optional
       Number of eigenvectors K with eigenvalues to return.  Default is 3.
    :return eigenvalues: ndarray, shape (K,)
        Array of the K lowest-value eigenvalues ordered from lowest to highest.
    :return eigenvectors: ndarray, shape (K,M)
        Array of K eigenvectors with M components arranged in order
        corresponding to their eigenvalues. The first index should correspond
        to the eigenvalue index in the eigenvalues array. The order of the
        components in the eigenvector remains the same as output by NumPy's eig.
    """
    w, v = np.linalg.eig(square_matrix)
    eigenvalues = w[:number_of_eigenvectors]
    eigenvectors = v[:number_of_eigenvectors]
    return eigenvalues, eigenvectors


if __name__ == "__main__":
    square_matrix = np.array([[2, -1], [-1, 2]])
    result = calculate_lowest_eigenvectors(square_matrix, number_of_eigenvectors=2)
    print(result)
