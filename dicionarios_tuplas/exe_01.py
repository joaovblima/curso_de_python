"""
Considere uma lista: [120, "Python", 120.1, "asw", False, [10, 20]]

Faça um programa que retorne as seguintes informações: 
    - elemento na posição -1 da lista
    - elemento na primeira posição da lista
    - O ultimo caractere do seguindo elemento da lista

"""

lista  = [120, "Python", 120.1, "asw", False, [10, 20]]

x = lista[-1]
y = lista[0]
z = lista[1][-1]

print(x, "-", y,"-", z)
