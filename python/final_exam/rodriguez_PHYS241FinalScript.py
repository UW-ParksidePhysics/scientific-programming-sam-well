"""
This script:
    1. Reads in the data set given, fits the functional form given, and produces a plot of data points in a scatter
    plot against the fit curve; and
    2. Takes the matrix given and plots the lowest three eigenvectors against a grid of points in space.
"""

from read_two_columns_text import *
from calculate_bivariate_statistics import *
from convert_units import *
from calculate_quadratic_fit import *
from equations_of_state import *
from fit_curve_array import *
from generate_matrix import *
import matplotlib.pylab as plt
import numpy as np
from annotate_plot import *
from datetime import datetime
from calculate_lowest_eigenvectors import *

__author__ = 'Sam Rodriguez'
__filename__ = 'Au.Fm-3m.GGA-PBEsol.volumes_energies.dat'
__equation_of_state__ = 'murnaghan'  # lowercase
__potential__ = 'harmonic'  # lowercase
__Ndim__ = 110
__parameter__ = 300
__eigenfunctions__ = (0, 1, 2)

display_graph = True
# "Created by" labels may look misaligned in plot view, but they are aligned correctly in the PNGs


def parse_file_name(filename):
    """
    Extracts and returns the chemical symbol, crystal symmetry symbol, density
    functional exchange-correlation approximation acronym from a given data
    file's name. And returns these three strings from the file name.
    :param filename: str
    :return: chemical_symbol: str
    :return: crystal_symmetry_symbol: str
    :return: density_approx_acronym: str
    """
    filename_values = filename.split('.')
    chemical_symbol = filename_values[0]
    crystal_symmetry_symbol = filename_values[1]
    density_approx_acronym = filename_values[2]
    return chemical_symbol, crystal_symmetry_symbol, density_approx_acronym


