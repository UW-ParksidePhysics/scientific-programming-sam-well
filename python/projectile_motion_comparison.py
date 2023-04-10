import vpython as vp
import numpy as np

BALL_RADIUS = 1
EARTH_GRAV_ACCEL = -9.8  # m/s**2
MARS_GRAV_ACCEL = -3.7  # m/s**2
MOON_GRAV_ACCEL = -1.6  # m/s**2


def get_launch_angle_1():
    return vp.vector(10.*np.cos(np.pi/6), 10.*np.sin(np.pi/6), 10.)


def get_launch_angle_2():
    return vp.vector(10.*np.cos(np.pi/3), 10.*np.sin(np.pi/3), 10.)


def generate_ball_earth():
    ball_earth_initial_position = vp.vector(25., 25., 0.1)
    return vp.sphere(
        pos=ball_earth_initial_position, radius=BALL_RADIUS, color=vp.color.blue, make_trail=True
    )


def generate_ball_mars():
    ball_mars_initial_position = vp.vector(-25., -25., 0.1)
    return vp.sphere(
        pos=ball_mars_initial_position, radius=BALL_RADIUS, color=vp.color.yellow, make_trail=True
    )


def generate_ball_moon():
    ball_moon_initial_position = vp.vector(-75., -75., 0.1)
    return vp.sphere(
        pos=ball_moon_initial_position, radius=BALL_RADIUS, color=vp.color.white, make_trail=True
    )


earth_center = vp.vector(50., 50., 0.)
earth_dimensions = vp.vector(50., 50., 0.)
earth = vp.box(pos=earth_center, size=earth_dimensions, color=vp.color.green)

mars_center = vp.vector(0., 0., 0.)
mars_dimensions = vp.vector(50., 50., 0.)
mars = vp.box(pos=mars_center, size=mars_dimensions, color=vp.color.red)

moon_center = vp.vector(-50., -50., 0.)
moon_dimensions = vp.vector(50., 50., 0.)
moon = vp.box(pos=moon_center, size=moon_dimensions, color=vp.color.gray(.8))

animation_time_step = 0.01  # seconds
rate_of_animation = 1/animation_time_step
time_step = 0.005
stop_time = 10.

time = 0.
ball_earth = generate_ball_earth()
ball_earth_velocity = get_launch_angle_1()
z = ball_earth_velocity.z
while ball_earth.pos.z > 0:
    vp.rate(rate_of_animation)

    ball_earth_velocity.z = z + EARTH_GRAV_ACCEL*time
    if ball_earth.pos.z <= 0:
        ball_earth_velocity.x = 0
        ball_earth_velocity.y = 0
        ball_earth_velocity.z = 0

    ball_earth.pos.x += ball_earth_velocity.x * time_step
    ball_earth.pos.y += ball_earth_velocity.y * time_step
    ball_earth.pos.z += ball_earth_velocity.z * time_step

    time += time_step

time = 0.
ball_earth = generate_ball_earth()
ball_earth_velocity = get_launch_angle_2()
z = ball_earth_velocity.z
while ball_earth.pos.z > 0:
    vp.rate(rate_of_animation)

    ball_earth_velocity.z = z + EARTH_GRAV_ACCEL*time
    if ball_earth.pos.z <= 0:
        ball_earth_velocity.x = 0
        ball_earth_velocity.y = 0
        ball_earth_velocity.z = 0

    ball_earth.pos.x += ball_earth_velocity.x * time_step
    ball_earth.pos.y += ball_earth_velocity.y * time_step
    ball_earth.pos.z += ball_earth_velocity.z * time_step

    time += time_step

time = 0.
ball_mars = generate_ball_mars()
ball_mars_velocity = get_launch_angle_1()
z = ball_mars_velocity.z
while ball_mars.pos.z > 0:
    vp.rate(rate_of_animation)

    ball_mars_velocity.z = z + MARS_GRAV_ACCEL*time
    if ball_mars.pos.z <= 0:
        ball_mars_velocity.x = 0
        ball_mars_velocity.y = 0
        ball_mars_velocity.z = 0

    ball_mars.pos.x += ball_mars_velocity.x * time_step
    ball_mars.pos.y += ball_mars_velocity.y * time_step
    ball_mars.pos.z += ball_mars_velocity.z * time_step

    time += time_step

time = 0.
ball_mars = generate_ball_mars()
ball_mars_velocity = get_launch_angle_2()
z = ball_mars_velocity.z
while ball_mars.pos.z > 0:
    vp.rate(rate_of_animation)

    ball_mars_velocity.z = z + MARS_GRAV_ACCEL*time
    if ball_mars.pos.z <= 0:
        ball_mars_velocity.x = 0
        ball_mars_velocity.y = 0
        ball_mars_velocity.z = 0

    ball_mars.pos.x += ball_mars_velocity.x * time_step
    ball_mars.pos.y += ball_mars_velocity.y * time_step
    ball_mars.pos.z += ball_mars_velocity.z * time_step

    time += time_step

time = 0.
ball_moon = generate_ball_moon()
ball_moon_velocity = get_launch_angle_1()
z = ball_moon_velocity.z
while ball_moon.pos.z > 0:
    vp.rate(rate_of_animation)

    ball_moon_velocity.z = z + MOON_GRAV_ACCEL*time
    if ball_moon.pos.z <= 0:
        ball_moon_velocity.x = 0
        ball_moon_velocity.y = 0
        ball_moon_velocity.z = 0

    ball_moon.pos.x += ball_moon_velocity.x * time_step
    ball_moon.pos.y += ball_moon_velocity.y * time_step
    ball_moon.pos.z += ball_moon_velocity.z * time_step

    time += time_step

time = 0.
ball_moon = generate_ball_moon()
ball_moon_velocity = get_launch_angle_2()
z = ball_moon_velocity.z
while ball_moon.pos.z > 0:
    vp.rate(rate_of_animation)

    ball_moon_velocity.z = z + MOON_GRAV_ACCEL*time
    if ball_moon.pos.z <= 0:
        ball_moon_velocity.x = 0
        ball_moon_velocity.y = 0
        ball_moon_velocity.z = 0

    ball_moon.pos.x += ball_moon_velocity.x * time_step
    ball_moon.pos.y += ball_moon_velocity.y * time_step
    ball_moon.pos.z += ball_moon_velocity.z * time_step

    time += time_step
