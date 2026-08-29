import math


def calculate_kinetic_energy(mass, velocity):
    k = 0.5 * mass * math.pow(velocity, 2)
    return k

def calculate_gravitational_potential_energy(mass, g_x, height):
    u = mass * g_x * height
    return u

def calculate_mechanical_energy(mass, velocity, g_x, height):
    e = calculate_kinetic_energy(mass, velocity) + calculate_gravitational_potential_energy(mass, g_x, height)
    return e

