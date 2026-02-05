# %%
nome = "joão"

for letra in nome:
    print(letra)

# %%

numero = 2 
max_num = 100

for i in range(1, max_num + 1):
    print(numero, "x", i, "=", numero * i)

# %%
#  numros divisiveis por 4

for i in range(4, 100+1):
    if i % 4 == 0:
        print(i)