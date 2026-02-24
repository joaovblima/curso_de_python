#solicite ao usuario o nome de uma fruta e exiba o preço correspondente


dicionario_de_frutas = {"maçã": 1.50, "pera": 1.25, "goiaba": 2.15, "banana": 2.75, "laranja": 0.65, "abacaxi": 3.20, "uva": 1.9, "limão": 1.25, "jaca": 5.8}

fruta = input("digite a fruta: ")
if fruta in dicionario_de_frutas:
    print("o valor de", fruta,"é: R$",dicionario_de_frutas[fruta])
else:
    print("digite uma fruta que tenha no estoque")

