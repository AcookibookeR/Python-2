soma = 0
cont = 0
for c in range (1,501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f"A soma final foi de {soma} .")
print(f"O total de número somados foram de {cont} .")
print("Fim!")