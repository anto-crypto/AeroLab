import math


def calculate_fall_time(velocity, height, g_x):
    t = math.pow(math.pow(velocity, 2) + 2 * g_x * height, 0.5) / g_x
    return t

def calculate_final_velocity(velocity, height, g_x):
    v = velocity - g_x * calculate_fall_time(velocity, height, g_x)
    return v

