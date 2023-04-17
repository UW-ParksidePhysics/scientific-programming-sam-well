"""
The following code attempts to find the equilibrium position of preset particles
given that the user selects three and inputs an initial position, velocity,
and acceleration.
"""

import matplotlib.pyplot as plt
import numpy as np

# value lists

initial_velocity_magnitude_list = []
initial_acceleration_list = []
initial_position_list = []

# ion values
# mass in kg
# charge in Coulombs

ions = {'hydrogen': {'mass': 1.67e-27, 'charge': 1.6e-19},
        'oxygen': {'mass': 2.66e-26, 'charge': -3.2e-19},
        'chlorine': {'mass': 5.89e-26, 'charge': -1.6e-19},
        'lithium': {'mass': 1.15e-26, 'charge': 1.6e-19},
        'aluminum': {'mass': 4.48e-26, 'charge': 4.8e-19},
        'silver': {'mass': 1.79e-25, 'charge': 1.6e-19},
        'gold': {'mass': 3.27e-25, 'charge': 4.8e-19},
        'fluorine': {'mass': 3.16e-26, 'charge': -1.6e-19},
        'sodium': {'mass': 3.82e-26, 'charge': 1.6e-19},
        'magnesium': {'mass': 4.04e-26, 'charge': 3.2e-19},
        'calcium': {'mass': 6.66e-26, 'charge': 3.2e-19},
        'nitrogen': {'mass': 2.33e-26, 'charge': -4.8e-19},
        'sulfur': {'mass': 5.32e-26, 'charge': -3.2e-19}}

"""
Preset mass values found by using mass values from https://ptable.com/?lang=en#Properties 
and converting them with personal calculation. Preset charge values found by multiplying
most common charge of each element by 1.6x10^-19 as found on 
https://study.com/skill/learn/how-to-calculate-the-total-charge-in-coulombs-of-an-ion-explanation.html#:~:
text=To%20convert%20this%20to%20coulombs,of%20the%20charge%20in%20coulombs.
"""


# calling a dictionary item: ions['name']['property]

# needed functions for matrix_operations
# converts inputs to floats
def tuple_to_float(value):
    value_tuple = value
    value_i_list = list(value_tuple)
    value_f_list = []
    for item in value_i_list:
        value_f_list.append(float(item))
    return value_f_list


# converts inputted velocity value into single magnitude vector
def calc_velocity_magnitude(velocity_x, velocity_y):
    velocity_magnitude = np.sqrt((velocity_x ** 2) + (velocity_y ** 2))
    return velocity_magnitude


