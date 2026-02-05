numero_1 = input("Digite o primeiro numero: ")
numero_2 = input("Digite o segundo numero: ")
numero_3 = input("Digite o terceiro numero: ")

maior_numero = 0

numero_1 = int(numero_1)
numero_2 = int(numero_2)
numero_3 = int(numero_3)

if numero_1 > numero_2 and numero_1 > numero_3:
    maior_numero = numero_1
elif numero_2 > numero_3 and numero_2 > numero_1:
    maior_numero = numero_2
else:
    maior_numero = numero_3

print("maior numero é", maior_numero)