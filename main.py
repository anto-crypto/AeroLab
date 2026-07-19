def opening():
    #Title
    name = 'AeroLab v0.1'
    length = len(name)
    print('=' * (10 + length))
    print(' ' * 4, name, ' ' * 6)
    print('=' * (10 + length))
    
    #Themes
    print('1 - Mechanics')
    print('2 - Thermodynamics')
    print('3 - Physics Utilities')
    print('0 - Exit')

opening()
print()

running = True
while running:
    answer = input('Please choose one of the following options: ')
    #Cheking if the answer is one of the necessary numbers
    if answer in ['0','1','2','3']:
        theme = int(answer)

        #The choice of theme
        if theme == 0:
            running = False
        elif theme == 1:
            from mechanics.main import mechanics_menu
            mechanics_menu()
        elif theme == 2:
            #Thermodynamics
            continue
        else:
            #Physics Utilities
            continue
        
    else:
        print('Error! Its necessary to use only the numbers 1, 2, 3 or 0. Try again')


if __name__ == '__main__':
    opening()

