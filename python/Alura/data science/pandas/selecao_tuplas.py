# seleção simples
nome_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5'])

print(nome_carros[0])   # selecionando indice 0
print(nome_carros[1])   # selecionando indice 1
print(nome_carros[-1])  # selecionando indice -1 (ultimo)
print(nome_carros[1:3]) # slice do indice 1 ao 3-1(2)

# seleção interna
nome_carros_2 = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5',('Fusca', 'Gol', 'C4'))

print(nome_carros_2[-1])     # tupla interna
print(nome_carros_2[-1][1])  # elemento 1 da tupla interna
print(nome_carros_2[-1][-1]) # ultimo elemento da tupla interna
