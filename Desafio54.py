from datetime import date
ano_atual = date.today().year
cont_ida = 0
maior = 0
menor = 0

for idade in range (0, 7):
    cont_ida += 1
    ano = int(input(f"Digite o {cont_ida}ª ano de nascimento: "))
    idade = ano_atual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f"{maior} pessoa(s) são maiores de idade!")
print(f"{menor} pessoa(s) são menores de idade!")