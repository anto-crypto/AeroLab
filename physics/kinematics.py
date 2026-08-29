import math


def calculate_final_position(initial_position, initial_velocity, acceleration, time):
    x = initial_position + initial_velocity * time + 0.5 * acceleration * math.pow(time, 2)
    return x

def calculate_final_velocity(initial_velocity, acceleration, time):
    v = initial_velocity + acceleration * time
    return v

