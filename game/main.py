import random


def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('Piedra, papel o tijeras => ').lower()
    print('')
    
    if not user_option in options:
        print('Esa opción no es valida')
        # continue
        return None, None
    
    computer_option = random.choice(options)
    
    print('👤 =>',user_option)
    print('🤖 =>',computer_option)
    
    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('')
        print('-' * 20)
        print('Empate!')
        print('-' * 20)
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('')
            print('piedra gana a tijera')
            print('')
            print('-' * 20)
            print('👤 gano!')
            print('-' * 20)
            user_wins += 1

        else:
            print('')
            print('papel gana a piedra')
            print('')
            print('-' * 20)
            print('🤖 gano!')
            print('-' * 20)
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('')
            print('papel gana a piedra')
            print('')
            print('-' * 20)
            print('👤 gano!')
            print('-' * 20)
            user_wins += 1
        else:
            print('')
            print('tijera gana a papel')
            print('')
            print('-' * 20)
            print('🤖 gano!')
            print('-' * 20)
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('')
            print('tijera gana a papel')
            print('')
            print('-' * 20)
            print('👤 gano!')
            print('-' * 20)
            user_wins += 1
        else:
            print('')
            print('piedra gana a tijera')
            print('')
            print('-' * 20)
            print('🤖 gano!')
            print('-' * 20)
            computer_wins += 1
            
    return user_wins, computer_wins

def run_game():
    # valores incrementales
    rounds = 1
    user_wins = 0
    computer_wins = 0

    while True:
        print('')
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)
        print('')
        
        print('👤 wins =>', user_wins)
        print('🤖 wins =>', computer_wins)
        print('')
        
        #aumentamos el contador cada vez que comienza una nueva ronda
        rounds += 1
        
        # mandamos a llamar la función
        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
    
        # revisa cual es el ganador de la sesión de juego
        if computer_wins == 3:
            print('')
            print('El ganador es 🤖')
            print('')
            break
        if user_wins == 3:
            print('')
            print('El ganador es 👤')
            print('')
            break
        
run_game()