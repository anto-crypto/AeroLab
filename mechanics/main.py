from utils.usefull_tools import (
    mechanics_menu_decoration,
    generate_time_points,
    select_gravity,
    data_decoration,
    results_decoration
    )

def mechanics_menu():

    while True:

        mechanics_menu_decoration()

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
                
                #The data
                data_decoration()

                print(f'Velocity = {velocity} m/s')
                print(f'θ = {angle}˚')
                print(f'Gravity: {g_x} m/s²')

                #Results
                results_decoration()

                from mechanics.projectile import (
                    calculate_flight_time,
                    calculate_max_height,
                    calculate_range
                )

                flight_time = calculate_flight_time(velocity, angle, g_x)
                maximum_height = calculate_max_height(velocity, angle, g_x)
                range_x = calculate_range(velocity, angle, g_x)

                print(f'Flight time = {flight_time:.3f} s')
                print(f'Maximum height = {maximum_height:.3f} m')
                print(f'Range = {range_x:.3f} m')
                print()

                #Graphic
                from plotting.plots import projectile_graphic
                projectile_graphic(velocity, angle, g_x, flight_time)

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

                #The data
                data_decoration()

                print(f'Height = {height} m')
                print(f'θ = {angle}˚')
                print(f'μ = {mu}')
                print(f'Velocity = {velocity} m/s')
                print(f'Gravity: {g_x} m/s²')

                #Results
                results_decoration()

                from mechanics.inclined_plane import (
                    calculate_acceleration,
                    calculate_time,
                    calculate_final_velocity
                )

                acceleration = calculate_acceleration(mu, angle, g_x)
                final_time = calculate_time(height, angle, mu, g_x)
                final_velocity = calculate_final_velocity(height, velocity, angle, mu, g_x)

                print(f'Acceleration = {acceleration:.3f} m/s²')
                print(f'Time = {final_time:.3f} s')
                print(f'Final Velocity = {final_velocity:.3f} m/s')
                print()

                #Graphic
                from plotting.plots import inclined_plane_graphic
                inclined_plane_graphic(velocity, final_time, acceleration)

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

                #The data
                data_decoration()
                print(f'Velocity = {velocity} m/s')
                print(f'Radius = {radius} m')
                if velocity == 0:
                    print(f'θ = {theta}˚')
                    print(f'Time = {time} s')

                #Results
                results_decoration()
                if velocity == 0:
                    from mechanics.circular_motion import (
                        calculate_angular_velocity,
                        calculate_centripetal_acceleration,
                        calculate_period,
                        calculate_frequency
                    )

                    angular_velocity = calculate_angular_velocity(theta, time)
                    centripetal_acceleration = calculate_centripetal_acceleration(theta, time, radius)
                    period = calculate_period(theta, time)
                    frequency = calculate_frequency(theta, time)

                    print(f'Angular velocity = {angular_velocity:.3f} rad/s')
                    print(f'Centripetal acceleration = {centripetal_acceleration:.3f} rad/s²')
                    print(f'Period = {period:.3f} s')
                    print(f'Frequency = {frequency:.3f} s^-1')
                    print()
                else:
                    from mechanics.circular_motion import (
                        calculate_angular_velocity_v,
                        calculate_centripetal_acceleration_v,
                        calculate_period_v,
                        calculate_frequency_v
                    )

                    angular_velocity_v = calculate_angular_velocity_v(velocity, radius)
                    centripetal_acceleration_v = calculate_centripetal_acceleration_v(velocity, radius)
                    period_v = calculate_period_v(velocity, radius)
                    frequency_v = calculate_frequency_v(velocity, radius)

                    print(f'Angular velocity = {angular_velocity_v:.3f} rad/s')
                    print(f'Centripetal acceleration = {centripetal_acceleration_v:.3f} rad/s²')
                    print(f'Period = {period_v:.3f} s')
                    print(f'Frequency = {frequency_v:.3f} s^-1')
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

