saldo_em_conta = 0

while True:
    valor = input("Entre com valor: ")
    if valor == "":
        break
    else:
        valor = float(valor)
        saldo_em_conta += valor
    
print("a soma de todos os valores digitados é de: ", saldo_em_conta)


