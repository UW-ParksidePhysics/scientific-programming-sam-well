"""
Fit a quadratic polynomial to a two row NumPy array of x-y data using NumPy's
polynomialLinks to an external site. class polyfit() method
"""

__author__ = "Sam Rodriguez"

import numpy as np


def calculate_quadratic_fit(data):
    """
    Fit a quadratic polynomial to a two row NumPy array of x-y data using
    NumPy's polynomial class polyfit() method
    :param data: ndarray, shape (2, M)
        x-y data to be fit. M is the number of data points.
    :return quadratic_coefficients: ndarray, shape (3,)
        Quadratic polynomial coefficients, ordered constant term first, then
        linear term, and quadratic term last.
    """
    quadratic_coefficients = np.polyfit(data[0], data[1], 2)
    return np.flip(quadratic_coefficients)


if __name__ == "__main__":
    pass_data = calculate_quadratic_fit([np.linspace(-1, 1), np.linspace(-1, 1) ** 2])
    print(pass_data)
