import numpy as np

km = np.loadtxt('numpy\data\carros-km.txt')
anos = np.loadtxt('numpy\data\carros-anos.txt', dtype=int)


km_media = km / (2019 - anos)
print(type(km_media))