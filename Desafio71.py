from random import randint

total = valor_a_sacar = sort_index = 0
cedulas = [50,20,10,1]
cel_50 = cel_20 = cel_10 = cel_1 = 0

valor_a_sacar = int(input("Por favor, digite o valor que deseja sacar; apenas valores inteiros estão disponíveis para saque: "))
if valor_a_sacar == float:
    print("Erro! Digite um valor válido!")
else:
    while True:
        sort_index = randint(0,3)
        cedulas = [50,20,10,1]
        
        if (valor_a_sacar - total) >= 50 and sort_index == 0:
            total += 50
            cel_50 += 1
        
        elif (valor_a_sacar - total) >= 20 and sort_index == 1:
            total += 20
            cel_20 += 1
        
        elif (valor_a_sacar - total) >= 10 and sort_index == 2 :
            total += 10
            cel_10 += 1
        
        elif (valor_a_sacar - total) >= 1 and sort_index == 3:
            total += 1
            cel_1 += 1

        if total == valor_a_sacar:
            break
print(f"O caixa liberou um total de {cel_50} de 50, {cel_20} de 20, {cel_10} de 10 e {cel_1} de 1 real.")
