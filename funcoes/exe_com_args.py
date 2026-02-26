def soma(a:float, b:float, *args)->float:
    resultado = [a + b] + list(args)
    return sum(resultado)

def media(a:float, b:float, *args)->float:
    return soma(a, b, *args) / (len(args) + 2)


a = float(input("digite o valor a: "))
b = float(input("digite o valor b: "))
c = float(input("digite o valor c: "))
d = float(input("digite o valor d: "))

print("media: ",media(a, b, c,d))
