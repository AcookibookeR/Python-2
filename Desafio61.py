inicio = int(input("Digite um primeiro valor: "))
razao = int(input("Digite a razão: "))
termo = inicio
cont = 0

while cont != 10:
    print(f"{termo} -> ", end= "")
    termo += razao
    cont += 1
print("FIM!")