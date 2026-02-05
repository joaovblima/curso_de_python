numero = input("Digite um número de 1 a 10 para saber a tabuada: ")
numero = int(numero)

for i in range(1, 11):
    print(numero, "X", i,"=", numero * i)