"""
Murnaghan
Harmonic, 110, 300
0, 1, 2
"""

import scipy as sp
from read_two_columns_text import *
from calculate_bivariate_statistics import *
from calculate_quadratic_fit import *
from equations_of_state import *


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
    eos_fit = fit_eos(
        updated_data[0], updated_data[1], quadratic_coeffs,
        eos='murnaghan', number_of_points=110)
    # print(eos_fit_curve)
    # print(eos_parameters)
    convert_units(updated_data[0], 'bohr/atom', 'angstrom**3/atom')
    convert_units(eos_fit_curve, 'rydberg/atom', 'eV/atom')
    print(
       updated_data[0]
    )
    print(
        eos_fit_curve
    )
    convert_units(updated_data[1], 'rydberg/bohr**3', 'gigapascals')




