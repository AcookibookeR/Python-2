frase = str(input("Digite um frase: ")).strip().lower()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f"A frase \" {frase} \" é um palíndromo!")
else:
    print(f"A frase \" {frase} \" não é um palíndromo!")