num = int(input("Informe um valor a ser convertido: "))
print(''' Essas são as opções de conversão: 
(1) Binário
(2) Octal
(3) Hexadecimal''')

choice = int(input("Opção: "))
if choice == 1:
    print(f"O número {num} convertido em binário é {bin(num)} .")
elif choice == 2:
    print(f"O número {num} convertido em octal é {oct(num)} .")
elif choice == 3:
    print(f"O número {num} convertido para hexadecimal é {hex(num)} .")
else:
    print("Opção inválida!")