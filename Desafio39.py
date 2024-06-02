# from datetime import date
# ano = date.today().year
ano = int(input("Informe o ano de seu nascimento: "))
idade = 2024 - ano

if idade == 18:
    print("É a hora de se alistar!")
elif idade >= 19 and idade != 18:
    tempo_passou = idade - 18
    print("Você passou do tempo de alistamento!")
    print(f"Você já passou {tempo_passou} ano(s)!")
elif idade < 18:
    tempo_falta = 18 - idade
    print("Ainda não é hora de se alistar!")
    print(f"Ainda faltam {tempo_falta} anos!")