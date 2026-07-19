def mechanics_menu():
    print()
    print('Mechanics Menu')
    print('1 - Projectile Motion')
    print('2 - Inclined Plane')
    print('3 - Circular Motion')
    print('0 - Back')
    print()

    running = True
    while running:
        answer = input('Select one of the options: ')
        #Checking if the answer is one of the necessary numbers and not else
        if answer in ['0', '1', '2', '3']:
            theme = int(answer)

            #The choice of theme
            if theme == 0:
                running = False

            #Projectil Motion
            elif theme == 1:
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
                name = 'The Data'
                length = len(name)
                print('*' * (10 + length))
                print(name, ' ' * 6)
                print('*' * (10 + length))
                print()
                #The data
                print(f'Velocity = {velocity} m/s')
                print(f'θ = {angle}˚')
                #Print decoration
                print()
                name = 'Projectile Results'
                length = len(name)
                print('=' * (10 + length))
                print(name, ' ' * 6)
                print('=' * (10 + length))
                print()
                #Results
                print(f'Flight time = {calculate_flight_time(velocity, angle):.2f} s')
                print(f'Maximum height = {calculate_max_height(velocity, angle):.2f} m')
                print(f'Range = {calculate_range(velocity, angle):.2f} m')
                print()

            #Inclined Plane
            elif theme == 2:
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
                name = 'The Data'
                length = len(name)
                print('*' * (10 + length))
                print(name, ' ' * 6)
                print('*' * (10 + length))
                print()
                #The data
                print(f'Height = {height} m')
                print(f'θ = {angle}˚')
                print(f'μ = {mu}')
                print(f'Velocity = {velocity} m/s')
                #Print
                print()
                name = 'Inclinated Plane Results'
                length = len(name)
                print('=' * (10 + length))
                print(name, ' ' * 6)
                print('=' * (10 + length))
                print()
                #Results
                from mechanics.inclined_plane import calculate_acceleration
                from mechanics.inclined_plane import final_velocity
                from mechanics.inclined_plane import calculate_time
                print(f'Acceleration = {calculate_acceleration(mu, angle):.2f} m/s²')
                print(f'Final Velocity = {final_velocity(height, velocity, angle, mu):.2f} m/s')
                print(f'Time = {calculate_time(height, angle, mu):.2f} s')
                print()

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
                name = 'The Data'
                length = len(name)
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
                name = 'Circular Motion Results'
                length = len(name)
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
        else:
            print('Error! Its necessary to use only the numbers 0 or 1. Try again')
