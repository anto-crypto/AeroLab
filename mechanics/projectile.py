import math


def calculate_flight_time(v0, angle, G):
    flight_time = 2 * v0 * math.sin(math.radians(angle)) / G
    return flight_time

def calculate_max_height(v0, angle, G):
    max_height = math.pow(v0, 2) * math.pow(math.sin(math.radians(angle)), 2) / (2 * G)
    return max_height

def calculate_range(v0, angle, G):
    x_range = math.pow(v0, 2) * (math.sin(math.radians(2 * angle))) / G
    return x_range
