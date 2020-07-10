import numpy as np

dados = np.array([[44410., 5712., 37123., 0., 25757.],
                 [2003, 1991, 1990, 2019, 1006]])

cont = np.arange(10)

print(dados.shape)      # retorna quantidade de linhas e colunas

print(dados.ndim)       # retorna a quantidade de dimnensões do array

print(dados.size)       # retorna o numeros de elementos do array

print(dados.dtype)      # retorna o tipo de dados do array

print(dados.T)          # retorna o array transposto, coverte linhas em colunas e vice versa

print(dados.transpose)  # mesma função do array.T

print(dados.tolist)     # converte o array para lista do python

print(cont.reshape((5, 2), order='C'))    # retorna array contendo uma nova forma, order='C', order='F

km = [44410, 5712, 37123, 0, 25757]
anos = [2003, 1991, 1990, 2019, 2006]

info_carros = km + anos # concatenação das listas
print(info_carros)
print(np.array(info_carros).reshape((5, 2), order='F')) # concatenação com reshape

dados_new = dados.copy()    # cria uma cópia do array
dados_new.resize((3, 5), refcheck=False)  # adiciona mais uma linha(ou coluna) no array | refcheck ignora referencia
print(dados_new)
dados_new[2] = dados_new[0] / (2019 - dados_new[1])
