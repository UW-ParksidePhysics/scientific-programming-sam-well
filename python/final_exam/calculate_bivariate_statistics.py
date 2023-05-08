"""
Calculate statistical characteristics of a data set using SciPy's stats.describe function
"""

__author__ = 'Sam Rodriguez'

import scipy as sp
import numpy as np


def calculate_bivariate_statistics(data, axis=1):
    """
    Calculate statistical characteristics of a data set using SciPy's stats.describe function
    :param data: ndarray, shape(2, M)
        x-y data to be characterized. M is the number of data points.
    :return statistics: ndarray, shape(6,)
        mean of y, standard deviation of y, minimum x-value, maximum x-value, minimum y-value, maximum y-value
    """
    # data = read_two_columns_text
    try:
        statistics = sp.stats.describe(data, axis)
        select_statistics = np.array([statistics.mean[1], statistics.variance[1], statistics.minmax[0][0],
                                      statistics.minmax[1][0], statistics.minmax[0][1], statistics.minmax[1][1]])
    except IndexError as error:
        print(f'{error}')
    return select_statistics


if __name__ == "__main__":
    x_s = np.linspace(-10, 10, 21)
    y_s = (x_s ** 2)
    test_array = np.array([x_s, y_s])
    select_statistics = calculate_bivariate_statistics(test_array)
    print(f'test_statistics={select_statistics}')
