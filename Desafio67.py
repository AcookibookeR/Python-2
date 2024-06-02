num = int(input("Digite a tabuada que deseja saber: "))
mult = 0

while True:
    if num < 0 or mult == 11:
        break
    resultado = num * mult
    print(f" {num} X {mult} = {resultado}")
    mult += 1
print("FIM!")