pare = ""
resultado_media = 0
contador_media = 0
soma_media = 0
maior_num = 0
menor_num = 0
num = 0
while pare != "sim":
    num = int(input("Digite um valor: "))
    soma_media += num
    contador_media += 1
    if num > maior_num:
        maior_num = num
    else:
        menor_num = num
    pare = str(input("Deseja parar? "))

resultado_media = soma_media / contador_media
print(f"A média final foi {resultado_media} !")
print(f"O maior número foi {maior_num} !")
print(f"O menor número foi {menor_num} !")
print("FIM!")
