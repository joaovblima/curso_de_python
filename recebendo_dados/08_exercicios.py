# %%
print("BEM-VINDO A VENDINHA")
print("ÁGUA MINERAL NATURAL R$ 1,50 - 1")
print("ÁGUA MINERAL COM GÁS R$ 2,50 - 2")
escolha = input("escolha sua compra: ")
escolha = int(escolha)
escolha_quantidade = input("selecione a quantidade: ")
escolha_quantidade = int(escolha_quantidade)

valor_total = 0

if escolha == 1:
    valor_total =  1.5 * escolha_quantidade
    print("Você vai pagar R$", valor_total)
else: 
    valor_total =  2.5 * escolha_quantidade
    print("Você vai pagar R$", valor_total)