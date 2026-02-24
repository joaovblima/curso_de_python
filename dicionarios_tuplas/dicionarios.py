dados_joao = {
    "nome": "joao", 
    "sobrenome": "lima", 
    "idade": 29,
}

dados_teo = {
    "nome": "teo", 
    "filhos": True, 
    "formacao": ["estatistica", "bigdata, datascience"],
    "cargos": [
        {"nome": "ds jr", "empresa": "tapps"}, 
        {"nome": "ds pl", "empresa": "sasa"},
        {"nome": "ds sr", "empresa": "boticario"},
        {"nome": "ds espec", "empresa": "via-varejo"}
    ], 
}

#print(dados_joao)
#print(dados_teo)
#print(dados_teo["formacao"][-1])
#print(dados_teo["cargos"][-1]["empresa"])
#print(dados_teo.keys())
#print(dados_teo.values())

for k, v in dados_teo.items():
    print(k,"->", v)
