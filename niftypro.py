def a(force, distance):
    work = force * distance
    print(f'Work = {work}J')

def b(displacement, time):
    velocity = displacement/time
    print(f'Velocity = {velocity}m/s')

def c(initial_velocity, final_velocity, time):
    acceleration = (final_velocity - initial_velocity) / time
    print(f'Acceleration = {acceleration}m/s^2')

def d(mass, acceleration):
    force = mass * acceleration
    print(f'{force = }N')

def e(mass, velocity):
    momentum = mass * velocity
    print(f'{momentum = }kgm/s')

