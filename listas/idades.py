idades = []

while True:
    idade = input("Digite uma idade: ")
    if idade == "":
        break

    idade = int(idade) 
    idades.append(idade)


print("media das idades digitadas: ", sum(idades)/len(idades))
