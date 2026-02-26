txt =  "Bem-vindo ao escrevedor de arquivo."
print(txt)
nome_arquivo = input("digite o nome do arquivo que você quer escrever: ")
texto = input("digite o que você quer escrever? ")

with open(nome_arquivo, mode="w") as of:
    of.write(texto)