# main function for simulation
# all x and y positions in m
# all accelerations in m/s^2
# all velocities in m/s
def matrix_operations(name_ion_1, name_ion_2, name_ion_3, initial_position_values, initial_velocity_values, ):
    def calc_position_eq(acceleration, time, initial_velocity, initial_position):
        current_position = (0.5 * acceleration * (time ** 2)) + (initial_velocity * time) + initial_position
        return current_position

    def calc_matrix_eq(mass, charge_1, charge_2, magnitude, position_change, k=8.987e+9):
        matrix_equation = (k / mass) \
                          * ((charge_1 * charge_2) / (magnitude ** 3)
                             * position_change)
        return matrix_equation

    def calc_magnitude(position_list_1, position_list_2):
        displacement_vector_x = position_list_2[0] - position_list_1[0]
        displacement_vector_y = position_list_2[1] - position_list_1[1]
        magnitude = np.sqrt((displacement_vector_x ** 2) + (displacement_vector_y ** 2))
        return magnitude

    def calc_magnitude_post_matrix(x_val_1, x_val_2, y_val_1, y_val_2):
        displacement_vector_x = x_val_2 - x_val_1
        displacement_vector_y = y_val_2 - y_val_1
        post_matrix_magnitude = np.sqrt((displacement_vector_x ** 2) + (displacement_vector_y ** 2))
        return post_matrix_magnitude

    def calc_position_difference(position_1, position_2):
        pos_diff = position_1 - position_2
        return pos_diff

    def calc_new_acceleration(force, mass):
        acceleration = force / mass
        return acceleration

    # while loop (final)
    # condition? (final)

    # define current values (final)

    # matrix magnitudes
    magnitude_1_2 = calc_magnitude(initial_position_values[0], initial_position_values[1])
    magnitude_1_3 = calc_magnitude(initial_position_values[0], initial_position_values[2])
    magnitude_2_3 = calc_magnitude(initial_position_values[1], initial_position_values[2])

    # matrix position changes
    d_position_x_1_2 = calc_position_difference(initial_position_values[0][0], initial_position_values[1][0])
    d_position_y_1_2 = calc_position_difference(initial_position_values[0][1], initial_position_values[1][1])
    d_position_x_1_3 = calc_position_difference(initial_position_values[0][0], initial_position_values[2][0])
    d_position_y_1_3 = calc_position_difference(initial_position_values[0][1], initial_position_values[2][1])
    d_position_x_2_3 = calc_position_difference(initial_position_values[1][0], initial_position_values[2][0])
    d_position_y_2_3 = calc_position_difference(initial_position_values[1][1], initial_position_values[2][1])

    # particle 1
    # matrix equations
    x_1_2 = calc_matrix_eq(ions[name_ion_1]['mass'], ions[name_ion_1]['charge'], ions[name_ion_2]['charge'],
                           magnitude_1_2, d_position_x_1_2)
    y_1_2 = calc_matrix_eq(ions[name_ion_1]['mass'], ions[name_ion_1]['charge'], ions[name_ion_2]['charge'],
                           magnitude_1_2, d_position_y_1_2)

    x_1_3 = calc_matrix_eq(ions[name_ion_1]['mass'], ions[name_ion_1]['charge'], ions[name_ion_3]['charge'],
                           magnitude_1_3, d_position_x_1_3)
    y_1_3 = calc_matrix_eq(ions[name_ion_1]['mass'], ions[name_ion_1]['charge'], ions[name_ion_2]['charge'],
                           magnitude_1_3, d_position_y_1_3)

    # particle 2
    # matrix equations
    x_2_1 = calc_matrix_eq(ions[name_ion_2]['mass'], ions[name_ion_2]['charge'], ions[name_ion_1]['charge'],
                           magnitude_1_2, d_position_x_1_2)
    y_2_1 = calc_matrix_eq(ions[name_ion_2]['mass'], ions[name_ion_2]['charge'], ions[name_ion_1]['charge'],
                           magnitude_1_2, d_position_y_1_2)

    x_2_3 = calc_matrix_eq(ions[name_ion_2]['mass'], ions[name_ion_2]['charge'], ions[name_ion_3]['charge'],
                           magnitude_2_3, d_position_x_2_3)
    y_2_3 = calc_matrix_eq(ions[name_ion_2]['mass'], ions[name_ion_2]['charge'], ions[name_ion_3]['charge'],
                           magnitude_2_3, d_position_y_2_3)

    # particle 3
    # matrix equations
    x_3_1 = calc_matrix_eq(ions[name_ion_3]['mass'], ions[name_ion_3]['charge'], ions[name_ion_1]['charge'],
                           magnitude_1_2, d_position_x_1_2)
    y_3_1 = calc_matrix_eq(ions[name_ion_3]['mass'], ions[name_ion_3]['charge'], ions[name_ion_1]['charge'],
                           magnitude_1_2, d_position_y_1_2)

    x_3_2 = calc_matrix_eq(ions[name_ion_3]['mass'], ions[name_ion_3]['charge'], ions[name_ion_2]['charge'],
                           magnitude_2_3, d_position_x_2_3)
    y_3_2 = calc_matrix_eq(ions[name_ion_3]['mass'], ions[name_ion_3]['charge'], ions[name_ion_2]['charge'],
                           magnitude_2_3, d_position_y_2_3)

    ion_matrix = np.array([
        [x_1_2, y_1_2, 0, 0, 0, 0],
        [x_1_3, y_1_3, 0, 0, 0, 0],
        [x_2_1, y_2_1, 0, 0, 0, 0],
        [x_2_3, y_2_3, 0, 0, 0, 0],
        [x_3_1, y_3_1, 0, 0, 0, 0],
        [x_3_2, y_3_2, 0, 0, 0, 0]
    ])

    # why is determinant always 0? does matrix need to be reshaped?
    determinant = np.linalg.det(ion_matrix)

    # if greater than previous: (final)
    # do this to new values (final)

    # building new values for when loop added
    force_1 = calc_magnitude_post_matrix(x_1_2, x_1_3, y_1_2, y_1_3)
    force_2 = calc_magnitude_post_matrix(x_2_1, x_2_3, y_2_1, y_2_3)
    force_3 = calc_magnitude_post_matrix(x_3_1, x_3_2, y_3_1, y_3_2)

    acceleration_1 = calc_new_acceleration(force_1, ions[name_ion_1]['mass'])
    acceleration_2 = calc_new_acceleration(force_2, ions[name_ion_2]['mass'])
    acceleration_3 = calc_new_acceleration(force_3, ions[name_ion_3]['mass'])

    particle_1_position_array = ([])
    position_1_x = calc_position_eq(acceleration_1, 1, initial_velocity_values[0], initial_position_values[0][0])
    particle_1_position_array = np.append(particle_1_position_array, position_1_x)
    position_1_y = calc_position_eq(acceleration_1, 1, initial_velocity_values[0], initial_position_values[0][1])
    particle_1_position_array = np.append(particle_1_position_array, position_1_y)

    particle_2_position_array = ([])
    position_2_x = calc_position_eq(acceleration_2, 1, initial_velocity_values[1], initial_position_values[1][0])
    particle_2_position_array = np.append(particle_2_position_array, position_2_x)
    position_2_y = calc_position_eq(acceleration_2, 1, initial_velocity_values[1], initial_position_values[1][1])
    particle_2_position_array = np.append(particle_2_position_array, position_2_y)

    particle_3_position_array = ([])
    position_3_x = calc_position_eq(acceleration_3, 1, initial_velocity_values[2], initial_position_values[2][0])
    particle_3_position_array = np.append(particle_3_position_array, position_3_x)
    position_3_y = calc_position_eq(acceleration_3, 1, initial_velocity_values[2], initial_position_values[2][1])
    particle_3_position_array = np.append(particle_3_position_array, position_3_y)

    # define new values (final)

    # else: (final)

    # final graph
    plt.plot(particle_1_position_array[0], particle_1_position_array[1], 'r-')
    plt.plot(particle_2_position_array[0], particle_2_position_array[1], 'b--')
    plt.plot(particle_3_position_array[0], particle_3_position_array[1], 'g:')

    # how display name of chose of ion?
    plt.legend(['red = ', ions[name_ion_1]])
    plt.legend(['blue = ', ions[name_ion_2]])
    plt.legend(['green = ', ions[name_ion_2]])

    plt.xlabel(' x position ')
    plt.ylabel(' y position ')
    plt.title(' plotting equilibrium position of ions ')
    plt.savefig('equilibrium_pos.pdf')
    plt.show()

    print(f'{determinant}')
    print(f'position of {ions[name_ion_1]} = {particle_1_position_array}')
    print(f'position of {ions[name_ion_2]} = {particle_2_position_array}')
    print(f'position of {ions[name_ion_3]} = {particle_3_position_array}')


