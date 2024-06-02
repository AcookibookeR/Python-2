valor_casa = float(input("Digite o valor da casa: "))
salarium = float(input("Digite o valor do seu salário: "))
tempo_anos = int(input("Digite o tempo, em anos, que deseja para pagar a casa: "))

porc_sala = (salarium * 30) / 100
prestacao_mensal = valor_casa / (tempo_anos * 12)

print(f"A prestação mensal ficou em R$ {prestacao_mensal} .")
print(f"E 30% do seu salário de R$ {salarium} correspondem a  R$ {porc_sala} .")

if prestacao_mensal > porc_sala:
    print("Empréstimo negado!")
else:
    print("Empréstimo aprovado!")