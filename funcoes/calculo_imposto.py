def calc_imposto(preco:float, tx_imposto_base:float, **kwargs):
        imposto =  preco * tx_imposto_base
        
        for i in kwargs:
            print(i, kwargs[i])
            imposto += preco * kwargs[i]

        return imposto

teste = calc_imposto(100, 0.03, municipio=0.01, estadual=0.005, nacional=0.001)
print(teste)
