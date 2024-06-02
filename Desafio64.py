num = 0
cont_num = 0
soma_num = 0
soma_total = 0
while num != 999:
    num = int(input("Digite um número: "))
    soma_num += num
    cont_num += 1
soma_total = soma_num - 999
print(f"A soma final de todas as tentivas foi de {soma_total} !")
print(f"Foi preciso um total de {cont_num - 1} vezes para parar o programa!")