dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
print(dados['Passat']) # seleciona valor da chave

# verifica se chave existe
if 'Passat' in dados:
    print('Chave existe')

# exibe quantidade de pares
print(len(dados))

# adicionana novo par ao dicionario
dados['DS5'] = 124549.07
print(dados)

# remove par do dicionario
del dados['Passat']
print(dados)

# atualiza pares / adiciona pares
dados.update({'Passat': 106161.95, 'Fusca': 150000})
print(dados)

# cria cópia independete de dicionario
dados_copy = dados.copy()

del dados_copy['Fusca']

print(dados)
print(dados_copy)

# elimina par e retorna quem foi removido
print(dados_copy.pop('Passat'))

# pop(chave, [defaut]) | defaut = caso não encontre o elemento
print(dados_copy.pop('Passat', 'Chave não encontrada'))

# elimina todos os pares do dicionario
dados_copy.clear()
print(dados_copy)
