num = int(input("Digite um número: "))
for primo in range (1, num+1):
    if num % primo == 0:
        print('\033[33m', end= "")
    else:
        print('\033[34m', end= "")
    print(primo, end= " ")