# user interface
print(f'Hello! This is a simulation of 3 ions finding equilibrium with each other.')
print()
print(f'Your choice of ions are the following:')
print(f'hydrogen, oxygen, chlorine, lithium')
print(f'aluminum, silver, gold, fluorine')
print(f'sodium, magnesium, calcium, nitrogen, sulfur')
print()
print(f'When entering the name, please type as seen')
# particle 1
i1 = input('name of ion 1 = ')

v1 = eval(input('initial velocity of ion 1 in (x, y) = '))
v1_list = tuple_to_float(v1)
v1_mag = calc_velocity_magnitude(v1_list[0], v1_list[1])
initial_velocity_magnitude_list.append(v1_mag)

a1 = eval(input('initial acceleration of ion 1 in (x, y) = '))
a1_list = tuple_to_float(a1)
initial_acceleration_list.append(a1_list)

p1 = eval(input('initial position of ion 1 in (x, y) = '))
p1_list = tuple_to_float(p1)
initial_position_list.append(p1_list)

# particle 2
i2 = input('name of ion 2 = ')

v2 = eval(input('initial velocity of ion 2 in (x, y) = '))
v2_list = tuple_to_float(v2)
v2_mag = calc_velocity_magnitude(v2_list[0], v2_list[1])
initial_velocity_magnitude_list.append(v2_mag)

