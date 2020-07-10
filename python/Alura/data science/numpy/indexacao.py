import numpy as np

contador = np.arange(10)

km2 = np.array([44410., 5712., 37123., 0., 25757.])
anos2 = np.array([2003, 1991, 1990, 2019, 2006])
dados = np.array([km2, anos2])

item = 6
index = item - 1

print(contador[index])
print(dados[1][2])      # array[linha][coluna]