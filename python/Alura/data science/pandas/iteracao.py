dados = {'Crossfox': 72832.16, 'DS5': 124549.07, 'Fusca': 150000, 'Jetta Variant': 88078.64, 'Passat': 106161.94}

# retorna todas as keys do dict
print(dados.keys())

# retorna os valores das keys
for key in dados.keys():
    print(dados[key]) 

# retorna todos os valores   
print(dados.values())

# retorna lista contendo uma tupla para cada par (chave-valor) do dict
print(dados.items())

# desempacotamento de dict por chave-valor
for key, value in dados.items():
    if value > 100000:
        print(key, value)
    