from random import randint
sort_Pc = randint(0,10)
tentativa = 0
resp_Pc = 0

while resp_Pc != sort_Pc:
    resp_Pc = int(input("Digite seu palpite: "))
    tentativa += 1
print(f"Você acertou o número! Que era {sort_Pc}!")
print(f"Você precisou de {tentativa} tentativa(s) para acertar!")