menu = """
1 - Somar dois números
2 - Subtrair dois números
3 - Multiplicar dois números
4 - Sair
"""
opcao = input(menu)
opcao = int(opcao)
while True:
    if opcao == 1:
        numero_1 = input("primeiro numero: ")
        numero_2 = input("segundo numero: ")
        numero_1 = int(numero_1)
        numero_2 = int(numero_2)
        resultado = numero_1 + numero_2
        print("resultado da soma:", resultado)
        break
    elif opcao == 2:
        numero_1 = input("primeiro numero: ")
        numero_2 = input("segundo numero: ")
        numero_1 = int(numero_1)
        numero_2 = int(numero_2)
        resultado = numero_1 - numero_2
        print("resultado da subtracao:", resultado)
        break
    elif opcao == 3:
        numero_1 = input("primeiro numero: ")
        numero_2 = input("segundo numero: ")
        numero_1 = int(numero_1)
        numero_2 = int(numero_2)
        resultado = numero_1 * numero_2
        print("resultado da multiplicação: ", resultado)
        break
    elif opcao == 4:
        break
    else:
        print("opcao invalida")
        break
