import numpy as np
import pandas as pa

contador = np.arange(10)

km2 = np.array([44410., 5712., 37123., 0., 25757.])
anos2 = np.array([2003, 1991, 1990, 2019, 2006])
dados = np.array([km2, anos2])

# print(contador[1:8:1]) # array[inicio:fim:passo]

# print(contador[::2]) # indice pares

print(dados[:, 1:3][0] / (2019 - dados[:, 1:3][1]))

print(contador[contador > 5])

print(dados[:, dados[1] > 2000])
