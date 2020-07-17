dados = {'Crossfox': 72832.16, 'Jetta Variant': 88078.64, 'Passat': 106161.94}

# varredura build-in
valores = []
for valor in dados.values():
    valores.append(valor)
print(valores)

# soma
soma = 0
for valor in dados.values():
    soma += valor
print(soma)

# soma build-in
soma_2 = sum(dados.values())
print(soma_2)
