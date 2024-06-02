total_gasto = 0
total_produtos_mil = 0
mais_barato = float('inf') #Tive que por um valor infinito, apenas para fazer a primeira comparação do menor preço.
nome_barato = ""

#PS: Para inicia o mais_barato, eu podia ter feito: cont = 0.
# If cont == 0 or preco < mais_barato:
#   mais_barato = preco
#   nome_barato = nome
#  cont += 1
#  Assim no primeiro ciclo ele seria ativado pelo cont, e apartir do segundo ele faria a comparação do preço.

while True:
    nome = (input("Digite o nome do produto: "))
    preco = float(input("Digite o valor do produto: "))
    
    if preco < mais_barato:
        mais_barato = preco
        nome_barato = nome

    if preco > 1000:
        total_produtos_mil += 1

    total_gasto += preco
    escolha = str(input("\nDeseja por mais itens? ")).strip().lower()
    print("\n")
    if escolha == 'nao':
        break

print(f"FIM!\n")
print(f"O total da compra foi de R$ {total_gasto} !")
print(f"O total de produtos que custaram mais de R$ 1000 foi de {total_produtos_mil} !")
print(f"O produto mais barato foi o {nome_barato} com o preço de R$ {mais_barato} !")
