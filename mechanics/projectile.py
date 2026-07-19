import math
from utils.constants import g_Earth


def calculate_flight_time(v0, angle):
    flight_time = 2 * v0 * math.sin(math.radians(angle)) / g_Earth
    return flight_time

def calculate_max_height(v0, angle):
    max_height = math.pow(v0, 2) * math.pow(math.sin(math.radians(angle)), 2) / (2 * g_Earth)
    return max_height

def calculate_range(v0, angle):
    x_range = math.pow(v0, 2) * (math.sin(math.radians(2 * angle))) / g_Earth
    return x_range
