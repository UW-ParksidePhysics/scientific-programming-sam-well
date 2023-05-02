"""
Make fit curve using fit polynomial coefficients, NumPy's polynomialLinks to an
external site., and minimum and maximum x-values
"""

__author__ = "Sam Rodriguez"

import numpy as np


def fit_curve_array(quadratic_coefficients,
                    minimum_x,
                    maximum_x,
                    number_of_points=100):
    """
    Make fit curve using fit polynomial coefficients, NumPy's polynomial, and
    minimum and maximum x-values
    :param quadratic_coefficients: ndarray, shape (3,)
        Quadratic polynomial coefficients, ordered constant term first, then
        linear term, and quadratic term last.
    :param minimum_x: float
        Starting value for the fit_curve array.
    :param maximum_x: float
        Ending value for the fit curve array.
    :param number_of_points: int, optional
        Number of points N to return for final fit curve. Default is 100.
    :return fit_curve: ndarray, shape (2, N)
        x-y data created by the coefficients of the fit function. N is the
        number of function evaluation points.
    """

    try:
        x_values = np.linspace(minimum_x, maximum_x, number_of_points)
        y_values = quadratic_coefficients[0] + \
                    quadratic_coefficients[1] * x_values + \
                    quadratic_coefficients[2] * x_values ** 2
        fit_curve = [x_values, y_values]
    except ArithmeticError as error:
        print(f"{error}")
    except IndexError as error:
        print(f"{error}")

    return fit_curve


if __name__ == "__main__":
    array = fit_curve_array([0, 0, 1], -2, 2)
    print(array[1][0] == array[0][0] ** 2)

