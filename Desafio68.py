placar_user = 0
placar_pc = 0
soma_total = 0

from random import randint

while True: # OU placar_pc == 0
    # Se eu uso while True, quer dizer que ele rodará infinitamente até achar algo que o pare (BREAK). Não possui uma para ESPECIFICA.
    # Porém se eu uso while placar_pc == 0, indica que HÁ uma para especifica. E também facilita caso eu queria mudar posteriormente.

    num_pc = randint(0, 1000)
    cat_pc = randint(0, 1)
    if cat_pc == 0:
        cat_pc = "par"
    else:
        cat_pc = "impar"

    esc_user = int(input("Jogue um número: "))
    cat_user = str(input("Escolha Ímpar ou Par: ")).strip().lower()

    soma_total = num_pc + esc_user
    if soma_total % 2 == 0:
        if cat_user == "par":
            placar_user += 1
            print("Você ganhou!")
        else:
            placar_pc += 1
            break
    else:
        if cat_user == "impar":
            placar_user += 1
            print("Você ganhou!")
        else:
            placar_pc += 1
            break

print("Você perdeu!")
print(f"O computador acertou {placar_pc} vezes e você {placar_user} vezes!")
print("-"*50)