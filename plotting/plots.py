import matplotlib.pyplot as plt
import math
from utils.usefull_tools import generate_time_points


def projectile_graphic(velocity, angle, g_x, flight_time):
    l = generate_time_points(flight_time)
    x_list = []
    y_list = []

    for i in l:
        x = velocity * math.cos(math.radians(angle)) * i
        x_list.append(x)
        y = velocity * math.sin(math.radians(angle)) * i - 0.5 * g_x * math.pow(i, 2)
        y_list.append(y)
        
    plt.plot(x_list, y_list, marker = '.',
                            markersize = 10,
                            markerfacecolor = 'blue')
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.title('Projectile Motion')
    plt.grid(True)
    plt.show()


def inclined_plane_graphic(velocity, final_time, acceleration):
    l = generate_time_points(final_time)
    x_list = []
    v_list = []

    for i in l:
        x = velocity * i + 0.5 * acceleration * math.pow(i, 2)
        x_list.append(x)
        v = velocity + acceleration * i
        v_list.append(v)
    
    figure, axes = plt.subplots(1, 2)
    axes[0].plot(l, x_list, marker = '.')
    axes[0].set_title('Space-Time')
    axes[0].grid(True)
    axes[0].set_xlabel('Space (m)')
    axes[0].set_ylabel('Time (s)')
    axes[1].plot(l, v_list, marker = '.')
    axes[1].set_title('Velocity-Time')
    axes[1].grid(True)
    axes[1].set_xlabel('Velocity (m/s)')
    axes[1].set_ylabel('Time (s)')
    plt.show()


def free_fall_graphic(velocity, height, g_x, fall_time):
    l = generate_time_points(fall_time)
    x_list = []
    y_list = []

    for i in l:
        y = height + velocity * i - 0.5 * g_x * math.pow(i, 2)
        y_list.append(y)
        
    plt.plot(l, y_list, marker = '.',
                            markersize = 10,
                            markerfacecolor = 'blue')
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.title('Free Fall')
    plt.grid(True)
    plt.show()

