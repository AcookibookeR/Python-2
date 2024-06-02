inicio = int(input("Digite um primeiro valor: "))
razao = int(input("Digite a razão: "))
decimo = inicio + (10 - 1) * razao
for PA in range (inicio, decimo + 1, razao):
    print(PA, end= " ")