import numpy as np

anos = np.loadtxt(fname = 'numpy\data\carros-anos.txt', dtype=int)
km = np.loadtxt(fname = 'numpy\data\carros-km.txt')
valor = np.loadtxt(fname = 'numpy\data\carros-valor.txt')

# column_stack

dataset = np.column_stack((anos, km, valor)) # transforma em coluna
print(dataset.shape)                         # agora possui 3 colunas (anos, km, valor)

media = np.mean(dataset, axis=0)             # retorna media das colunas
media2 = np.mean(dataset, axis=1)            # ... por linha
media3 = np.mean(dataset[:, 1])

# desvio padrão
desvio_p = np.std(dataset[:, 2])        # retorna o desvio padrão dos elementos do array ao longo do eixo especificado

# somatórios
soma = dataset[:, 1].sum(axis=0)              # retorna a soma dos elementos do array ao longo do eixo especificado

