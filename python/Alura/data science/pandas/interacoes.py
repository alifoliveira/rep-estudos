# Varredura de tupla
nome_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5')

for item in nome_carros:
    print(item)
    
# Desempacotamento de tupla
carro_1, carro_2, carro_3, carro_4 = nome_carros
print(carro_1, carro_2, carro_3, carro_4)

# Zip
carros = ['Jetta Variant', 'Passat', 'Crossfox', 'DS5']
valores = ['88078.64', '106161.94', '72832.16', '124549.07']
lista = list(zip(carros, valores)) # cria uma lista de tuplas no formato (chave, valor)
print(lista)

# Exemplo de utilização do zip
for carro, valor in zip(carros, valores):
    if float(valor) > 100000.0:
        print(carro)