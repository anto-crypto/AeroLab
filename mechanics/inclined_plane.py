import math
from utils.constants import g_Earth


def calculate_acceleration(mu, angle):
    acceleration = g_Earth * (math.sin(math.radians(angle)) - mu * math.cos(math.radians(angle)))
    return acceleration

def final_velocity(height, initial_velocity, angle, mu):
    velocity = math.sqrt(math.pow(initial_velocity, 2) + 2 * height / math.sin(math.radians(angle)) * calculate_acceleration(mu, angle))
    return velocity

def calculate_time(height, angle, mu):
    l = height / math.sin(math.radians(angle))
    time = math.pow(2 * l / calculate_acceleration(mu, angle), 0.5)
    return time
