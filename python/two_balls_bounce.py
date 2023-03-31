import vpython as vp

BALL_RADIUS = 0.5

ball1_initial_position = vp.vector(-10., (-7.5+BALL_RADIUS), 0.)
ball1_initial_velocity = vp.vector(25., 2., 0.)
ball1 = vp.sphere(pos=ball1_initial_position, radius=BALL_RADIUS, color=vp.color.blue, make_trail=True)

ball2_initial_position = vp.vector(-10., (7.5-BALL_RADIUS), 0.)
ball2_initial_velocity = vp.vector(25., -3., 0.)
ball2 = vp.sphere(pos=ball2_initial_position, radius=BALL_RADIUS, color=vp.color.green, make_trail=True)

wall_center = vp.vector(0., 0., 0.)
wall_dimensions = vp.vector(0.25, 10., 10.)
wall = vp.box(pos=wall_center, size=wall_dimensions, color=vp.color.red)

animation_time_step = 0.01  # seconds
rate_of_animation = 1/animation_time_step
time_step = 0.005
stop_time = 1.

time = 0.
ball1_velocity = ball1_initial_velocity
ball2_velocity = ball2_initial_velocity
while time < stop_time:
    vp.rate(rate_of_animation)

    if (ball1.pos.x + BALL_RADIUS) > wall.pos.x:
        ball1_velocity.x = -ball1_velocity.x  # reverse ball1 velocity
    ball1.pos.x += ball1_velocity.x * time_step
    ball1.pos.y += ball1_velocity.y * time_step
    ball1.pos.z += ball1_velocity.z * time_step

    if (ball2.pos.x + BALL_RADIUS) > wall.pos.x:
        ball2_velocity.x = -ball2_velocity.x  # reverse ball2 velocity
    ball2.pos.x += ball2_velocity.x * time_step
    ball2.pos.y += ball2_velocity.y * time_step
    ball2.pos.z += ball2_velocity.z * time_step
    time += time_step
