#For: se eu sei o limite de repetições, é recomendável o FOR.
#While: se eu não sei o limite, uso o while (condição) para alcançar o objetivo. WHILE.

answer = ""
while answer != "M" and answer != "F":
    answer = str(input("Digite seu sexo: ")).strip().upper()
print("Fim!")