a2 = eval(input('initial acceleration of ion 2 in (x, y) = '))
a2_list = tuple_to_float(a2)
initial_acceleration_list.append(a2_list)

p2 = eval(input('initial position of ion 2 in (x, y) = '))
p2_list = tuple_to_float(p2)
initial_position_list.append(p2_list)

# particle 3
i3 = input('name of ion 3 = ')

v3 = eval(input('initial velocity of ion 3 in (x, y) = '))
v3_list = tuple_to_float(v3)
v3_mag = calc_velocity_magnitude(v3_list[0], v3_list[1])
initial_velocity_magnitude_list.append(v3_mag)

a3 = eval(input('initial acceleration of ion 3 in (x, y) = '))
a3_list = tuple_to_float(a3)
initial_acceleration_list.append(a3_list)

p3 = eval(input('initial position of ion 3 in (x, y) = '))
p3_list = tuple_to_float(p3)
initial_position_list.append(p3_list)

# run simulation with given info
matrix_operations(i1, i2, i3, initial_position_list, initial_velocity_magnitude_list)

# # Draft code comments
#
# Does the code run without error?
# - No error when initial positions are unique
# If any error occurs, can you suggest a potential fix?
# - When initial positions are not unique:
#     - Divide by zero
#     - Invalid value in scalar multiply error
#     - Invalid value encountered in det
#   The magnitude value in line 73 is zero, so you would have to work back
#   from there.
#
# How understandable is the output of the code?
# Point out any parts you do not understand.
# - No visible points on plot
#
# How readable is the code itself?
# Say where formatting or commenting would make the code more readable or where PEP-8 is violated.
# - Generally easy to read
# - Many single lines that could be broken into multiple lines
# - The matrix_operations function could be abstracted into a separate module
# - Command line I/O could be refactored or abstracted for ease of reading
#
# How clearly do the code comments describe the problem it is trying to solve?
# Identify places that would benefit from a clearer comment.
# - Comments are useful. Some could be reformatted in a header/content style
#   to aid in readability. Ex:
#       # main function for simulation
#       #     all x and y positions in m
#       #     all accelerations in m/s^2
#       #     all velocities in m/s
#
# How clearly do the variable names relate to the concepts they concretize?
# Point out any variables you don't recognize, and/or suggest better names. Check for PEP-8 compliance.
# - Most variable names are specific. Some that could be more specific are
#   the user input values during prompting, such as v1, a1, p1.
#   In smaller loops or functions this is usually fine, but with the prompt
#   section's size and placement in the base scope, it would benefit from
#   greater specificity.
#
# How well does the range of variables capture the problem described?
# Identify extraneous regions that could be left out or important regions that should be included.
# - Prompting section could be refactored using a function that encapsulates
#   reoccurring behavior, thereby reducing the amount of user input variables
#   explicitly written.
#
# To what degree does the script follow a functional programming paradigm, packaging all major components of the script
# into separately defined functions that pass information among them in a small number of lines? Identify ways in which
# the functionalization of the code could be improved.
# - As mentioned earlier, the matrix_operations function and the prompting
#   section would benefit from abstraction and refactoring.
#
# How clearly do the visualizations show the solutions to the problem?
# - Currently, only scale is displayed. Lacking visible plot points.
#
# Say if there is extraneous whitespace or the co-domain or domain of the data should be changed or any other ways the
# visualizations could be more effective
# - Currently, only scale is displayed. Lacking visible plot points.
#
