num = int(input("Quantos termos você quer na sequência de Fibonacci: "))
t1 = 0
t2 = 1
cont = 3

print(f"{t1} -> {t2}", end= "")
while cont <= num:
    t3 = t1 + t2
    print(f" -> {t3}", end= "")
    t1 = t2
    t2 = t3
    cont += 1
print(" -> FIM!")

# 0   1   1   2   3   5   8  13...
#      t1, t2, t3, t4, t5, t6, t7, t8...
# Fiz o while para que o valor de t1, t2 e t3 fiquem mudando constante para depois somá-los.
# Exatamente como a sequência de Fibonacci exige.