import math
from utils.constants import PI


def calculate_angular_velocity_v(linear_velocity, radius):
    ang_velocity_v = linear_velocity / radius
    return ang_velocity_v

def calculate_centripetal_acceleration_v(linear_velocity, radius):
    cen_acceleration = math.pow(linear_velocity, 2) / radius
    return cen_acceleration

def calculate_period_v(linear_velocity, radius):
    period = 2 * PI * radius/ linear_velocity
    return period

def calculate_frequency_v(linear_velocity, radius):
    frequency = 1 / calculate_period_v(linear_velocity, radius)
    return frequency

def calculate_centripetal_force(mass, linear_velocity, radius):
    f = mass * math.pow(linear_velocity, 2) / radius
    return f

