idade = num_mul = total_homens = menor_idade = maior_idade = 0 
sexo = ""

while True:
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1
    sexo = str(input("Digite o seu sexo: ")).strip().lower()
    if sexo == "masculino":
        total_homens += 1
    elif sexo == "feminino" and idade < 20:
        num_mul += 1

    escolha = str(input("\nDeseja cadastrar outra pessoa? ")).strip().lower()
    if escolha == "nao":
        break

print("FIM!")
print(f"Existe um total de {maior_idade} pessoa(s) maior(es) de idade!")
print(f"Foram cadastrados um total de {total_homens} homens!")
print(f"Existe um total de {num_mul} mulher(es) menor(es) de 20 anos!")