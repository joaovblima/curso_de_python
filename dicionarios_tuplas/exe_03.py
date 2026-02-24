dict = {}
while True:
    frase = input("digite a frase: ")
    if frase == "":
        break
    if frase not in dict:
        dict[frase] = 1
    else:
        dict[frase] += 1


for k, v in dict.items():
    print(k,"->",v)
