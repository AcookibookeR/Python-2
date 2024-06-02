# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.


def nome():
    nome = str(input("Digite seu nome: ")).strip().lower()
    return nome

def idade():
    idade = int(input("Digite sua idade: "))
    return idade

def sexo():
    sexo = str(input("Digite seu sexo: ")).strip().lower()
    return sexo

cont_mulher = 0
id_total = 0
id_HomemVelho = 0
for c in range (1,5):
    nome_d = nome()
    idade_d = idade()

    sexo_d = sexo()
    if sexo_d == "feminino" and idade_d < 20:
        cont_mulher += 1
    elif sexo_d == "masculino":
        if id_HomemVelho == 0:
            id_HomemVelho += idade_d
        elif idade_d > id_HomemVelho:
            id_HomemVelho = idade_d
        else:
            id_HomemVelho += 0

    id_total += idade_d    
    print(id_HomemVelho)
    print(c)

media_id = id_total / c
print(f"A idade média final do grupo foi de {media_id} anos!")
print(f"Existem um total de {cont_mulher} mulher(es) menores de 20 anos!")
if id_HomemVelho == 0:
    print("Não existem homens nesta lista!")
else:
    print(f"O homem mais velho do grupo possui {id_HomemVelho} anos!")