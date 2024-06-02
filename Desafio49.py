num = int(input("Digite um número: "))
tamanho = int(input("Digite o tamanho da tabuado: "))

for cont in range (0, tamanho +1):
    print(f"{num} X {cont} = ",num * cont)
print("Fim!")