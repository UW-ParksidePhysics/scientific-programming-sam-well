import vpython as vp
import numpy as np

BALL_RADIUS = 0.5
LAUNCH_ANGLE = np.pi / 4  # 45 degrees
EARTH_GRAV_ACCEL = -9.81 # m/s**2

ball_initial_position = vp.vector(0., 0., 0.)
ball_initial_velocity = vp.vector(2., 2., 0.)
ball = vp.sphere(pos=ball_initial_position, radius=BALL_RADIUS, color=vp.color.blue, make_trail=True)

field_center = vp.vector(5., -0.5, 0.)
field_dimensions = vp.vector(10, 1., 1.)
field = vp.box(pos=field_center, size=field_dimensions, color=vp.color.green)

animation_time_step = 0.01  # seconds
rate_of_animation = 1/animation_time_step
time_step = 0.005
stop_time = 1000.

time = 0.
ball_velocity = ball_initial_velocity
ball_velocity_magnitude = np.sqrt(ball_initial_velocity.x**2 + ball_initial_velocity.y**2)
while time < stop_time:
    vp.rate(rate_of_animation)

    time_of_flight = (2 * (ball_initial_velocity.y * np.sin(LAUNCH_ANGLE))) / -EARTH_GRAV_ACCEL
    # ball_range = (ball_initial_velocity.x**2 * np.sin(2*LAUNCH_ANGLE)) / -EARTH_GRAV_ACCEL
    ball_range = ball_initial_velocity.x * time_of_flight

    if time < time_of_flight:
        print(f"time of flight: {time_of_flight}")
        # print(f"range: {ball_range}")
        ball.pos.x += ball_initial_velocity.x * time
        ball.pos.y += (ball_velocity.y * time) + (0.5 * EARTH_GRAV_ACCEL * time ** 2)
        ball.pos.z += ball_initial_velocity.z * time
        print(ball.pos.x)
        print(time)
    time += time_step
