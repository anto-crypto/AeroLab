from utils.usefull_tools import (
    select_gravity,
    physics_menu_decoration,
    data_decoration,
    results_decoration
)


def physics_menu():

    while True:

        physics_menu_decoration()

        answer = input('Select one of the options: ')

        if answer in ['0', '1', '2', '3']:
            theme = int(answer)

            if theme == 0:
                break

            elif theme == 1:
                
                #Checking if the inital position is a number
                while True:
                    try:
                        initial_position = float(input('Insert initial position (m): '))
                        break
                    except ValueError:
                        print('Error! Its necessary to use only numbers (with dot). Try again')
                
                #Checking if the velocity is a number
                while True:
                    try:
                        initial_velocity = float(input('Insert initial velocity (m/s): '))
                        break
                    except ValueError:
                        print('Error! Its necessary to use only numbers (with dot). Try again')
                
                #Checking if the acceleration is a number
                while True:
                    try:
                        acceleration = float(input('Insert acceleration (m/s²) or 0: '))
                        break
                    except ValueError:
                        print('Error! Its necessary to use only numbers (with dot). Try again')
                
                #Checking if the time is a number
                while True:
                    try:
                        time = float(input('Insert time (s): '))
                        break
                    except ValueError:
                        print('Error! Its necessary to use only numbers (with dot). Try again')
                
                #The data
                data_decoration()

                print(f'Initial position = {initial_position} m')
                print(f'Initial velocity = {initial_velocity} m/s')
                print(f'Acceleration = {acceleration} m/s²')
                print(f'Time = {time} s')
                print()

                #The results
                results_decoration()

                from physics.kinematics import (
                    calculate_final_position,
                    calculate_final_velocity
                )

                final_position = calculate_final_position(initial_position, initial_velocity, acceleration, time)
                final_velocity = calculate_final_velocity(initial_velocity, acceleration, time)

                if acceleration != 0:
                    print('Uniformly Accelerated Motion')
                    print(f'Final position = {final_position:.3f} m')
                    print(f'Final velocity = {final_velocity:.3f} m/s')
                else:
                    print('Uniform Motion')
                    print(f'Final position = {final_position:.3f} m')

            elif theme == 2:
                g_x = select_gravity()
                
                #Checking if the mass is a number
                while True:
                    try:
                        mass = float(input('Insert mass (kg): '))
                        break
                    except ValueError:
                        print('Error! Its necessary to use only numbers (with dot). Try again')
                
                #Checking if the velocity is a number
                while True:
                    try:
                        velocity = float(input('Insert initial velocity (m/s) or 0: '))
                        break
                    except ValueError:
                        print('Error! Its necessary to use only numbers (with dot). Try again')
                
                #Checking if the height is a number
                while True:
                    try:
                        height = float(input('Insert height (m) or 0: '))
                        break
                    except ValueError:
                        print('Error! Its necessary to use only numbers (with dot). Try again')
                
                #The data
                data_decoration()

                print(f'Mass = {mass} kg')
                print(f'Velocity = {velocity} m/s')
                print(f'Height = {height} m')
                print(f'Gravity = {g_x} m/s²')

                #The results
                results_decoration()

                from physics.energy import (
                    calculate_kinetic_energy,
                    calculate_gravitational_potential_energy,
                    calculate_mechanical_energy
                )

                if height == 0 and velocity != 0:
                    kinetic_energy = calculate_kinetic_energy(mass, velocity)
                    print(f'Kinetic energy = {kinetic_energy:.3f} J')
                elif velocity == 0 and height != 0:
                    gravitational_potential_energy = calculate_gravitational_potential_energy(mass, g_x, height)
                    print(f'Gravitational potential energy = {gravitational_potential_energy:.3f} J')
                else:
                    mechanical_energy = calculate_mechanical_energy(mass, velocity, g_x, height)
                    print(f'Mechanical energy = {mechanical_energy:.3f} J')
                    from plotting.plots import energy_graphic
                    energy_graphic(mass, velocity, g_x, height)

            elif theme == 3:

                #Checking if the mass is a number
                while True:
                    try:
                        mass = float(input('Insert mass (kg): '))
                        break
                    except ValueError:
                        print('Error! Its necessary to use only numbers (with dot). Try again')
                    
                #Checking if the velocity is a number
                while True:
                    try:
                        velocity = float(input('Insert velocity (m/s): '))
                        break
                    except ValueError:
                        print('Error! Its necessary to use only numbers (with dot). Try again')
                
                #Checking if the force is a number
                while True:
                    try:
                        force = float(input('Insert force (N): '))
                        break
                    except ValueError:
                        print('Error! Its necessary to use only numbers (with dot). Try again')
                
                #Checking if the time interval is a number
                while True:
                    try:
                        interval_time = float(input('Insert time interval (s): '))
                        break
                    except ValueError:
                        print('Error! Its necessary to use only numbers (with dot). Try again')
                
                #The data
                data_decoration()

                print(f'Mass = {mass} kg')
                print(f'Velocity = {velocity} m/s')
                print(f'Force = {force} N')
                print(f'Time interval = {interval_time} s')
                print()

                #The results
                results_decoration()

                from physics.momentum import (
                    calculate_impulse,
                    calculate_momentum
                )

                momentum = calculate_momentum(mass, velocity)
                impulse = calculate_impulse(force, interval_time)

                print(f'Quantity of motion = {momentum:.3f} kg*m/s')
                print(f'Impulse = {impulse:.3f} N*s')

        else:
            print('Error! Its necessary to use only the numbers 0 or 1. Try again')

