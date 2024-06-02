preco_normal = 2560.75
print(f"O preço normal, sem descontos, da geladeira é de R$ {preco_normal} .")

avista_cheque_dinheiro = str(input("Deseja pagar à vista via cheque/dinheiro, recebendo 10% de desconto? ")).strip()
if avista_cheque_dinheiro == 'sim':
    desconto10 = (preco_normal * 10) / 100
    preco_final = preco_normal - desconto10
    print(f"O preço final à vista com cheque ou dinheiro é de {preco_final} .")
else:
    avista_cartao = str(input("Deseja pagar no cartão à vista, com 5% de desconto? ")).strip()
    if avista_cartao == 'sim':
        desconto5 = (preco_normal * 5) / 100
        preco_final = preco_normal - desconto5
        print(f"O preço final à vista com cartão é de {preco_final} .")
    else:
        duasxcartao = str(input("Deseja parcelar em 2x no cartão, sem desconto? ")).strip()
        if duasxcartao == 'sim':
            preco_final = preco_normal / 2
            print(f"O preço final parcelado em 2x no cartão é de {preco_final} .")
        else:
            tresxcartao = str(input("Deseja parcelar em mais de 3 parcelas, com juros de 20%? ")).strip()
            if tresxcartao == 'sim':
                juros = (preco_normal * 20) / 100
                preco_final = preco_normal + juros
                r_tresxcartao = int(input("Digite o total de parcelas que deseja: "))
                parcelas = preco_final / r_tresxcartao
                print(f"O preço final parcelado em {r_tresxcartao} vezes é de {preco_final} .")
            else:
                print("Nenhuma opção selecionada. O preço final é o mesmo sem descontos ou acréscimos.")