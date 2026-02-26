nome_arquivo = "data.csv"

with open(nome_arquivo) as open_file:
    data = open_file.readlines()
    
for linha in data:
    print(linha)


chaves = data[0].strip("\n").split(";")
print(chaves)
