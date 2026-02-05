
texto1 = """
BEM-VINDO A SORVETERIA .PY
NOSSO CARDÁPIO: 
CASQUINHA (R$1,00) - 1
CASCÃO    (R$2,50) - 2
CESTINHA  (R$4,50) - 3

"""
texto2 = """
SABOR DO SORVETE: 
MORANGO
CREME
CHOCOLATE
"""

texto3 = """
COBERTURA: 
CARAMELO      (R$1,50)   - 1
MORANGO       (R$1,50)   - 2
CHOCOLATE     (R$ 1,50)  - 3
SEM COBERTURA (R$0,00)   - 4
""" 

print(texto1)
escolha_sorvete = input()

print(texto2)
escolha_sabor = input()

print(texto3)
escolha_cobertura = input()

valor_total = 0

if int(escolha_sorvete) == 1:
    valor_total = 1
elif int(escolha_sorvete) == 2:
    valor_total = 2.5
elif int(escolha_sorvete) == 3:
    valor_total = 4
else:
    print("valor inválido.")

if int(escolha_cobertura) == 1:
    valor_total += 1.5
elif int(escolha_cobertura) == 2:
    valor_total += 1.5
elif int(escolha_cobertura) == 3:
    valor_total += 1.5
elif int(escolha_cobertura) == 4:
    valor_total
else:
    print("você selecionou valor errado.")

print("total a pagar é R$", valor_total)