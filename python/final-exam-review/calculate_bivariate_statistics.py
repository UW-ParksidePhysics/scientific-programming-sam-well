"""
Calculate statistical characteristics of a data set using SciPy's stats.describe function
"""

__author__ = 'Sam Rodriguez'

import scipy as sp
import numpy as np


def calculate_bivariate_statistics(data):
    """
    Calculate statistical characteristics of a data set using SciPy's stats.describe function
    :param data: ndarray, shape(2, M)
        x-y data to be characterized. M is the number of data points.
    :return statistics: ndarray, shape(6,)
        mean of y, standard deviation of y, minimum x-value, maximum x-value, minimum y-value, maximum y-value
    """
    # data = read_two_columns_text
    try:
        statistics = sp.stats.describe(data)
    except IndexError as error:
        print(f'{error}')
    return statistics


if __name__ == "__main__":
    test_array = np.linspace(-10, 10, 21)
    test_array = test_array ** 2
    statistics = calculate_bivariate_statistics(test_array)
    print(f'test_statistics={statistics}')
