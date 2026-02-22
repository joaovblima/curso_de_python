#escreva um programa que receba uma lista do usuario e conte quantas vezes um numero especifico da lista aparece
#solicite um numero e exiba a contagem 

lista = [1, 2, 3, 4, 5, 2, 2, 3, 4, 5]

numero = input("digite um numero: ")
numero = int(numero)

quantidade = 0
for i in lista:
    if i == numero:
        quantidade+=1


print("seu numero", numero, "aparece", quantidade, "vezes na lista")

