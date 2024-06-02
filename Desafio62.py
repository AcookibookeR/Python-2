inicio = int(input("Digite um primeiro valor: "))
razao = int(input("Digite a razão: "))
termo = inicio
cont = 0
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont != total:
        print(f"{termo} -> ", end= "")
        termo += razao
        cont += 1
    print("PAUSA!")
    mais = int(input("Quantos termos a mais deseja ver: "))
print("FIM!")
print(f"O total de termos utilizados foi {total} .")