if __name__ == '__main__':
    chemical_symbol, crystal_symmetry_symbol, density_approx_acronym = \
        parse_file_name(__filename__)

    data = read_two_columns_text(__filename__)  # volumes/atom, energy/atom
    updated_data = None
    if crystal_symmetry_symbol == 'Fm-3m':
        updated_data = data / 1
    elif crystal_symmetry_symbol == 'Fd-3m':
        updated_data = data / 2

    stats = calculate_bivariate_statistics(updated_data)
    quadratic_coeffs = calculate_quadratic_fit(updated_data)

    y_fit_curve, eos_parameters = fit_eos(
        updated_data[0], updated_data[1], quadratic_coeffs,
        eos=__equation_of_state__)
    x_fit_curve = fit_curve_array(quadratic_coeffs, stats[2], stats[3],
                                  number_of_points=50)
    volume_list1 = [convert_units(volume, 'bohr/atom', 'angstrom**3/atom')
                    for volume in x_fit_curve[0]]
    energy_list1 = [convert_units(energy, 'rydberg/atom', 'eV/atom')
                    for energy in x_fit_curve[1]]
    bulk_modulus = convert_units(eos_parameters[1], 'rydberg/bohr**3',
                                 'gigapascals')

    volume_list2 = [convert_units(volume, 'bohr/atom', 'angstrom**3/atom')
                    for volume in updated_data[0]]
    energy_list2 = [convert_units(energy, 'rydberg/atom', 'eV/atom')
                    for energy in updated_data[1]]

    plt.plot(volume_list1, energy_list1, 'black')
    plt.plot(volume_list2, energy_list2, 'bo')

    x_range = max(volume_list1) - min(volume_list1)
    y_range = max(energy_list1) - min(energy_list1)
    x_limits = [min(volume_list1) - (0.1 * x_range),
                max(volume_list1) + (0.1 * x_range)]
    y_limits = [min(energy_list1) - (0.1 * y_range),
                max(energy_list1) + (0.1 * y_range)]
    plt.xlim(x_limits[0], x_limits[1])
    plt.ylim(y_limits[0], y_limits[1])
    plt.xlabel(r'$V\/(\mathrm{Å^3/atom})$')
    plt.ylabel(r'$E\/(\mathrm{eV/atom})$')
    annotate_plot({
        'string': f"Created by {__author__} {datetime.today().isoformat()}",
        'position': np.array([0.05, 0.05]),
        'alignment': ['left', 'bottom'],
        'fontsize': 10
    })

    crystal_symmetry_symbol_plot = None
    if crystal_symmetry_symbol == 'Fm-3m':
        crystal_symmetry_symbol_plot = r"$Fm\overline{3}m$"
    else:
        crystal_symmetry_symbol_plot = r"$Fd\overline{3}m$"
    annotate_plot({
        'string': f"{crystal_symmetry_symbol_plot}",
        'position': np.array([0.5, 0.5]),
        'alignment': ['left', 'bottom'],
        'fontsize': 10
    })

    annotate_plot({
        'string': f"$K_0 = {bulk_modulus:.1f}\/$GPa",
        'position': np.array([0.5, 0.55]),
        'alignment': ['left', 'bottom'],
        'fontsize': 10
    })

    x_list = [volume_list1[energy_list1.index(min(energy_list1))],
              volume_list1[energy_list1.index(min(energy_list1))]]
    y_list = [min(energy_list1), y_limits[0]]
    vertical_line_y_max = min(energy_list1) - y_limits[0]
    plt.plot(x_list,
             y_list,
             'k--')
    annotate_plot({
        'string': f"$V_0 = {eos_parameters[3]:.2f}\/$GPa",
        'position': np.array([0.6, 0.25]),
        'alignment': ['left', 'bottom'],
        'fontsize': 10
    })

    plt.subplots_adjust(bottom=0.25)
    plt.title(f"{__equation_of_state__.capitalize()} Equation of State for "
              f"{chemical_symbol} in DFT {density_approx_acronym}",
              y=1.1)
    if display_graph is True:
        plt.show()
    else:
        plt.savefig(f"{__author__.split()[1]}.{chemical_symbol}."
                    f"{crystal_symmetry_symbol}."
                    f"{density_approx_acronym}."
                    f"{__equation_of_state__.capitalize()}"
                    f".EquationOfState.png")

    # Visualize Vectors in Space
    plt.clf()

    matrix = generate_matrix(
        min(volume_list1), max(volume_list1), __Ndim__, __potential__, __parameter__)
    eigenvalues, eigenvectors = calculate_lowest_eigenvectors(matrix)
    grid = np.linspace(-10, 10, __Ndim__)
    if __eigenfunctions__[0] in eigenvectors:
        index = np.where(eigenvectors == __eigenfunctions__[0])[0]
        eigenvectors[index] = abs(eigenvectors[index])
    plt.plot(grid, eigenvectors[0], 'b-')
    plt.plot(grid, eigenvectors[1], 'g-')
    plt.plot(grid, eigenvectors[2], 'r-')
    plt.axhline(0, color='black')

    maximum_eigenvector = max([max(abs(eigenvectors[0])), max(abs(eigenvectors[1])), max(abs(eigenvectors[2]))])
    plt.ylim(-2*maximum_eigenvector, 2*maximum_eigenvector)

    plt.xlabel(r"$x\/$[a.u.]")
    plt.ylabel(r"$\psi_n (x)\/$[a.u.]")
    plt.legend([fr"$\psi_1,\/E_1\/=\/{eigenvalues[0]:.3f}\/$a.u.",
                fr"$\psi_2,\/E_2\/=\/{eigenvalues[1]:.3f}\/$a.u.",
                fr"$\psi_3,\/E_3\/=\/{eigenvalues[2]:.3f}\/$a.u."])

    annotate_plot({
        'string': f"Created by {__author__} {datetime.today().isoformat()}",
        'position': np.array([0.05, 0.05]),
        'alignment': ['left', 'bottom'],
        'fontsize': 10
    })
    plt.title(f"Select Wavefunctions for a {__potential__.capitalize()} Potential\n"
              f"on a Spatial Grid of {__Ndim__} Points")
    if display_graph is True:
        plt.show()
    else:
        plt.savefig(f"{__author__.split()[1]}.{__potential__.capitalize()}."
                    f"{__eigenfunctions__}.png")

