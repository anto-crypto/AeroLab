import math


def calculate_acceleration(mu, angle, G):
    acceleration = G * (math.sin(math.radians(angle)) - mu * math.cos(math.radians(angle)))
    return acceleration

def final_velocity(height, initial_velocity, angle, mu, G):
    velocity = math.sqrt(math.pow(initial_velocity, 2) + 2 * height / math.sin(math.radians(angle)) * calculate_acceleration(mu, angle, G))
    return velocity

def calculate_time(height, angle, mu, G):
    l = height / math.sin(math.radians(angle))
    time = math.pow(2 * l / calculate_acceleration(mu, angle, G), 0.5)
    return time
