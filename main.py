from utils.usefull_tools import opening


def main():
    while True:

        #Checking it the answer is correct
        while True:
            
            #Opening
            opening()
            print()

            answer = input('Please choose one of the following options: ')

            #Cheking if the answer is one of the necessary numbers
            if answer in ['0','1','2','3']:
                theme = int(answer)

                #The choice of theme
                if theme == 0:
                    break
                elif theme == 1:
                    from mechanics.main import mechanics_menu
                    mechanics_menu()
                elif theme == 2:
                    #Thermodynamics
                    continue
                else:
                    from physics.main import physics_menu
                    physics_menu()
                    continue
                
            else:
                print('Error! Its necessary to use only the numbers 1, 2, 3 or 0. Try again')
        
        if theme == 0:
            break


if __name__ == '__main__':
    main()

