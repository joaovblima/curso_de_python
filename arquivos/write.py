nome_arquivo = "exemplo.txt" 

txt = "GLORIA AO PAI AO FILHO E AO ESPIRITO SANTO"
with open(nome_arquivo, mode="w") as open_file:
    open_file.write(txt)
    
