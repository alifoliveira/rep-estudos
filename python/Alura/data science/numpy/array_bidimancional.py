import numpy as np

km2 = np.array([44410., 5712., 37123., 0., 25757.])
anos2 = np.array([2003, 1991, 1990, 2019, 2006])

dados = np.array([km2, anos2]) # array de duas dimensões [x, y]

km_media = dados[0] / (2019 -1)
