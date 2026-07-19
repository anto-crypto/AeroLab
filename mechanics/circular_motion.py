import math
from utils.constants import PI

#Theta
def calculate_angular_velocity(theta, time):
    ang_velocity = math.radians(theta) / time
    return ang_velocity

def calculate_centripetal_acceleration(theta, time, radius):
    cen_acceleration = math.pow(calculate_angular_velocity(theta, time), 2) * radius
    return cen_acceleration

def calculate_period(theta, time):
    period = 2 * PI / calculate_angular_velocity(theta, time)
    return period

def calculate_frequency(theta, time):
    frequency = 1 / calculate_period(theta, time)
    return frequency

#Velocity
def calculate_angular_velocity_v(velocity, radius):
    ang_velocity_v = velocity / radius
    return ang_velocity_v

def calculate_centripetal_acceleration_v(velocity, radius):
    cen_acceleration = math.pow(velocity, 2) / radius
    return cen_acceleration

def calculate_period_v(velocity, radius):
    period = 2 * PI * radius/ velocity
    return period

def calculate_frequency_v(velocity, radius):
    frequency = 1 / calculate_period_v(velocity, radius)
    return frequency
