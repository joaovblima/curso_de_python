numero = input("digite um numero: ")
numero = int(numero)

if numero > 0 and numero % 2 ==0:
    print("Numero positivo e par")
elif numero > 0 and numero % 2 != 0:
    print("Numero positivo e impar")
elif numero < 0 and numero % 2 ==0:
    print("numero negativo e par")
else:
    print("numero negativo e impar")