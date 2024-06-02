num1 = int(input("Digite um valor: "))
num2 = int(input("Digite outro valor: "))

if num1 > num2:
    print(f"O valor {num1} é maior do que {num2} .")
elif num2 > num1:
    print(f"O valor {num2} é maior do que {num1} .")
elif num1 == num2:
    print("Ambos os valores são iguais.")