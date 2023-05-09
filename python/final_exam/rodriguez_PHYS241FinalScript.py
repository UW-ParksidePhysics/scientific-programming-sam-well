"""
Harmonic, 110, 300
0, 1, 2
"""

__author__ = 'Sam Rodriguez'
__equation_of_state__ = 'murnaghan'

display_graph = True


import scipy as sp
from read_two_columns_text import *
from calculate_bivariate_statistics import *
from calculate_quadratic_fit import *
from equations_of_state import *
from fit_curve_array import *
import matplotlib.pylab as plt
import numpy as np
from annotate_plot import *
from datetime import datetime


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


def convert_units(value, current_unit, expected_unit):
    """
    Converts value from current unit to an expected unit.
    :param value: float
    :param current_unit: str
        Expects 'bohr/atom', 'rydberg/atom', or 'rydberg/bohr**3'
    :param expected_unit: str
        Expects 'angstrom**3/atom', 'eV/atom', 'gigapascals'
    :return: converted_value: float
    """
    return_value = None
    if current_unit == 'bohr/atom' and expected_unit == 'angstrom**3/atom':
        # m/bohr
        bohr_radius = sp.constants.physical_constants['Bohr radius'][0]
        # m/angstrom
        angstrom = sp.constants.angstrom
        return_value = (value * bohr_radius**3) / angstrom**3
    elif current_unit == 'rydberg/atom' and expected_unit == 'eV/atom':
        rydberg_conversion = sp.constants.physical_constants[
            'Rydberg constant times hc in eV'][0]
        return_value = value * rydberg_conversion
    elif current_unit == 'rydberg/bohr**3' and expected_unit == 'gigapascals':
        bohr_radius = sp.constants.physical_constants['Bohr radius'][0]
        rydberg_conversion = sp.constants.physical_constants[
            'Rydberg constant times hc in J'][0]
        return_value = ((value * rydberg_conversion) / bohr_radius**3) * 10**-9

    return return_value


if __name__ == '__main__':
    filename = 'Au.Fm-3m.GGA-PBEsol.volumes_energies.dat'
    chemical_symbol, crystal_symmetry_symbol, density_approx_acronym = \
        parse_file_name(filename)

    data = read_two_columns_text(filename)  # volumes/atom, energy/atom
    updated_data = None
    match crystal_symmetry_symbol:
        case 'Fm-3m':
            updated_data = data / 1
        case 'Fd-3m':
            updated_data = data / 2

    stats = calculate_bivariate_statistics(updated_data)
    quadratic_coeffs = calculate_quadratic_fit(updated_data)

    # FIX ME!!!!!
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
        'position': np.array([0, 0]),
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
        'position': np.array([0.6, 0.2]),
        'alignment': ['left', 'bottom'],
        'fontsize': 10
    })

    plt.subplots_adjust(bottom=0.2)
    plt.title(f"{__equation_of_state__.capitalize()} Equation of State for "
              f"{chemical_symbol} in DFT {density_approx_acronym}")
    match display_graph:
        case True:
            plt.show()
        case False:
            plt.savefig(f"{__author__.split()[1]}.{chemical_symbol}."
                        f"{crystal_symmetry_symbol}."
                        f"{density_approx_acronym}."
                        f"{__equation_of_state__.capitalize()}"
                        f".EquationOfState.png")
