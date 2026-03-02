import json
import requests
import pandas as pd
ceps = [
    "57800000",
    "57880000", 
    "57890000",
]

url = "https://viacep.com.br/ws/{cep}/json/"
# cria-se uma lista vazia
dados = []
#um loop na lista de ceps criado acima
for i in ceps:
    #aqui com um get eu pego as informacoes formatando, dou a informação que cep é o elemento i da minha lista de ceps
    resposta = requests.get(url.format(cep=i))
    
    #se a resposta for 200 eu adiciono a lista
    if resposta.status_code == 200:
        dados.append(resposta.json())
        

with open("ceps.json", "w", encoding="utf-8") as of:
    json.dump(dados, of, ensure_ascii=False, indent=4)




