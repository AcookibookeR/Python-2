esc = 0

while esc != 5:
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    print("\n""""[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa
          """)
    esc = int(input("Digite sua escolha: "))
    if esc == 1:
        resultado = num1 + num2
        print(f"A soma dos dois números é: {resultado} !")
    elif esc == 2:
        resultado = num1 * num2
        print(f"A multiplicação dos dois números é: {resultado} !")
    elif esc == 3:
        if num1 > num2:
            print(f"O maior número é o {num1} !")
        else:
            print(f"O maior número é o {num2} !")
    elif esc > 5 or esc == 0:
        print("Número inválido!")