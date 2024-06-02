from random import randint
user_pc = 0
user = 0

while user_pc != 3 and user != 3:
    user_choice = str(input("Escolha pedra, papel ou tesoura: ")).strip().lower()
    sort_pc = randint (1,3)
    if sort_pc == 1:
        sort_pc = 'pedra'
    elif sort_pc == 2:
        sort_pc = 'papel'
    else:
        sort_pc = 'tesoura'

        if (user_choice == 'tesoura' and sort_pc == 'pedra') or \
           (user_choice == 'pedra' and sort_pc == 'papel') or \
           (user_choice == 'papel' and sort_pc == 'tesoura'):
            print("Você perdeu!")
            user_pc += 1
        elif (user_choice == 'pedra' and sort_pc == 'tesoura') or \
             (user_choice == 'papel' and sort_pc == 'pedra') or \
             (user_choice == 'tesoura' and sort_pc == 'papel'):
            print("Você ganhou!")
            user += 1
        elif (user_choice == 'pedra' and sort_pc == 'pedra') or \
             (user_choice == 'papel' and sort_pc == 'papel') or \
             (user_choice == 'tesoura' and sort_pc == 'tesoura'):
             print("Empate!")

if user_pc == 3:
    print("O computador venceu o jogo!")
else:
    print("Você ganhou o jogo!")
        

    


