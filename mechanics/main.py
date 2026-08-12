import math


def select_gravity():
    from utils.constants import gravity

    print()
    print('Environment gravity')
    print('1 - Earth')
    print('2 - Mars')
    print('3 - Moon')
    print()

    #Cheking the environment
    while True:
        try:
            environment = int(input('Select the environment for the gravity: '))
        except ValueError:
            print('Error! Please chose one of the numbers requested.')

        #Checking the G
        if environment == 1:
            g_x = gravity['Earth']
            break
        elif environment == 2:
            g_x = gravity['Mars']
            break
        elif environment == 3:
            g_x = gravity['Moon']
            break
        else:
            print('Chose a number between 1 to 3.')

    return g_x


def generate_time_points(time):
    time_list = []
    i = 0
    while i <= int(time):
        time_list.append(i)
        i += 0.5
    time_list.append(time)
    return time_list



def mechanics_menu():

    while True:

        print()
        print('Mechanics Menu')
        print(' 1 - Projectile Motion')
        print(' 2 - Inclined Plane')
        print(' 3 - Circular Motion')
        print(' 4 - Free Fall')
        print(' 5 - Uniform Circular Motion')
        print(' 6 - Centripetal Force')
        print(' 0 - Back')
        print()

        answer = input('Select one of the options: ')

        #Checking if the answer is one of the necessary numbers and not else
        if answer in ['0', '1', '2', '3', '4', '5', '6']:
            theme = int(answer)

            #The choice of theme
            if theme == 0:
                break

            #Projectil Motion
            elif theme == 1:
                g_x = select_gravity()

                #Checking if the velocity is a number
                while True:
                    try:
                        velocity = float(input('Insert initial velocity (m/s): '))
                        break
                    except ValueError:
                        print('Error! Its necessary to use only numbers (with dot). Try again')  

                #Checking if the angle is a number
                while True:
                    try:
                        angle = float(input('Insert initial angle (degrees): '))
                        break
                    except ValueError:
                        print('Error! Its necessary to use only numbers (with dot). Try again')

                #The data decoration
                print()
                name_data = 'The Data'
                length = len(name_data)
                print('*' * (10 + length))
                print(name_data, ' ' * 6)
                print('*' * (10 + length))
                print()

                #The data
                print(f'Velocity = {velocity} m/s')
                print(f'θ = {angle}˚')
                print(f'Gravity: {g_x} m/s²')

                #Print decoration
                print()
                name_result = 'Projectile Results'
                length = len(name_result)
                print('=' * (10 + length))
                print(name_result, ' ' * 6)
                print('=' * (10 + length))
                print()

                #Results
                from mechanics.projectile import calculate_flight_time
                from mechanics.projectile import calculate_max_height
                from mechanics.projectile import calculate_range
                print(f'Flight time = {calculate_flight_time(velocity, angle, g_x):.2f} s')
                print(f'Maximum height = {calculate_max_height(velocity, angle, g_x):.2f} m')
                print(f'Range = {calculate_range(velocity, angle, g_x):.2f} m')
                print()

                #Graphic
                import matplotlib.pyplot as plt
                time_points = calculate_flight_time(velocity, angle, g_x)
                l = generate_time_points(time_points)
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

            #Inclined Plane
            elif theme == 2:
                g_x = select_gravity()

                    #Checking if the height is a number
                while True:
                    try:
                        height = float(input('Insert height (m): '))
                        break
                    except ValueError:
                        print('Error! Its necessary to use only numbers (with dot). Try again')

                #Checking if the angle is a number
                while True:
                    try:
                        angle = float(input('Insert angle (degrees): '))
                        break
                    except ValueError:
                        print('Error! Its necessary to use only numbers (with dot). Try again')

                #Checking if the mu is a number
                while True:
                    try:
                        mu = float(input('Insert μ if necessery otherwise click 0: '))
                        break
                    except ValueError:
                        print('Error! Its necessary to use only numbers (with dot). Try again')

                #Checking if the initial velocity is a number
                while True:
                    try:
                        velocity = float(input('Insert initial velocity (m/s): '))
                        break
                    except ValueError:
                        print('Error! Its necessary to use only numbers (with dot). Try again')

                #The data decoration
                print()
                name_data = 'The Data'
                length = len(name_data)
                print('*' * (10 + length))
                print(name_data, ' ' * 6)
                print('*' * (10 + length))
                print()

                #The data
                print(f'Height = {height} m')
                print(f'θ = {angle}˚')
                print(f'μ = {mu}')
                print(f'Velocity = {velocity} m/s')
                print(f'Gravity: {g_x} m/s²')

                #Print
                print()
                name_result = 'Inclinated Plane Results'
                length = len(name_result)
                print('=' * (10 + length))
                print(name_result, ' ' * 6)
                print('=' * (10 + length))
                print()

                #Results
                from mechanics.inclined_plane import calculate_acceleration
                from mechanics.inclined_plane import calculate_time
                from mechanics.inclined_plane import calculate_final_velocity
                print(f'Acceleration = {calculate_acceleration(mu, angle, g_x):.2f} m/s²')
                print(f'Time = {calculate_time(height, angle, mu, g_x):.2f} s')
                print(f'Final Velocity = {calculate_final_velocity(height, velocity, angle, mu, g_x):.2f} m/s')
                print()

                #Graphic
                import matplotlib.pyplot as plt
                time_points = calculate_time(height, angle, mu, g_x)
                acceleration = calculate_acceleration(mu, angle, g_x)
                l = generate_time_points(time_points)
                x_list = []
                v_list = []
                for i in l:
                    x = velocity * i + 0.5 * acceleration * math.pow(i, 2)
                    x_list.append(x)
                    v = velocity + acceleration * i
                    v_list.append(v)
                figure, axes = plt.subplots(1, 2)
                axes[0].plot(x_list, l, marker = '.')
                axes[0].set_title('Space-Time')
                axes[0].grid(True)
                axes[0].set_xlabel('Space (m)')
                axes[0].set_ylabel('Time (s)')
                axes[1].plot(v_list, l, marker = '.')
                axes[1].set_title('Velocity-Time')
                axes[1].grid(True)
                axes[1].set_xlabel('Velocity (m/s)')
                axes[1].set_ylabel('Time (s)')
                plt.show()

            #Circular Motion
            elif theme == 3:

                #Checking if the initial velocity is a number
                while True:
                    try:
                        velocity = float(input('Insert initial velocity (m/s) if necessary otherwise click 0: '))
                        break
                    except ValueError:
                        print('Error! Its necessary to use only numbers (with dot). Try again')

                #Checking if the radius is a number
                while True:
                    try:
                        radius = float(input('Insert radius (m): '))
                        break
                    except ValueError:
                        print('Error! Its necessary to use only numbers (with dot). Try again')

                #Checking if the time is a number
                while True:
                    try:
                        if velocity == 0:
                            time = float(input('Insert time (s): '))
                            break
                        else:
                            break
                    except ValueError:
                        print('Error! Its necessary to use only numbers (with dot). Try again')

                #Checking if the theta is a number
                while True:
                    try:
                        if velocity == 0:
                            theta = float(input('Insert angle (˚): '))
                            break
                        else:
                            break
                    except ValueError:
                        print('Error! Its necessary to use only numbers (with dot). Try again')

                #The data decoration
                print()
                name_data = 'The Data'
                length = len(name_data)
                print('*' * (10 + length))
                print(name, ' ' * 6)
                print('*' * (10 + length))
                print()

                #The data
                print(f'Velocity = {velocity} m/s')
                print(f'Radius = {radius} m')
                if velocity == 0:
                    print(f'θ = {theta}˚')
                    print(f'Time = {time} s')

                #Print
                print()
                name_result = 'Circular Motion Results'
                length = len(name_result)
                print('=' * (10 + length))
                print(name, ' ' * 6)
                print('=' * (10 + length))
                print()

                #Results
                if velocity == 0:
                    from mechanics.circular_motion import calculate_angular_velocity
                    from mechanics.circular_motion import calculate_centripetal_acceleration
                    from mechanics.circular_motion import calculate_period
                    from mechanics.circular_motion import calculate_frequency
                    print(f'Angular velocity = {calculate_angular_velocity(theta, time):.2f} rad/s')
                    print(f'Centripetal acceleration = {calculate_centripetal_acceleration(theta, time, radius):.2f} rad/s²')
                    print(f'Period = {calculate_period(theta, time):.2f} s')
                    print(f'Frequency = {calcluate_frequency(theta, time):.2f} s^-1')
                    print()
                else:
                    from mechanics.circular_motion import calculate_angular_velocity_v
                    from mechanics.circular_motion import calculate_centripetal_acceleration_v
                    from mechanics.circular_motion import calculate_period_v
                    from mechanics.circular_motion import calculate_frequency_v
                    print(f'Angular velocity = {calculate_angular_velocity_v(velocity, radius):.2f} rad/s')
                    print(f'Centripetal acceleration = {calculate_centripetal_acceleration_v(velocity, radius):.2f} rad/s²')
                    print(f'Period = {calculate_period_v(velocity, radius):.2f} s')
                    print(f'Frequency = {calcluate_frequency_v(velocity, radius):.2f} s^-1')
                    print()

            #Free Fall
            elif theme == 4:
                continue

            #Uniform Circular Force
            elif theme == 5:
                continue

            #Centripetal Force
            elif theme == 6:
                continue


        else:
            print('Error! Its necessary to use only the numbers 0 or 1. Try again')

