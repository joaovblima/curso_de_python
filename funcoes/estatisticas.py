def soma(a:float, b:float)->float:
    return a + b

def media(a:float, b:float)->float:
    return soma(a, b)/2



valor1 = input("entre com o valor a :")
valor1 = int(valor1)

valor2 = input("entre com o valor b:")
valor2 = int(valor2)

print("media: ", media(valor1, valor2))
