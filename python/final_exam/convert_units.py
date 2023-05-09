import scipy as sp


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
        return_value = (value * bohr_radius ** 3) / angstrom ** 3
    elif current_unit == 'rydberg/atom' and expected_unit == 'eV/atom':
        rydberg_conversion = sp.constants.physical_constants[
            'Rydberg constant times hc in eV'][0]
        return_value = value * rydberg_conversion
    elif current_unit == 'rydberg/bohr**3' and expected_unit == 'gigapascals':
        bohr_radius = sp.constants.physical_constants['Bohr radius'][0]
        rydberg_conversion = sp.constants.physical_constants[
            'Rydberg constant times hc in J'][0]
        return_value = ((value * rydberg_conversion) / bohr_radius ** 3) * 10 ** -9

    return return_value
