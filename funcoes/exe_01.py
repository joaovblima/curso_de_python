def par_ou_impar(num:int):
    if num % 2 ==0:
        return "par"
    else:
        return "impar"

numero = input("entre com um numero: ")
numero = int(numero)
print(par_ou_impar(numero))
