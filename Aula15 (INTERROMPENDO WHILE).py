#  For se usa quando você sabe quando parar. Tem algo FIXO. Tanto For e While são de repetição.
#  While se usa quando você tem uma repetição de ações por tempo indetemrinado ou até cumprir determinada ação.

# num = 10
# for c in range (0, 10):
#     print(num, end= " ")
#     num += 10

# num2 = 10
# while num2 != 110:
#     print(num2, end= " ")
#     num2 += 10

num = soma = 0
while True:
    num =  int(input("Digite um número: "))
    if num == 999:
        break # Esse checa se o num é 999, se não for, ele leva pra soma. Se for, ele para aqui e não soma e vai pro final do programa.
    soma += num
print(f"A soma final foi {soma} !")