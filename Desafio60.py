from math import factorial

# num = int(input("Digite um número para ser fatorado: "))
# result = factorial(num)

stop = 0
while 1 != stop:
    num = int(input("Digite um número para ser fatorado: "))
    result = factorial(num)
    print(f"O fatorial de {num} é {result} !")
    resp = str(input("Deseja sair? ")).strip().lower()
    if resp == "sim":
        stop += 1
print("Fim!")