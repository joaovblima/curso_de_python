nome_do_arquivo = "historia.txt"

with open(nome_do_arquivo) as open_file:
    conteudo = open_file.read()

print(conteudo)

