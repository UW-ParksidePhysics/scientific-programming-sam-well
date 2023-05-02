"""
Create a combined scatter and curve plot for the data and the fit polynomial,
respectively, using Pyplot's plot function
"""

__author__ = "Sam Rodriguez"

import matplotlib.pyplot as plt
import numpy as np


def plot_data_with_fit(data,
                       fit_curve,
                       data_format='o',
                       fit_format=''):
    """
    Create a combined scatter and curve plot for the data and the fit
    polynomial, respectively, using Pyplot's plot function
    :param data: ndarray, shap (2, M)
        x-y data that was fit. M is the number of data points.
    :param fit_curve: ndarray, shape (2, N)
        x-y data created by the coeffecients of the fit function. N is the
        number of function evaluation points (usually much greater than M).
    :param data_format: str, optional
        Optional formatting specification for the style of the scatter plot data
        points.  Default is 'o'.  See Pyplot's plot for specifications. (Use
        Pyplot's plot, not scatter for this.)
    :param fit_format: str, optional
        Optional formatting specification for the curve of the fit function.
        Default is '' (empty string). See Pyplot's plot for specifications.
    :return combined_plot: Pyplot return list
        A list of Line2D objects representing the plotted data. This is the
        default return type from Pyplot's plot.
    """
    # Insert code here
    combined_plot = plt.plot(data[0], data[1], data_format, fit_curve[0], fit_curve[1], fit_format)
    return combined_plot


if __name__ == "__main__":
    data = np.array([[-2, -1, 0, 1, 2], [4, 1, 0, 1, 4]])
    fit_curve = np.array([np.linspace(-2, 2), np.linspace(-2, 2) ** 2])
    plot_data_with_fit(data, fit_curve, data_format='x', fit_format='--')
    plt.show()
