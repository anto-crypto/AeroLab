def opening():

    #Title
    name = 'AeroLab v0.1'
    length = len(name)
    print('=' * (10 + length))
    print(' ' * 4, name, ' ' * 6)
    print('=' * (10 + length))
    
    #Themes
    print('Engineering Sandbox')
    print(' 1 - Mechanics')
    print(' 2 - Thermodynamics')
    print(' 3 - Physics Utilities')
    print(' 0 - Exit')
    print('=' * (10 + length))

def mechanics_menu_decoration():
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

def physics_menu_decoration():
    print()
    print('Physics Utils')
    print(' 1 - Kinematic')
    print(' 2 - Energy')
    print(' 3 - Momentum')
    print(' 0 - Back')
    print()


def generate_time_points(time):
    time_list = []
    i = 0
    while i <= int(time):
        time_list.append(i)
        i += 0.5
    time_list.append(time)
    return time_list


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


def data_decoration():
    #The data decoration
    print()
    name_data = 'The Data'
    length = len(name_data)
    print('*' * (10 + length))
    print(name_data, ' ' * 6)
    print('*' * (10 + length))
    print()

def results_decoration():
    #Print decoration
    print()
    name_result = 'Projectile Results'
    length = len(name_result)
    print('=' * (10 + length))
    print(name_result, ' ' * 6)
    print('=' * (10 + length))
    print()

